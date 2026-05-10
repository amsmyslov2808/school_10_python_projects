from my_word_document import MyWordDocument
from txt_document_worker import TxtDocumentWorker
from pdf_document_worker import PdfDocumentWorker
from csv_document_worker import CsvDocumentWorker

doc = MyWordDocument()
doc.print_info()

doc.save(TxtDocumentWorker("file.txt"))
doc.save(PdfDocumentWorker("file.pdf"))
doc.save(CsvDocumentWorker("file.csv"))

# doc.save_to_txt(TxtDocumentWorker("file.txt"), 1)
# doc.save_to_txt(TxtDocumentWorker("file10.txt"), 1)
# doc.load_from_txt(TxtDocumentWorker("file3.txt"))


# txt_document_worker2 = TxtDocumentWorker("file2.txt")
# doc2 = MyWordDocument()

# doc2.load_from_txt(TxtDocumentWorker("file3.txt"))
# doc.save_to_txt(TxtDocumentWorker("file3333.txt"))
