import mongoengine


class CheckModel(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'checks'
    }

    id = mongoengine.UUIDField(primary_key=True)
    sending_status = mongoengine.StringField(max_length=50, required=True)  # отправлен/ не отправлен
    payment_status = mongoengine.StringField(max_length=50, required=True)  # оплата прошла/ не прошла
    check_data = mongoengine.StringField(max_length=800, required=True)  # типо товары в чеке
    # payment_method = Column(String(50))
    card_number = mongoengine.StringField(max_length=16, required=True)
    user_id = mongoengine.StringField(max_length=200, required=True)
    check_price = mongoengine.IntField(max_length=200, required=True)


class UserCard(mongoengine.Document):
    meta = {
        'db_alias': 'mydb',
        'collection': 'cards'
    }

    id = mongoengine.UUIDField(primary_key=True)
    card_number = mongoengine.StringField(max_length=16, required=True)
    user_id = mongoengine.StringField(max_length=200, required=True)

