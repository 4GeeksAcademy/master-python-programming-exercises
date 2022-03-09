import pytest,os,re,io,sys, mock, json

@pytest.mark.it('The function generate_dict should exist')
def test_function_existence(capsys, app):
    assert app.generate_dict

@pytest.mark.it('The function should return a dictionary')
def test_typeof_return(capsys, app):
    assert type(app.generate_dict(7)) == type({})

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.generate_dict(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

@pytest.mark.it('The function should work with other entries')
def test_another_entry_5(capsys, app):
    assert app.generate_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


