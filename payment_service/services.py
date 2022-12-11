import opentracing

from models import CheckModel
import schemas
import uuid
from opentracing_instrumentation.request_context import get_current_span, span_in_context

async def get_all_checks() -> list[CheckModel]:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_checks.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            return CheckModel.objects


async def add_new_check(schema: schemas.Check) -> CheckModel:
    tracer = opentracing.global_tracer()
    with tracer.start_span(add_new_check.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            mod = CheckModel(
                id=uuid.uuid4(),
                user_id=schema.user_id,  # uuid.uuid4()
                sending_status=schema.sending_status,
                payment_status=schema.payment_status,
                card_number=schema.card_number,
                check_data=schema.check_data,
                check_price=schema.check_price
            )
            mod.save()
            return mod
