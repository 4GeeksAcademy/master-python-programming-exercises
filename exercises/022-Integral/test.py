import pytest,os,re,io,sys, mock, json

@pytest.mark.it('The function squares_dictionary should exist')
def test_function_existence(capsys, app):
    assert app.squares_dictionary

@pytest.mark.it('The function should return a dictionary')
def test_typeof_return(capsys, app):
    assert type(app.squares_dictionary(7)) == type({})

@pytest.mark.it('The function should return the expected output. Testing with 8')
def test_expected_output(capsys, app):
    assert app.squares_dictionary(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

@pytest.mark.it('The function should return the expected output. Testing with 5')
def test_another_entry_5(capsys, app):
    assert app.squares_dictionary(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

