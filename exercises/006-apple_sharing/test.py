import io, sys, pytest, os, re, mock

@pytest.mark.it('The function apple_sharing must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.apple_sharing)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.apple_sharing(10, 54) != None

@pytest.mark.it('The function must return a tuple')
def test_function_return_type(capsys, app):
    result = app.apple_sharing(10, 54)
    assert  type(result) == type((1,2))
    
@pytest.mark.it('The function apple_sharing must return the correct output')
def test_for_file_output(capsys, app):
    assert app.apple_sharing(10, 54) == (54//10, 54%10)


