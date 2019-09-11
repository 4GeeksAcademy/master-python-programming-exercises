import io
import sys
import os
import re
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Print next number')
def test_for_next_number(capsys):
    app.previous_next(4)
    captured = capsys.readouterr()

    assert "The next number for the number 4 is 5" in captured.out



@pytest.mark.it('Print previous number')
def test_for_previous_number(capsys):
    app.previous_next(4)
    captured = capsys.readouterr()

    assert "The previous number for the number 4 is 3" in captured.out






