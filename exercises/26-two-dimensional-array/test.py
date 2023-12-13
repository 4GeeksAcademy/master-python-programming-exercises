import pytest,os,re,io,sys, mock, json

@pytest.mark.it('The function two_dimensional_list must exist')
def test_function_existence(capsys, app):
    assert app.two_dimensional_list

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.two_dimensional_list(3,5) == [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

@pytest.mark.it('The function should work with other entries. Testing with (2, 7)')
def test_expected_output(capsys, app):
    assert app.two_dimensional_list(2,7) == [[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6]]
        
@pytest.mark.it('The function should work with other entries. Testing with (1, 10)')
def test_expected_output(capsys, app):
    assert app.two_dimensional_list(1,10) == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
