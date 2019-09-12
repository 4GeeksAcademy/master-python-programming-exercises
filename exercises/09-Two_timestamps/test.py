import io
import sys
sys.stdout = buffer = io.StringIO()
import app
import pytest

@pytest.mark.it('two_timestamp function is defined')
def test_function(capsys):
    assert app.two_timestamp is not None



@pytest.mark.it('Function prints how many seconds passed between each timestamp')
def test_seconds(capsys):
    app.two_timestamp(6,6,6,9,9,9)
    captured = capsys.readouterr()


    assert captured.out == "10983" + "\n"



@pytest.mark.it('Output cannot be a negative number')
def test_negative_number(capsys):
    captured2 = buffer.getvalue()

    if "-" in captured2:
        assert False
    else:
        assert True














