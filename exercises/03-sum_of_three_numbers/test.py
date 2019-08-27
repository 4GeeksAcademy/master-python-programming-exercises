import io
import sys
sys.stdout = buffer = io.StringIO()

import pytest
import app

@pytest.mark.it('Create 3 variables each with numbers as value')
def test_for_variables(capsys):

    captured = buffer.getvalue()
    print(captured)

    assert captured == "hello\n" #add \n because the console jumps the line on every print



