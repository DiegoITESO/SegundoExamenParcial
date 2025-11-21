

class Customer:
    def __init__(self, name: str, email: str, phone: str, device_id: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.device_id = device_id

class Order:
    def __init__(self, order_id: str, customer: Customer, total: float):
        self.order_id = order_id
        self.customer = customer
        self.total = total
