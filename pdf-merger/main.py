from PyPDF2 import PdfWriter

merger = PdfWriter()
n = int(input("How many pdfs you want to merge?\n"))

for i in range (n):
    name = input(f"Write the name of the pdf {i + 1}: ")
    merger.append(name)

merger.write("Merged.pdf")
merger.close()