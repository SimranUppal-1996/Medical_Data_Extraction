from backend.src.parser_prescription import PrescriptionParser
import pytest


@pytest.fixture()
def doc_2_virat():
    document_text = '''
Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

Omeprazole 40 mg

Directions: Use two tablets daily for three months
Refill: 3 times
'''
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')


def test_get_name(doc_2_virat, doc_3_empty):
    assert doc_2_virat.get_field('patient_name') == 'Virat Kohli'
    assert doc_3_empty.get_field('patient_name') is None


def test_get_address(doc_2_virat, doc_3_empty):
    assert doc_2_virat.get_field('patient_address') == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_field('patient_address') is None


def test_get_medicines(doc_2_virat, doc_3_empty):
    assert doc_2_virat.get_field('medicines') == 'Omeprazole 40 mg'
    assert doc_3_empty.get_field('medicines') is None


def test_get_directions(doc_2_virat, doc_3_empty):
    assert doc_2_virat.get_field('directions') == 'Use two tablets daily for three months'
    assert doc_3_empty.get_field('directions') is None


def test_parse(doc_2_virat, doc_3_empty):
    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicines': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refills': '3'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refills': None
    }



