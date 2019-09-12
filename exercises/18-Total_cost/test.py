import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest



@pytest.mark.it('Function total_cost is defined')
def test_for_dollars_and_cents(capsys):
    assert app.total_cost is not None

@pytest.mark.it('Print total cost (in dollar and cents) of N cupcakes.')
def test_for_variables(capsys):
    app.total_cost(45,50,5)
    captured = capsys.readouterr()
    assert captured.out == str(227) + " " + str(50) + "\n"