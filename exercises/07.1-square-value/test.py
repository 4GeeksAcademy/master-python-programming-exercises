import io, sys, pytest, os, re, mock

@pytest.mark.it('The function square must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.square)

@pytest.mark.it('The we tried 6 and it should return 36')
def test_for_file_output(capsys, app):
    assert app.square(6) == 6*6

@pytest.mark.it('The we tried 47 and it should return 2209')
def test_for_file_output(capsys, app):
    assert app.square(47) == 47*47

@pytest.mark.it("Use the ** operator")
def test_operator():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\*\*")
        assert bool(regex.search(content)) == True


