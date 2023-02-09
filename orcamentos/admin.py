from django.contrib import admin
from .models import CadastroClientes, Proposta, CadastroServico
from monitor.models import CadastroSensore
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Register your models here.

@admin.register(CadastroClientes)
class CadastrodeCliente(admin.ModelAdmin):
    '''Admin View for '''
    list_display = ('name','cnpj')

    
@admin.register(CadastroServico)
class CadastroServico(admin.ModelAdmin):
    list_display = ('name','descricao')



@admin.action(description="Gerar Orçamento")
def GerarPdf(modeladmin,request,queryset):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    n_orc = queryset.values_list('name',flat=True)
    sol_orc = queryset.values_list('solicitante__name',flat=True)
    s_orc = queryset.values_list('servico__name',flat=True)
    # d_serv = queryset.values_list('servico__descricao', flat=True)
    v_orc = queryset.values_list('valor',flat=True)
    image = ".\staticfiles\\admin\\img\\BLACK_320_120.jpg"
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # p.drawString(100,810, "x100")
    # p.drawString(200,810, "x200")
    # p.drawString(300,810, "x300")
    # p.drawString(400,810, "x400")
    # p.drawString(500,810, "x500")

    # p.drawString(10,100, 'y100')
    # p.drawString(10,200, 'y200')
    # p.drawString(10,300, 'y300')
    # p.drawString(10,400, 'y400')
    # p.drawString(10,500, 'y500')
    # p.drawString(10,600, 'y600')
    # p.drawString(10,700, 'y700')
    # p.drawString(10,800, 'y800') 


    p.drawImage(image, 50,740)
    p.setFont('Helvetica',24)
    p.drawString(250, 760, "Proposta Comercial")
    p.line(50,710,550,710)
    p.setFont('Helvetica',12)
    p.drawString(80, 680, f"Ordem de Serviço: {n_orc[0]}")
    p.drawString(360, 680, f"Solicitante: {sol_orc[0]}")
    p.drawString(80,640,"Serviços: ")
    p.drawString(80,600, f"{s_orc[0]}")
    p.line(50,160,550,160)
    p.setFont('Helvetica-Bold',12)
    p.drawString(410, 125, f"Valor Total: {v_orc[0]}")
    p.line(50,100,550,100)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'{n_orc[0]}.pdf')

@admin.register(Proposta)
class Proposta(admin.ModelAdmin):
    list_display = ('name','solicitante','valor')
    actions = [GerarPdf,]
    

@admin.register(CadastroSensore)
class CadastroSensore(admin.ModelAdmin):
    list_display = ('setor','url','modelo')


