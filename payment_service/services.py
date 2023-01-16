import opentracing

from models import CheckModel, UserCard
import schemas
import uuid
from opentracing_instrumentation.request_context import get_current_span, span_in_context


async def get_all_checks() -> list[CheckModel]:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_all_checks.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            return CheckModel.objects


async def get_cards_by_userid(user_id: str) -> list[UserCard]:
    tracer = opentracing.global_tracer()
    with tracer.start_span(get_cards_by_userid.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            all_cards = []
            for card in UserCard.objects:
                if card.user_id == user_id:
                    all_cards.append(card)
            return all_cards


async def add_new_card(schema: schemas.BaseUserCard) -> UserCard:
    tracer = opentracing.global_tracer()
    with tracer.start_span(add_new_card.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            mod = UserCard(
                id=uuid.uuid4(),
                user_id=schema.user_id,
                card_number=schema.card_number
            )
            mod.save()
            return mod


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
