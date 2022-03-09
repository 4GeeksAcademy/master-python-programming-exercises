import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function print_formula must exist')
def test_function_existence(capsys, app):
    assert app.print_formula

@pytest.mark.it('The solution should work as expected')
def test_expected_output(capsys, app):
    assert app.print_formula(100,150,180) == "18,22,24"

@pytest.mark.it('The solution should work as expected')
def test_another_output(capsys, app):
    assert app.print_formula(200,90,300) == "26,17,32"

