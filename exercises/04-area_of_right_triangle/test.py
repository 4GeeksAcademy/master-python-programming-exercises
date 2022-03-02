import io, sys, os, pytest, json, mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function area_of_triangle should exist')
def test_function_exists(capsys):
  try:
    import app
    app.area_of_triangle
  except AttributeError:
      raise AttributeError("The function 'area_of_triangle' should exist on app.py")

@pytest.mark.it('The solution should return the expected output')
def test_convert_inputs(capsys, app):
  app.area_of_triangle(3,5)
  captured = capsys.readouterr()
  assert "7.5\n" == captured.out
  # from app import area_of_triangle
  # result = area_of_triangle(3,5)
  # assert result == "7.5\n"


