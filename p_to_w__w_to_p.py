
# CONVERT PDF TO DOCX

# from pdf2docx import Converter
# old_pdf = 'IMRAN_BSCS.pdf'
# new_doc =  'IMRAN_BSCS.docx'

# cv = Converter(old_pdf)
# cv.convert(new_doc)
# cv.close()

# CONVERT DOCX TO PDF
from docx2pdf import convert
convert("IMRAN_BSCS.docx","IMRAN_BSC.pdf")
