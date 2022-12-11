from pydantic import BaseModel


class PostCategory(BaseModel):
    name: str


class Category(PostCategory):
    id: int


class PostPayment(BaseModel):
    status: str


class PaymentM(PostPayment):
    id: int
