import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You need to import the math module")
def test_import_random():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import(\s)+math")
        assert bool(regex.search(content)) == True


@pytest.mark.it('The function century must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.century)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.century(19001) != None

@pytest.mark.it('The function must return a number')
def test_function_return_type(capsys, app):
    assert type(app.century(19001)) == type(1)

@pytest.mark.it('We tried to pass 2000 as parameter and it did not return 20')
def test_for_file_output(capsys, app):
  assert app.century(2000) == 20

@pytest.mark.it('We tried to pass 2001 as parameter and it did not return 21')
def test_for_file_output2(capsys, app):
  assert app.century(2001) == 21

@pytest.mark.it('We tried to pass 2101 as parameter and it did not return 22')
def test_for_file_output3(capsys, app):
  assert app.century(2101) == 22

