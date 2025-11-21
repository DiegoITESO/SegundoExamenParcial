from abc import ABC, abstractmethod

class ReportFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass


class PDFFormatter(ReportFormatter):
    def format(self, text: str) -> str:
        return f"[PDF]\n{text}\n[/PDF]"


class ExcelFormatter(ReportFormatter):
    def format(self, text: str) -> str:
        return f"[EXCEL]\n{text}\n[/EXCEL]"


class HTMLFormatter(ReportFormatter):
    def format(self, text: str) -> str:
        return f"<html><body><pre>{text}</pre></body></html>"
    
class FormatterFactory:
    _registry = {
        "pdf": PDFFormatter,
        "excel": ExcelFormatter,
        "html": HTMLFormatter,
    }

    @classmethod
    def create(cls, format_type: str) -> ReportFormatter:
        if format_type not in cls._registry:
            raise ValueError(f"Formato no soportado: {format_type}")
        return cls._registry[format_type]()