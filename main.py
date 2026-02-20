from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")
pdf = FPDF(orientation='P',unit='mm',format = 'A4')
pdf.set_auto_page_break(auto=False, margin=0)


for index, rows in df.iterrows():
    #Creating Main Page
    pdf.add_page()
    pdf.set_font('Helvetica','B',size=25)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=rows["Topic"], ln=1, align='L')
    pdf.line(10, 21, 200, 21)

    #Set Footer
    pdf.ln(255)
    pdf.set_text_color(180,180,180)
    pdf.set_font('Times', 'I', size=9)
    pdf.cell(w=0, h=12, txt=rows["Topic"], align='R')

    #Adding Multiple Pages
    if rows["Pages"] >= 1:
        for i in range(1, rows["Pages"]):
            pdf.add_page()
            pdf.ln(267)
            pdf.set_text_color(180, 180, 180)
            pdf.set_font('Times', 'I', size=9)
            pdf.cell(w=0, h=12, txt=rows["Topic"], align='R')

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