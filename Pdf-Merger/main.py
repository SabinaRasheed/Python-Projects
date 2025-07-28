from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
num=int(input('enter the number of pdfs you want to merge:'))

for i in range(0,num):
    pdf_name= input(f'Enter the name of PDF file {i+1}:')
    pdfs.append(pdf_name)


for pdf in pdfs:
    merger.append(pdf)
    
merger.write("merged-pdf.pdf")
merger.close()
