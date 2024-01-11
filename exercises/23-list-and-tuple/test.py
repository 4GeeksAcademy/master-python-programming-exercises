import pytest

@pytest.mark.it('You should create a function named "list_and_tuple"')
def test_variable_exists(app):
  try:
    assert app.list_and_tuple
  except AttributeError:
    raise AttributeError('The function "list_and_tuple" should exists')

@pytest.mark.it('The function "list_and_tuple" should return two elements')
def test_function_return_two_elements(app):
  try:
    value = app.list_and_tuple()
    assert isinstance(value, tuple)
    assert len(value) == 2
  except AttributeError:
    raise AttributeError('The function "list_and_tuple" should exists')

@pytest.mark.it('The function "list_and_tuple" should return a list first')
def test_function_return_a_list(app):
  try:
    value = app.list_and_tuple()
    assert isinstance(value, tuple)
    assert isinstance(value[0], list)
  except AttributeError:
    raise AttributeError('The function "list_and_tuple" should exists')
  
@pytest.mark.it('The function "list_and_tuple" should return a tuple second')
def test_function_return_a_tuple(app):
  try:
    value = app.list_and_tuple()
    assert isinstance(value, tuple)
    assert isinstance(value[1], tuple)
  except AttributeError:
    raise AttributeError('The function "list_and_tuple" should exists')
  
@pytest.mark.it('The function "list_and_tuple" should return a list and tuple with the expected values')
def test_function_return_the_expected_values(app):
  try:
    value = app.list_and_tuple(1,2,3,4,5,6)
    assert value[0]==['1', '2', '3', '4', '5', '6']
    assert value[1]==('1', '2', '3', '4', '5', '6')
  except AttributeError:
    raise AttributeError('The function "list_and_tuple" should exists')

@pytest.mark.it('The function "list_and_tuple" should return a list and tuple with the expected values')
def test_function_return_the_expected_values(app):
  try:
    value = app.list_and_tuple(7,8,9,10,11,12)
    assert value[0]==['7', '8', '9', '10', '11', '12']
    assert value[1]==('7', '8', '9', '10', '11', '12')
  except AttributeError:
    raise AttributeError('The function "list_and_tuple" should exists')
