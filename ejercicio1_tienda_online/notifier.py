from abc import ABC, abstractmethod
from order import Order, Customer
from datetime import datetime

class Notifier(ABC):
    @abstractmethod
    def notify(self, order: Order):
        pass


class EmailNotifier(Notifier):
    def notify(self, order: Order):
        customer = order.customer
        total = order.total
        order_id = order.order_id

        message = (
            f"Estimado {customer.name}, "
            f"su pedido #{order_id} por ${total} ha sido confirmado."
        )

        print(f"EMAIL → {customer.email}")
        print(f"  Mensaje: {message}\n")

        return {
            "type": "email",
            "to": customer.email,
            "message": message,
            "order_id": order_id,
            "timestamp": datetime.now().isoformat()
        }


class SMSNotifier(Notifier):
    def notify(self, order: Order):
        customer = order.customer
        total = order.total
        order_id = order.order_id

        message = f"Pedido #{order_id} confirmado. Total: ${total}."

        print(f"SMS → {customer.phone}")
        print(f"  Mensaje: {message}\n")

        return {
            "type": "SMS",
            "to": customer.phone,
            "message": message,
            "order_id": order_id,
            "timestamp": datetime.now().isoformat()
        }


class PushNotifier(Notifier):
    def notify(self, order: Order):
        customer = order.customer
        total = order.total
        order_id = order.order_id

        message = f"Pedido confirmado #{order_id} - ${total}"

        print(f"PUSH → {customer.device_id}")
        print(f"  Mensaje: {message}\n")

        return {
            "type": "Push",
            "to": customer.device_id,
            "message": message,
            "order_id": order_id,
            "timestamp": datetime.now().isoformat()
        }


class NotifierFactory:
    _registry = {
        "email": EmailNotifier,
        "sms": SMSNotifier,
        "push": PushNotifier
    }

    @classmethod
    def create_notifier(cls, notif_type: str) -> Notifier:
        if notif_type not in cls._registry:
            raise ValueError(f"Canal de notificación no soportado: {notif_type}")

        return cls._registry[notif_type]()
