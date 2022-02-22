import io, os, mock, pytest, capsys, app, sys

@pytest.mark.it('The output should be the expected for this solution')
def test_output():
    fake_input = ["34,67,55,33,12,98"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "('34', '67', '55', '33', '12', '98\r')\n"


@pytest.mark.it('The solution should work with other inputs')
def test_output():
    fake_input = ["11,06,14,1"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "('11', '06', '14', '1\r')\n"