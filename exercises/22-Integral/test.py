import io, os, mock, pytest, sys

@pytest.mark.it('The solution sould work with other inputs')
def test_output(capsys, app):
    fake_input = ['5']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n"


@pytest.mark.it('The solution sould as showed in the instructions')
def test_output(capsys, app):
    fake_input = ['8']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n"

