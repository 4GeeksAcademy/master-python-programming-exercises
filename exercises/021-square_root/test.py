import io, sys, os, re, pytest
import app

@pytest.mark.it('You should create a function named square_root')
def test_square_root_exists(app):
    try:
        from app import square_root
        assert square_root 
    except AttributeError:
        raise AttributeError("The function 'square_root' should exist on app.py")

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.square_root(25) != None

@pytest.mark.it('The function must return a float number')
def test_function_return_type(capsys, app):
    assert type(app.square_root(25)) == type(1.0)

@pytest.mark.it('Testing the function square_root with the number 50, it should return 7.07')
def test_square_root_50(app):
    try:
        assert app.square_root(50) == 7.07
    except AttributeError:
        raise AttributeError("The function 'square_root' should return the value 7.07")

@pytest.mark.it('Testing the function square_root with the number 2.25, it should return 1.5')
def test_square_root_2_25(app):
    try:
        assert app.square_root(2.25) == 1.5
    except AttributeError:
        raise AttributeError("The function 'square_root' should return the value 1.5")

@pytest.mark.it('Testing the function square_root with the number 0, it should return 0')
def test_square_root_0(app):
    try:
        assert app.square_root(0) == 0
    except AttributeError:
        raise AttributeError("The function 'square_root' should return the value 0")