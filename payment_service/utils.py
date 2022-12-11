import uuid
import random

from schemas import Check

desc = ['ok', 'wait', 'close']
desc1 = ['bla bla bla', 'tra lia lia', 'ko ko ko']


def generate_check(number) -> list[Check]:
    return [
        Check(
            id=i,
            user_id=str(uuid.uuid4()),
            sending_status=random.choice(desc),
            payment_status=random.choice(desc),
            card_number=random.randint(1000000000000000, 9999999999999999),
            check_data=random.choice(desc1),
            check_price=random.randint(1,1000000)
        ) for i in range(number)
    ]
