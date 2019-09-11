import io
import sys
import os
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it('Print "Hello, --Your Name--"')
def test_desired_output(capsys):
    app.hello_name("David")
    captured = capsys.readouterr()

    assert captured.out == "Hello, David" + "\n"


