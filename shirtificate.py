from fpdf import FPDF, Align

from fpdf import Align


class PDF(FPDF):
    def header(self):
        # Rendering logo:

        self.image("shirtificate.png",w=pdf.epw, h=pdf.eph,  y=25, x=Align.C)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=20)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate",  align="C")


    def footer(self):
        #
        #user_input=input("Name:")
        self.set_font("helvetica", style="B", size=30)
        self.set_text_color(255, 255, 255)
        user_input=input("Name:")

        self.cell(-20, 200, f"{user_input} took cs50",  align="C")










# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")




