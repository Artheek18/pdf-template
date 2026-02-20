from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")
pdf = FPDF(orientation='P',unit='mm',format = 'A4')
for index, rows in df.iterrows():
    pdf.add_page()
    pdf.set_font('Helvetica','B',size=25)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=rows["Topic"], ln=1, align='L')
    pdf.line(10, 21, 200, 21)

    #print(rows[["Topic", 'Pages']])

""" 
pdf.add_page()
pdf.set_font('Helvetica','B',size=12)
pdf.cell(w=0, h=12, txt="Hello", ln=1, align='C',border=1)
pdf.cell(w=0, h=12, txt="My name is Artheeck Shan", ln=1, align='L',border=1)

pdf.add_page()
pdf.set_font('Helvetica','B',size=12)
pdf.cell(w=0, h=12, txt="How are you?", ln=1, align='C',border=1)
pdf.cell(w=0, h=12, txt="Im doing well shordie", ln=1, align='L',border=1)
"""



pdf.output("output.pdf")