import mock, pytest, io, sys 


@pytest.mark.it('The function letters_and_digits must exist')
def test_function_existence(capsys, app):
    assert app.letters_and_digits

@pytest.mark.it('The function should return the expected output')
def test_output(capsys, app):
    app.letters_and_digits("hello world! 123") == "LETTERS 10 DIGITS 3"

@pytest.mark.it('The solution should work with other parameters')
def test_another_entry(capsys, app):
    assert app.letters_and_digits("My name is C200 and i live in apartment 3H") == "LETTERS 29 DIGITS 4"
