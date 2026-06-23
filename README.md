# PDF ↔ DOCX Converter

A simple Python project that converts:

* PDF files to DOCX format using `pdf2docx`
* DOCX files to PDF format using `docx2pdf`

## Features

* Convert PDF documents into editable Word files.
* Convert Word documents into PDF format.
* Easy to use and beginner-friendly.
* Lightweight Python script.

## Technologies Used

* Python
* pdf2docx
* docx2pdf

## Installation

```bash
pip install pdf2docx
pip install docx2pdf
```

## Usage

### PDF to DOCX

```python
from pdf2docx import Converter

old_pdf = "sample.pdf"
new_doc = "sample.docx"

cv = Converter(old_pdf)
cv.convert(new_doc)
cv.close()
```

### DOCX to PDF

```python
from docx2pdf import convert

convert("sample.docx", "sample.pdf")
```

