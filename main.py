#! env python
from pikepdf import Pdf

with Pdf.open('./data/a.pdf') as a, Pdf.open('./data/b.pdf') as b:
    a.pages[0] = b.pages[0]
    a.pages.append(b.pages[1])
    a.save('./data/c.pdf')
