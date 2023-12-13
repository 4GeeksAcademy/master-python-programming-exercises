import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function sequence_of_words must exist')
def test_function_existence(capsys, app):
    assert app.sequence_of_words

@pytest.mark.it('The function should return the expected output')
def test_function_existence(capsys, app):
    assert app.sequence_of_words("bag,hello,without,world") == "bag,hello,without,world"

@pytest.mark.it('The function should return the expected output. Testing with different values')
def test_function_existence(capsys, app):
    assert app.sequence_of_words("No,pain,gain") == "No,gain,pain"
