from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource


def configure_tracer():
    # Установка имени сервиса
    resource = Resource(attributes={
        SERVICE_NAME: "movies-api"
    })
    # Создаем провайдера трейсера
    trace.set_tracer_provider(TracerProvider(resource=resource))

    jaeger_exporter = JaegerExporter(
        agent_host_name="jaeger",  # Это имя контейнера в docker-compose
        agent_port=6831,
    )

    # Добавляем SpanProcessor для отправки данных в Jaeger
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    # Возвращаем трейсера для использования в приложении
    return trace.get_tracer(__name__)


def init_tracer(app):
    configure_tracer()
    FastAPIInstrumentor.instrument_app(app)
