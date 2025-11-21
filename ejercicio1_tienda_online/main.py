from order import Order, Customer
from notifier import NotifierFactory
from order_processor import OrderProcessor
from notification_repository import NotificationRepository
import json

if __name__ == "__main__":
    repository = NotificationRepository()
    processor = OrderProcessor(repository)

    customer1 = Customer(
        name="Ana García",
        email="ana.garcia@email.com",
        phone="+34-600-123-456",
        device_id="DEVICE-ABC-123"
    )

    order1 = Order(
        order_id="ORD-001",
        customer=customer1,
        total=150.50
    )

    notifier_types_1 = ["email", "sms", "push"]
    notifiers_1 = [NotifierFactory.create_notifier(t) for t in notifier_types_1]

    processor.process_order(order1, notifiers_1)

    customer2 = Customer(
        name="Carlos Ruiz",
        email="carlos.ruiz@email.com",
        phone="+34-600-789-012",
        device_id="DEVICE-XYZ-789"
    )

    order2 = Order(
        order_id="ORD-002",
        customer=customer2,
        total=75.00
    )

    notifier_types_2 = ["email"]
    notifiers_2 = [NotifierFactory.create_notifier(t) for t in notifier_types_2]

    processor.process_order(order2, notifiers_2)

    print("\n" + "=" * 50)
    print("HISTORIAL DE NOTIFICACIONES")
    print("=" * 50)

    history = processor.get_notification_history()
    print(json.dumps(history, indent=2, ensure_ascii=False))