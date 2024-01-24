import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function lines must exist')
def test_function_existence(capsys, app):
    assert app.lines

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.lines("hello world") == "HELLO WORLD"

@pytest.mark.it('The function should return the expected output. Testing with a different value')
def test_another_output(capsys, app):
    assert app.lines("LeT the WOrld know YoU") == "LET THE WORLD KNOW YOU"
