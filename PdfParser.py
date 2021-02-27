from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdf(input_paths, output_path, filename):
    if filename == "":
        filename = "out"

    writer = PdfFileWriter()
    for i in input_paths:
        pdf_reader = PdfFileReader(i)
        for page in range(pdf_reader.getNumPages()):
            writer.addPage(pdf_reader.getPage(page))
    with open(output_path + filename + ".pdf", "wb") as f_out:
        writer.write(f_out)


def split_pdf(path, num):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for page in range(num):
            writer = PdfFileWriter()
            writer.addPage(pdf.getPage(page))
            with open(f"{page}.pdf", "wb") as f_out:
                writer.write(f_out)
