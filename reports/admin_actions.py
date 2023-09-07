from django.http import HttpResponse
from django.urls import reverse
from easy_pdf.views import PDFTemplateView


class ReportPDF(PDFTemplateView):
    template_name = 'report_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione aqui os dados do relatório
        return context


def generate_report_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    report_url = reverse('admin:report_pdf')
    report_pdf = ReportPDF.as_view()
    return report_pdf(request=request).get(request=request, url=report_url)
generate_report_pdf.short_description = 'Gerar relatório em PDF'


