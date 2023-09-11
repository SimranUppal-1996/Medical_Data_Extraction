import pytest

from backend.src.parser_patient_details import PatientDetailsParser


@pytest.fixture()
def doc_1_kathy():
    document_text = '''
    Patient Medical Record . : :

    Patient Information


    Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight:
    9264 Ash Dr 95
    New York City, 10005 a
    United States Height:
    190
    In Case of Emergency
    ee oe
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    I i
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?

    No

    List any Medical Problems (asthma, seizures, headaches):

    Migraine
    '''

    return PatientDetailsParser(document_text)


def test_get_patient_name(doc_1_kathy):
    assert doc_1_kathy.get_patient_name() == 'Kathy Crawford'


def test_get_patient_phone_number(doc_1_kathy):
    assert doc_1_kathy.get_patient_phone_number() == '(737) 988-0851'


def test_get_hepatitis_b_vaccination(doc_1_kathy):
    assert doc_1_kathy.get_hepatitis_b_vaccination() == 'No'


def test_get_medical_problems(doc_1_kathy):
    assert doc_1_kathy.get_medical_problems() == 'Migraine'


def test_parse(doc_1_kathy):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['phone_number'] == '(737) 988-0851'
    assert record_kathy['medical_problems'] == 'Migraine'
    assert record_kathy['hepatitis_b_vaccination'] == 'No'
