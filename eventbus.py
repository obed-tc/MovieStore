from typing import Callable, Any
import threading

class EventBus:
    def __init__(self):
        self.handlers = {}
        self.lock = threading.Lock()

    def subscribe(self, event_type: str, handler: Callable[[Any], None]):
        with self.lock:
            if event_type not in self.handlers:
                self.handlers[event_type] = []
            self.handlers[event_type].append(handler)

    def publish(self, event_type: str, data: Any):
        with self.lock:
            if event_type in self.handlers:
                for handler in self.handlers[event_type]:
                    handler(data)
    def unsubscribe(self, event_type: str, handler: Callable[[Any], None]):
        with self.lock:
            if event_type in self.handlers and handler in self.handlers[event_type]:
                self.handlers[event_type].remove(handler)

