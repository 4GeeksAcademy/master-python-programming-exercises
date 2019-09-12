import io
import sys

sys.stdout = buffer = io.StringIO()

import pytest
import app



@pytest.mark.it('Add all three numbers')
def test_add_variables(capsys):
    app.sum_of_three(1,1,2)
    captured = capsys.readouterr()
    print(captured.out)

    if captured.out == str(4) + "\n":
        assert True
    else:
        assert False


