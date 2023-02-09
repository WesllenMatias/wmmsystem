
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Image, SimpleDocTemplate, Table

def create_budget_with_logo(data):
    doc = SimpleDocTemplate("budget.pdf", pagesize=landscape(letter))

    # Adiciona a imagem do logo
    # logo = Image(logo_path)
    # logo.drawHeight = 1.5*inch*logo.drawHeight / logo.drawWidth
    # logo.drawWidth = 1.5*inch

    # Cria a tabela de dados
    table_data = [['Item', 'Quantidade', 'Preço']]
    for item in data:
        table_data.append([item['name'], item['quantity'], item['price']])
    table = Table(table_data)

    # Adiciona estilo à tabela
    table.setStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Adiciona a tabela e o logo ao documento
    doc.build([table])

# Exemplo de uso
data = [{'name': 'item1', 'quantity': 2, 'price': 10.99},
        {'name': 'item2', 'quantity': 1, 'price': 5.99}]
create_budget_with_logo(data)
