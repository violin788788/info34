from pypdf import PdfReader


def pdf_to_txt(pdf_path):
  print("generating, can take like 30 seconds")

  reader = PdfReader(pdf_path)
  text = " ".join(
      page.extract_text().replace("\n", " ") for page in reader.pages
  )
  txt_path = pdf_path.rsplit(".", 1)[0] + ".txt"
  with open(txt_path, "w", encoding="utf-8") as f:
    f.write(text)
  print ("created",txt_path,"of", pdf_path)


file = "fed.pdf"

pdf_to_txt(file)