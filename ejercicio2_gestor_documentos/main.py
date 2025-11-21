import json
from report_system import ReportSystemFacade

if __name__ == "__main__":
    system = ReportSystemFacade()
    sales_data = {
        "period": "Enero 2024",
        "sales": [
            {"product": "Laptop HP", "amount": 899.99},
            {"product": "Mouse Logitech", "amount": 25.50},
            {"product": "Teclado Mecánico", "amount": 120.00},
            {"product": "Monitor LG 24\"", "amount": 199.99}
        ]
    }
    print("\nGenerando reporte de ventas (PDF - Email)...")
    system.generate_report("sales", sales_data, "pdf", "email")
    inventory_data = {
        "items": [
            {"name": "Laptop HP", "category": "Computadoras", "quantity": 15},
            {"name": "Mouse Logitech", "category": "Accesorios", "quantity": 50},
            {"name": "Teclado Mecánico", "category": "Accesorios", "quantity": 30},
            {"name": "Monitor LG", "category": "Pantallas", "quantity": 20}
        ]
    }

    print("\nGenerando reporte de inventario (Excel - Download)...")
    system.generate_report("inventory", inventory_data, "excel", "download")

    financial_data = {
        "income": 50000.00,
        "expenses": 32000.00
    }

    print("\nGenerando reporte financiero (HTML - Cloud)...")
    system.generate_report("financial", financial_data, "html", "cloud")
