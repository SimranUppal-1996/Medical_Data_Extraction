from pdf2image import convert_from_path
import pytesseract
import util

from parser_vr import VrParser


POPPLER_PATH = r'C:\poppler-23.05.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract1(file_path, file_format):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    if len(pages)>0:
        page = pages[0]
        processed_image = util.preprocess_vr(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text

    # step 2: extract fields from text
    if file_format == 'vr':
        extracted_data = VrParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data
