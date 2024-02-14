import pytest, io, sys, json, mock, re, os

@pytest.mark.it('The function remove_duplicate_words must exist')
def test_function_existence(capsys, app):
    app.remove_duplicate_words

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.remove_duplicate_words("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"

@pytest.mark.it('The function should work with other entries. Testing with different values')
def test_expected_output_2(capsys, app):
    assert app.remove_duplicate_words("lets try this again with another try") == "again another lets this try with"

@pytest.mark.it('The function should work with other entries. Testing with different values')
def test_expected_output_3(capsys, app):
    assert app.remove_duplicate_words("Jacke was Named Jacke by his mother") == "Jacke Named by his mother was"

