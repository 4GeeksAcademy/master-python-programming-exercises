import pytest, io, sys, json, mock, re, os

@pytest.mark.it('The function divisible_binary must exist')
def test_function_existence(capsys, app):
    assert app.divisible_binary

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.divisible_binary("0100,0011,1010,1001") == "1010"

@pytest.mark.it('The function should work with other parameters. testing with 1111,1000,0101,0000')
def test_expected_output_2(capsys, app):
    assert app.divisible_binary("1111,1000,0101,0000") == "1111,0101,0000"

@pytest.mark.it("The function should work with other parameters. Testing with 1000")
def test_expected_output_3(capsys, app):
    assert app.divisible_binary("1000,1000,1000,1000") == ""
