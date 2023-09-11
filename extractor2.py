from pdf2image import convert_from_path
import pytesseract
import util

from parser_mh import MhParser

POPPLER_PATH = r'C:\poppler-23.05.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract2(file_path, file_format):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)

    if len(pages) > 0:
        page = pages[0]
        im1, im2, im3, im4, im5, im6, im7, im8 = util.preprocess_mh(page)
        text1 = pytesseract.image_to_string(im1, lang='eng')
        text2 = pytesseract.image_to_string(im2, lang='eng')
        text3 = pytesseract.image_to_string(im3, lang='eng')
        text4 = pytesseract.image_to_string(im4, lang='eng')
        text5 = pytesseract.image_to_string(im5, lang='eng')
        text6 = pytesseract.image_to_string(im6, lang='eng')
        text7 = pytesseract.image_to_string(im7, lang='eng')
        text8 = pytesseract.image_to_string(im8, lang='eng')

        extracted_data = f''' 
        'Name': {MhParser(text1).parse()}
        'Number': {MhParser(text1).parse2()}
        'Gender': {MhParser(text1).parse3()}
        'Condition': {MhParser(text2).parse4()}
        'Symptoms': {MhParser(text3).parse5()}
        'Medication': {MhParser(text4).parse6()}
        'Allergy': {MhParser(text5).parse7()}
        'Tobacco': {MhParser(text6).parse8()}
        'Drugs':{MhParser(text7).parse9()}
        'Alcohol': {MhParser(text8).parse10()}
'''

    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data


