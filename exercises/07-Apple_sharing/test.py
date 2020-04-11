import io, sys, pytest, os, re, mock

@pytest.mark.it('The function apple_sharing must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.apple_sharing)

@pytest.mark.it('The function apple_sharing must return the correct output')
def test_for_file_output(capsys, app):
    assert app.apple_sharing(10, 54) == (54//10, 54%10)


