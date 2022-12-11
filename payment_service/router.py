from fastapi import APIRouter, status, HTTPException
from schemas import Product, PostProduct, Check, CreateCheck
from utils import generate_check


router = APIRouter(
    tags=['Payment'],
    prefix='/payment',
)

serial = 5
checks = generate_check(serial)


@router.get('/', status_code=200, response_model=list[Check])
async def get_all_checks():
    return checks


# Don't work with '/', redirect error
@router.post('/add', status_code=201, response_model=Check)
async def add_new_check(check: CreateCheck):
    global serial
    new_check = Check(
        id=serial,
        user_id=check.user_id,
        sending_status=check.sending_status,
        payment_status=check.payment_status,
        card_number=check.card_number,
        check_data=check.check_data
    )
    serial += 1
    checks.append(new_check)
    return new_check


