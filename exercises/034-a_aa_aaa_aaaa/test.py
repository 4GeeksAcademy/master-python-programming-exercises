import io, sys, pytest, os, re, mock

@pytest.mark.it('The function computed_value must exist')
def test_function_existence(capsys, app):
    assert app.computed_value

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.computed_value(9) == 11106

@pytest.mark.it('The function should work with other inputs. Testing with 123')
def test_another_output(capsys, app):
    assert app.computed_value(123) == 123246369492

@pytest.mark.it('The function should work with other inputs. Testing with 0')
def test_with_zero(capsys, app):
    assert app.computed_value(0) == 0
