import PyPDF2
import pyttsx3

# abre o PDf ( ebook.pdf)

path = open('Introdução ao Python.pdf','rb')
pdf_reader = PyPDF2.PdfReader(path)

spaek = pyttsx3.init()


# Percorre as páginas do PDF, Extrai os texto e faz a leitura

for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    spaek.say(text)
    spaek.runAndWait()
spaek.stop()