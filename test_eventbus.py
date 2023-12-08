import unittest
from unittest.mock import Mock

from eventbus import EventBus

class TestEventBus(unittest.TestCase):

    def setUp(self):
        self.event_bus = EventBus()

    def test_subscribe_and_publish(self):
        # Configuración
        event_type = "test_event"
        handler_mock = Mock()
        data = {"key": "value"}

        # Suscribir al evento
        self.event_bus.subscribe(event_type, handler_mock)

        # Publicar el evento
        self.event_bus.publish(event_type, data)

        # Verificar que el manejador fue llamado con los datos correctos
        handler_mock.assert_called_once_with(data)

    def test_unsubscribe(self):
        # Configuración
        event_type = "test_event"
        handler_mock = Mock()

        # Suscribir y luego cancelar la suscripción
        self.event_bus.subscribe(event_type, handler_mock)
        self.event_bus.unsubscribe(event_type, handler_mock)

        # Publicar el evento (no debería llamar al manejador)
        self.event_bus.publish(event_type, {"key": "value"})

        # Verificar que el manejador no fue llamado
        handler_mock.assert_not_called()

    def test_unsubscribe_nonexistent_handler(self):
        # Configuración
        event_type = "test_event"
        handler_mock = Mock()

        # Intentar cancelar la suscripción a un manejador no suscrito
        self.event_bus.unsubscribe(event_type, handler_mock)

        # No debería haber errores aunque el manejador no esté suscrito
        handler_mock.assert_not_called()

    def test_subscribe_multiple_handlers(self):
        # Configuración
        event_type = "test_event"
        handler1_mock = Mock()
        handler2_mock = Mock()
        data = {"key": "value"}

        # Suscribir dos manejadores al mismo evento
        self.event_bus.subscribe(event_type, handler1_mock)
        self.event_bus.subscribe(event_type, handler2_mock)

        # Publicar el evento
        self.event_bus.publish(event_type, data)

        # Verificar que ambos manejadores fueron llamados con los datos correctos
        handler1_mock.assert_called_once_with(data)
        handler2_mock.assert_called_once_with(data)

if __name__ == '__main__':
    unittest.main()
