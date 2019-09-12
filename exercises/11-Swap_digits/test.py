import io
import sys
sys.stdout = buffer = io.StringIO()
import app
import pytest



@pytest.mark.it('swap_digits function is defined')
def test_for_swap_digits_function(capsys):
    assert app.swap_digits is not None



@pytest.mark.it('Check for swapped digits')
def test_for_swapped_digits(capsys):
    app.swap_digits(46)
    captured = capsys.readouterr()

    assert captured.out == str(64) + "\n"



