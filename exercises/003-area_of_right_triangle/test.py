import io, sys, os, pytest, json, mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function area_of_triangle should exist')
def test_function_exists(capsys, app):
  try:
    app.area_of_triangle
  except AttributeError:
      raise AttributeError("The function 'area_of_triangle' should exist on app.py")

@pytest.mark.it('The function must return something')
def test_function_returns(capsys, app):
  result = app.area_of_triangle(1, 2)
  assert result != None
  
@pytest.mark.it('The function must return a number')
def test_function_return_type(capsys, app):
  result = app.area_of_triangle(1,2)
  assert type(result) == type(1*2/2)
  
@pytest.mark.it('The solution should return the expected output. Testing with 3 and 5')
def test_convert_inputs(capsys, app):
  result = app.area_of_triangle(3, 5)
  assert result == 7.5

