import io, sys, os, re, pytest
import app

@pytest.mark.it('You should create a function named factorial')
def test_factorial_exists(app):
    try:
        from app import factorial
        assert factorial 
    except AttributeError:
        raise AttributeError("The function 'factorial' should exist on app.py")

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.factorial(8) != None

@pytest.mark.it('The function must return a number')
def test_function_return_type(capsys, app):
    assert type(app.factorial(8)) == type(1)

@pytest.mark.it('Testing the function factorial with the number 8, it should return 40320')
def test_factorial_8(app):
    try:
        assert app.factorial(8) == 40320
    except AttributeError:
        raise AttributeError("The function 'factorial' should return the value 40320")

@pytest.mark.it('Testing the function factorial with the number 3, it should return 6')
def test_factorial_3(app):
    try:
        assert app.factorial(3) == 6
    except AttributeError:
        raise AttributeError("The function 'factorial' should return the value 6")

@pytest.mark.it('Testing the function factorial with the number 1, it should return 1')
def test_factorial_1(app):
    try:
        assert app.factorial(1) == 1
    except AttributeError:
        raise AttributeError("The function 'factorial' should return the value 1")

