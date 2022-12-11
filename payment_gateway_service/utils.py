import uuid
import random

from schemas import PaymentM


desc = ['ok', 'wait', 'close']


def generate_payment_from_gateway(number) -> list[PaymentM]:
    return [
        PaymentM(
            id=i,
            status=random.choice(desc),
        ) for i in range(number)
    ]
