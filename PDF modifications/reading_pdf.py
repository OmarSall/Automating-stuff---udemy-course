import PyPDF2, os

os.chdir('E:\\Python Udemy\\Automate boting stuff with Python programming course\\excel')

# pdfFile = open('meetingminutes1.pdf', 'rb')

# reader = PyPDF2.PdfFileReader(pdfFile)
# print(reader.numPages)

# page = reader.getPage(0)

# page.extractText()

# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)


outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()
