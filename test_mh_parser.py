import pytest
from backend.src.parser_mh import MhParser


@pytest.fixture()
def doc_lalli1():
    document_text = 'Full Name Phone Number What is your Gender?\nLali Farah (91) 725-5945333 Male'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli2():
    document_text = 'Check the conditions that apply to you or to any members of your immediate relatives:\n\nHypertension'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli3():
    document_text = 'Check the symptoms that youre currently experiencing:\n\nPsychiatric'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli4():
    document_text = '‘Ave you currently taking any medication?\n\nNo'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli5():
    document_text = 'Do you have any medication allergies?\nNo'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli6():
    document_text = 'Do you use or do you hava history of using tobacco?\n\nYes'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli7():
    document_text ='Do youuse or do you have history of using illegal drugs?\n\nNo'

    return MhParser(document_text)


@pytest.fixture()
def doc_lalli8():
    document_text = 'How often de you consume alcohol?\n\nOccasionally'

    return MhParser(document_text)


def test_parse(doc_lalli1):
    assert doc_lalli1.parse() == 'Lali Farah'


def test_parse2(doc_lalli1):
    assert doc_lalli1.parse2() == '(91) 725-5945333'


def test_parse3(doc_lalli1):
    assert doc_lalli1.parse3() == 'Male'


def test_parse4(doc_lalli2):
    assert doc_lalli2.parse4() == 'Hypertension'


def test_parse5(doc_lalli3):
    assert doc_lalli3.parse5() == 'Psychiatric'


def test_parse6(doc_lalli4):
    assert doc_lalli4.parse6() == 'No'


def test_parse7(doc_lalli5):
    assert doc_lalli5.parse7() == 'No'


def test_parse8(doc_lalli6):
    assert doc_lalli6.parse8() == 'Yes'


def test_parse9(doc_lalli7):
    assert doc_lalli7.parse9() == 'No'


def test_parse10(doc_lalli8):
    assert doc_lalli8.parse10() == 'Occasionally'

