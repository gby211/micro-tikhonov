from pydantic import BaseModel


class PostProduct(BaseModel):
    name: str
    description: str
    price: int


class Product(PostProduct):
    id: int


class BasePaymentMethod(BaseModel):
    payment_type: str
    card_number: str


class CreatePaymentMethod(BasePaymentMethod):
    ...


class PaymentMethod(BasePaymentMethod):
    id: int
    user_id: str

    class Config:
        orm_mode = True


class BaseCheck(BaseModel):
    user_id: str
    sending_status: str
    payment_status: str
    card_number: str
    check_data: str


class CreateCheck(BaseCheck):
    ...


class Check(BaseCheck):
    id: int

    class Config:
        orm_mode = True
