import pytest, mock, app, io, sys, os 

@pytest.mark.it('The solution must return the expected value for an input like "3,5"')
def test_for_output_3_5(capsys):
    fake_input = ["3,5"]
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]\n"

        

@pytest.mark.it('Your solution should work with others input values, testing with: 2,7')
def test_for_output_2_7(capsys):
    fake_input = ["2,7"]
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6]]\n"

@pytest.mark.it('The input must be two numbers separate by comma, like this: 7,8')
def test_input(capsys):
    fake_input = ["2,7"]
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "[[0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6]]\n"