import pytest
from backend.src.parser_vr import VrParser


@pytest.fixture()
def doc_jot():
    document_text = '''
    Name
    jot Kaur

    Date of Birth
    March 21, 2000

    Vaccination Record

    Date
    ist Dose 12-03-2021
    2nd Dose 24-04-2022

    3rd Dose

    Age Batch No,
    23 400
    Gender Patient ID
    Female 101
    Dosage Lot Number Manufacturer Location/site
    2 3000 abe Jalandhar
    1 4000 xyz Ludhiana

    Please keep this record card, it includes the medical information, details and the vaccine you have received. This
    card will show the next schedule of your vaccine. It is important to show this card to the next vaccination schedule

    for health officials to verify.

    Greate your own automated PDFs with Jotform PDF Editor- It's free

    % Jotform

    nm
    arr WUT ST ELE
    '''
    return VrParser(document_text)


def test_get_name(doc_jot):
    assert doc_jot.get_name() == 'jot Kaur'


def test_get_dob(doc_jot):
    assert doc_jot.get_dob() == 'March 21, 2000'


def test_get_dosage_dates(doc_jot):
    assert doc_jot.get_dates() == ['12-03-2021', '24-04-2022']


def test_get_gender(doc_jot):
    assert doc_jot.get_gender() == 'Female'


def test_get_age(doc_jot):
    assert doc_jot.get_age() == '23'


def test_get_dosage_number(doc_jot):
    assert doc_jot.get_number() == ['2', '1']


def test_parse(doc_jot):
    record = doc_jot.parse()
    assert record['name'] == 'jot Kaur'
    assert record['dob'] == 'March 21, 2000'
    assert record['dosage_dates'] == ['12-03-2021', '24-04-2022']
    assert record['gender'] == 'Female'
    assert record['age'] == '23'
    assert record['dosage_number'] == ['2', '1']
