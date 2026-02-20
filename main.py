from fpdf import FPDF

pdf = FPDF(orientation='P',unit='mm',format = 'A4')
pdf.add_page()
pdf.set_font('Helvetica','B',size=12)
pdf.cell(w=0, h=12, txt="Hello", ln=1, align='C',border=1)
pdf.cell(w=0, h=12, txt="My name is Artheeck Shan", ln=1, align='L',border=1)
pdf.output("output.pdf")