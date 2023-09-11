import re
from backend.src.parser_generic import MedicalDocParser


class VrParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'name': self.get_name(),
            'dob': self.get_dob(),
            'dosage_dates': self.get_dates(),
            'gender': self.get_gender(),
            'age': self.get_age(),
            'dosage_number': self.get_number()
        }

    def get_name(self):
        pattern = r'Name(.*?)Date'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_dob(self):
        pattern = r'Birth(.*?)Vaccination'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_gender(self):
        pattern = r'ID(.*?)\d'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_age(self):
        pattern = r'Batch No,(.*?)\d{3}'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches[0].strip()

    def get_number(self):
        pattern = r'(\d{1}) \d{4}'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            return matches

    def get_dates(self):
        pattern1 = r'1st|ist Dose (.*?)2nd'
        pattern2 = r'2nd Dose (.*?)3rd'
        pattern3 = r'3rd Dose (.*?)Age'
        dates = []
        matches1 = re.findall(pattern1, self.text, flags=re.DOTALL)
        matches2 = re.findall(pattern2, self.text, flags=re.DOTALL)
        matches3 = re.findall(pattern3, self.text, flags=re.DOTALL)
        try:
            dates.append(matches1[0].strip())
            dates.append(matches2[0].strip())
            dates.append(matches3[0].strip())
        except Exception as e:
            return dates


