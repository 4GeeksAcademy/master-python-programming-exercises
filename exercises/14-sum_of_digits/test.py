import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num" and "total"')
def test_for_variable(capsys):

    captured = buffer.getvalue()

    assert app.num is not None
    assert type(app.num) is int
