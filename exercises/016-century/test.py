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

@pytest.mark.it('We tried to pass 1801 as parameter and it did not return 19!')
def test_for_file_output(capsys, app):
  if app.century(1801) % 100 == 0:
    assert app.century(1801) == math.floor(1801/100) 
  else:
    assert app.century(1801) == math.floor(1801/100 +1)

