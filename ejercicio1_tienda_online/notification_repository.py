from order import Order

class NotificationRepository:
    def __init__(self):
        self._data = []
    
    def save(self, notification: dict):
        self._data.append(notification)
    
    def get_all(self):
        return self._data