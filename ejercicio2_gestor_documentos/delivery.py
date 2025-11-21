from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, formatted_report: str, report_type: str):
        pass


class EmailDelivery(DeliveryStrategy):
    def deliver(self, formatted_report: str, report_type: str):
        print(f"Enviando por email reporte {report_type}...")


class DownloadDelivery(DeliveryStrategy):
    def deliver(self, formatted_report: str, report_type: str):
        filename = f"{report_type}.txt"
        print(f"Descarga lista: {filename}")


class CloudDelivery(DeliveryStrategy):
    def deliver(self, formatted_report: str, report_type: str):
        print(f"Subiendo reporte {report_type} a la nube...")

class DeliveryFactory:
    _registry = {
        "email": EmailDelivery,
        "download": DownloadDelivery,
        "cloud": CloudDelivery,
    }

    @classmethod
    def create(cls, delivery_type: str) -> DeliveryStrategy:
        if delivery_type not in cls._registry:
            raise ValueError(f"Método de entrega no soportado: {delivery_type}")
        return cls._registry[delivery_type]()