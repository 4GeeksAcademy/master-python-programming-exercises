import io, sys, os, pytest, json, mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
@pytest.mark.it('The function area_of_triangle should exist')
def test_function_exists(capsys):
  
  try:
    import app
    app.area_of_triangle
  except AttributeError:
      raise AttributeError("The function 'area_of_triangle' should exist on app.py")

@pytest.mark.it('Calculate the area of the triangle.')
def test_area_of_triangle(stdin):

  _stdin = json.loads(stdin)
  with mock.patch('builtins.input', lambda x: _stdin.pop(0)):

    sys.stdout = buffer = io.StringIO()
    import app
    _stdin = json.loads(stdin)
    result = int(_stdin[0]) * int(_stdin[1]) / 2
    assert buffer.getvalue() == str(result) + "\n"


