import opentracing
from fastapi import APIRouter, status, HTTPException
from schemas import Product, PostProduct, Check, CreateCheck
from utils import generate_check
import services
import mappers
from opentracing_instrumentation.request_context import get_current_span, span_in_context


router = APIRouter(
    tags=['Payment'],
    prefix='/payment',
)

serial = 5
checks = generate_check(serial)


@router.get('/', status_code=200, response_model=list[Check])
async def get_all_checks():
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_checks.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            checks = await services.get_all_checks()
            output = [
                mappers.mapping_model_schema(check)
                for check in checks
            ]
            return output


# Don't work with '/', redirect error
@router.post('/add', status_code=201, response_model=Check)
async def add_new_check(check: CreateCheck):
    tracer = opentracing.global_tracer()
    with tracer.start_span(add_new_check.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            act = await services.add_new_check(check)
            return mappers.mapping_model_schema(act)

    # global serial
    # new_check = Check(
    #     id=serial,
    #     user_id=check.user_id,
    #     sending_status=check.sending_status,
    #     payment_status=check.payment_status,
    #     card_number=check.card_number,
    #     check_data=check.check_data,
    #     check_price=check.check_price
    # )
    # serial += 1
    # checks.append(new_check)
    # return new_check
