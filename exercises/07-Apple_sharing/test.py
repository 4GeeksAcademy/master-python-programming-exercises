import io
import sys
sys.stdout = buffer = io.StringIO()
import app
import math
import pytest

@pytest.mark.it('Print how many apples each student will get')
def test_for_apples_for_student(capsys):
    app.apple_sharing(23,256)
    captured = capsys.readouterr()

    test1 = captured.out.split("\n")
    if test1[0] == "11"

@pytest.mark.it('Print how many apples will remain in the basket')
def test_for_remaining_apples(capsys):
    app.apple_sharing(23,256)
    captured = capsys.readouterr()

    assert "3" in captured.out
