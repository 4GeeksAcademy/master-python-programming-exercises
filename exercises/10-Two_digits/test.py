import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function two_digits is defined')
def test_for_function(capsys):
    assert app.two_digits is not None

@pytest.mark.it("Print the left & right digit of any two digits number")
def test_for_left_and_right_digit(capsys):
    app.two_digits(80)
    captured = capsys.readouterr()
    print(captured)

    assert captured.out == "8 " + "0" + "\n"

@pytest.mark.it('Interger must be between 10 and 99')
def test_for_two_digits(capsys):
    app.two_digits(23)
    captured = buffer.getvalue()
    aa = captured.split(" ")
    #print("test:",aa[0][1])

    if int(aa[0]) > 9:
        assert False
    else:
        assert True



