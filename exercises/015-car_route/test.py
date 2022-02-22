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

@pytest.mark.it('We tried to pass 659 and 1857 as parameter and it did not return 3!')
def test_for_file_output(capsys, app):
    assert app.car_route(659, 1857) == math.ceil(1857 / 659)






