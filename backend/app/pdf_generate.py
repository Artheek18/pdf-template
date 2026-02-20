from fpdf import FPDF
import pandas as pd

import fpdf
print("fpdf version:", fpdf.__version__)


def build_pdf_from_df(df: pd.DataFrame, output_path: str) -> None:
    pdf = FPDF(orientation='P',unit='mm',format = 'A4')
    pdf.set_auto_page_break(auto=False, margin=0)


    #Create Table of Contents
    pdf.add_page()
    toc_page_num = pdf.page_no()  # will be 1
    pdf.set_font('Helvetica', 'B', size=18)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(w=0, h=12, txt="Table of Contents", ln=1, align='L')
    pdf.ln(4)

    toc_start_y = pdf.get_y()
    toc_entries = []
    df = df.sort_values(by="Order", kind="stable")

    for index, rows in df.iterrows():
        pages = int(rows["Pages"])
        lessons = str(rows["Topic"])
        order = rows["Order"]


        #Creating Main Page
        pdf.add_page()
        start_page = pdf.page_no()
        toc_entries.append((order, lessons, start_page))
        pdf.set_font('Helvetica','B',size=25)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=lessons, ln=1, align='L')


        #Lines for notes
        for page_line in range(21, 292, 10):
            pdf.line(10, page_line, 200, page_line)

        #Set Footer
        pdf.set_y(-9)
        pdf.set_text_color(180,180,180)
        pdf.set_font('Times', 'I', size=9)
        pdf.cell(w=0, h=12, txt=lessons, align='R')

        #Adding Multiple Pages
        if pages > 1:
            for i in range(1, pages):
                #Add Page
                pdf.add_page()

                # Lines for notes
                for page_line in range(21, 292, 10):
                    pdf.line(10, page_line, 200, page_line)

                #Set Footer
                pdf.set_y(-9)
                pdf.set_text_color(180, 180, 180)
                pdf.set_font('Times', 'I', size=9)
                pdf.cell(w=0, h=12, txt=lessons, align='R')

        #print(rows[["Topic", 'Pages']])
        #print("After adding topic page, current page:", pdf.page_no())

    pdf.page = toc_page_num
    pdf.set_y(toc_start_y)

    pdf.set_font('Times', '', size=11)
    pdf.set_text_color(100, 100, 100)

    left_margin = 10
    right_margin = 200
    usable_width = right_margin - left_margin

    for order, topic, start_page in toc_entries:
        left_text = f"{order}. {topic}"
        right_text = str(start_page)

        # Measure text widths
        left_width = pdf.get_string_width(left_text)
        right_width = pdf.get_string_width(right_text)

        # How much space is left for dots?
        dots_width = usable_width - left_width - right_width - 4  # small padding

        # Width of a single dot
        dot_width = pdf.get_string_width(".")

        # Number of dots needed
        num_dots = max(0, int(dots_width / dot_width))

        dots = "." * num_dots

        # Print line
        pdf.set_x(left_margin)
        pdf.cell(left_width, 8, left_text, ln=0)
        pdf.cell(dots_width, 8, dots, ln=0)
        pdf.cell(0, 8, right_text, ln=1, align="R")

    pdf.page = len(pdf.pages)
    pdf.output("output_path")