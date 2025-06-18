
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
shirt = pdf.image("shirtificate.png", x=30, y=50, w=150)

pdf.set_font("helvetica", "B", 40)
pdf.text(x=48, y=30, txt="CS50 Shirtificate")

pdf.set_text_color(255)
pdf.set_font("helvetica", "B", 25)
name = input("Name: ").strip().title() + " took CS50"
pdf.multi_cell(w=189, h=170, txt=name, border=0, align="C")

pdf.output("shirtificate.pdf")




