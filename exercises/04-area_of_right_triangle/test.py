import io
import sys
import os
sys.stdout = buffer = io.StringIO()


import app
import pytest


@pytest.mark.it('Print the area of the triangle')
def test_area_of_triangle(capsys):

    app.area_of_triangle(3,3)
    captured = capsys.readouterr()
    print(captured.out)

    if captured.out == str(4.5) + "\n":
        assert True
    else:
        assert False



