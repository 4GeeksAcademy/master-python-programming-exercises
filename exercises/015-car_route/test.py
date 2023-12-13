import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You need to import the math module")
def test_import_random():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import(\s)+math")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function car_route must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.car_route)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.car_route(659, 1857) != None

@pytest.mark.it('The function must return a number')
def test_function_return_type(capsys, app):
    assert type(app.car_route(659, 1857)) == type(1)

@pytest.mark.it('We tried to pass 20 and 40 as parameter and it did not return 2')
def test_for_file_output(capsys, app):
    assert app.car_route(20, 40) == 2

@pytest.mark.it('We tried to pass 20 and 900 as parameter and it did not return 45')
def test_for_file_output2(capsys, app):
    assert app.car_route(20, 900) == 45






