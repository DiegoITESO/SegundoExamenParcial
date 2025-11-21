from abc import ABC, abstractmethod
from datetime import datetime

class ReportContentStrategy(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        pass


class SalesReportContent(ReportContentStrategy):
    def generate(self, data: dict) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_sales = sum(item['amount'] for item in data['sales'])

        content = []
        content.append("====== REPORTE DE VENTAS ======")
        content.append(f"Fecha: {timestamp}\n")
        content.append(f"Total ventas: ${total_sales:.2f}")
        content.append(f"Transacciones: {len(data['sales'])}")
        content.append(f"Periodo: {data['period']}\n")
        content.append("Detalle:")
        for sale in data['sales']:
            content.append(f" - {sale['product']} : ${sale['amount']:.2f}")
        return "\n".join(content)


class InventoryReportContent(ReportContentStrategy):
    def generate(self, data: dict) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_items = sum(item['quantity'] for item in data['items'])

        content = []
        content.append("====== REPORTE DE INVENTARIO ======")
        content.append(f"Fecha: {timestamp}\n")
        content.append(f"Total productos: {total_items}")
        content.append(f"Categorías: {len(set(i['category'] for i in data['items']))}\n")
        content.append("Inventario:")
        for item in data['items']:
            content.append(
                f" - {item['name']} ({item['category']}): {item['quantity']} unidades"
            )
        return "\n".join(content)


class FinancialReportContent(ReportContentStrategy):
    def generate(self, data: dict) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        balance = data['income'] - data['expenses']

        content = []
        content.append("====== REPORTE FINANCIERO ======")
        content.append(f"Fecha: {timestamp}\n")
        content.append(f"Ingresos: ${data['income']:.2f}")
        content.append(f"Gastos: ${data['expenses']:.2f}")
        content.append(f"Balance: ${balance:.2f}")
        return "\n".join(content)
    
class ReportContentFactory:
    _registry = {
        "sales": SalesReportContent,
        "inventory": InventoryReportContent,
        "financial": FinancialReportContent,
    }

    @classmethod
    def create(cls, report_type: str) -> ReportContentStrategy:
        if report_type not in cls._registry:
            raise ValueError(f"Tipo de reporte no soportado: {report_type}")
        return cls._registry[report_type]()