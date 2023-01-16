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
    sending_status: str
    payment_status: str
    check_data: str
    card_number: str
    user_id: str
    check_price: int


class CreateCheck(BaseCheck):
    ...


class Check(BaseCheck):
    id: int

    class Config:
        orm_mode = True


class BaseUserCard(BaseModel):
    user_id: str
    card_number: str


class Card(BaseUserCard):
    id: int
