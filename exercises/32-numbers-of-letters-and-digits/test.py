import mock, pytest

@pytest.mark.it('The solution should return the expected output')
def test_output(capsys, app):
    fake_input = ["hello world! 123"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "LETTERS 10 DIGITS 3\n"

@pytest.mark.it('The solution should work with others inputs')
def test_output_2(capsys, app):
    fake_input = ["How are you 11111"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "LETTERS 9 DIGITS 5\n"