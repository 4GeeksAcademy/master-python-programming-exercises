import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function net_amount must exist')
def test_function_existence(capsys, app):
    assert app.net_amount
    
@pytest.mark.it('The solution should return the expected output')
def test_output(capsys, app):
    assert app.net_amount("D 300 D 300 W 200 D 100") == 500

@pytest.mark.it('The solution should work with other parameters. Testing with "W 300 D 300 W 200 D 300"')
def test_output_2(capsys, app):
    assert app.net_amount("W 300 D 300 W 200 D 300") == 100

@pytest.mark.it('The solution should work with other parameters. Testing with "W 300 D 300 W 200 D 300"')
def test_output_negative(capsys, app):
    assert app.net_amount("W 300 D 300 W 200 W 300") == -500
