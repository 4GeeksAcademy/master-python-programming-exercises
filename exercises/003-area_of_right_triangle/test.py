import io, sys, os, pytest, json, mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function area_of_triangle should exist')
def test_function_exists(capsys):
  try:
    import app
    app.area_of_triangle
  except AttributeError:
      raise AttributeError("The function 'area_of_triangle' should exist on app.py")

@pytest.mark.it('The solution should return the expected output. Testing with 3 and 5')
def test_convert_inputs(capsys, app):
  result = app.area_of_triangle(3, 5)
  assert result == 7.5

@pytest.mark.it('The solution should return the expected output. Testing with 4 and 6')
def test_convert_inputs(capsys, app):
  result = app.area_of_triangle(4, 6)
  assert result == 12
