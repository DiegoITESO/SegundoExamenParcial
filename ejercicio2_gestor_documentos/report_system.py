from report_content import ReportContentStrategy, ReportContentFactory
from formatter import ReportFormatter, FormatterFactory
from delivery import DeliveryStrategy, DeliveryFactory

class ReportSystemFacade:
    def generate_report(self, report_type: ReportContentStrategy, data: ReportFormatter, output_format, delivery_method: DeliveryStrategy):
        content_strategy = ReportContentFactory.create(report_type)
        formatter = FormatterFactory.create(output_format)
        delivery = DeliveryFactory.create(delivery_method)

        raw_content = content_strategy.generate(data)
        formatted = formatter.format(raw_content)

        delivery.deliver(formatted, report_type)
        return formatted