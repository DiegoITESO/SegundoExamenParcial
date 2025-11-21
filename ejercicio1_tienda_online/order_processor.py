from notification_repository import NotificationRepository
from order import Order
from notifier import Notifier

class OrderProcessor:
    def __init__(self, repository: NotificationRepository):
        self._repository = repository

    def process_order(self, order: Order, notifiers: list[Notifier]):
        for notifier in notifiers:
            notification = notifier.notify(order)
            self._repository.save(notification)
        
    def get_notification_history(self):
        return self._repository.get_all().copy()
    
