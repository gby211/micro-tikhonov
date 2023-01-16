import opentracing

import schemas
import models
from opentracing_instrumentation.request_context import get_current_span, span_in_context


def mapping_model_schema(model: models.CheckModel):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_model_schema.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            schema = schemas.Check(
                id=model.id,
                user_id=model.user_id,
                sending_status=model.sending_status,
                payment_status=model.payment_status,
                card_number=model.card_number,
                check_data=model.check_data,
                check_price=model.check_price
            )
            return schema


def mapping_schema_model(schema: schemas.Check):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_schema_model.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            model = schemas.Check(
                id=schema.id,
                user_id=schema.user_id,
                sending_status=schema.sending_status,
                payment_status=schema.payment_status,
                card_number=schema.card_number,
                check_data=schema.check_data,
                check_price=schema.check_price
            )
            return model


def mapping_model_schema_card(model: models.UserCard):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_model_schema_card.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            schema = schemas.Card(
                id=model.id,
                user_id=model.user_id,
                card_number=model.card_number
            )
            return schema


def mapping_schema_model_card(schema: schemas.Card):
    tracer = opentracing.global_tracer()
    with tracer.start_span(mapping_schema_model_card.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            model = schemas.Card(
                id=schema.id,
                user_id=schema.user_id,
                card_number=schema.card_number
            )
            return model
