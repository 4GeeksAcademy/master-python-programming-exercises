import io, sys, pytest, os, re, mock

@pytest.mark.it('The function hello_name must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.hello_name)

@pytest.mark.it('The function hello_name must accept 1 parameter and return the correct output')
def test_for_file_output(capsys, app):
    assert app.hello_name('a') == "Hello, a!"