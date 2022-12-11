from fastapi import APIRouter, status, HTTPException
from schemas import Category, PostCategory, PaymentM, PostPayment
from utils import generate_payment_from_gateway

router = APIRouter(
    tags=['Gateway'],
    prefix='/gateway',
)

serial = 5
payments = generate_payment_from_gateway(serial)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[PaymentM])
async def get_all_payments():
    return payments


@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=PaymentM)
async def add_new_payment(payment: PostPayment):
    global serial
    new_payment = PaymentM(
        id=serial,
        satus=payment.status,
    )
    serial += 1
    payments.append(new_payment)
    return new_payment

