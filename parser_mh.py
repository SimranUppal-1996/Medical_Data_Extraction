import re
from backend.src.parser_generic import MedicalDocParser


class MhParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        pattern = r'(.*) \(\d{2}\)'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse2(self):
        pattern = r'\(\d{2}\) \d{3}-\d{7}'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse3(self):
        pattern = r'Male|Female'
        flags = re.DOTALL
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse4(self):
        pattern = r'\n\n(.*)$'
        flags = re.DOTALL
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse5(self):
        pattern = r'\n\n(.*)$'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse6(self):
        pattern = r'Yes|No'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse7(self):
        pattern = r'Yes|No'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse8(self):
        pattern = r'Yes|No'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse9(self):
        pattern = r'Yes|No'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]

    def parse10(self):
        pattern = r'\n\n(.*)$'
        flags = 0
        matches = re.findall(pattern, self.text, flags=flags)
        if len(matches) > 0:
            return matches[0]




