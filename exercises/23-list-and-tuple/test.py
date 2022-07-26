import io, sys, os, pytest, json, mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The output should be the expected for this solution')
def test_output(capsys, app):
    fake_input = ["34,67,55,33,12,98"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "['34', '67', '55', '33', '12', '98']\n" or "('34', '67', '55', '33', '12', '98')\n"

@pytest.mark.it('The solution should work with other parameters')
def test_output_2(capsys, app):
    fake_input = ["11,56,23,12,02"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "['11', '56', '23', '12', '02']\n" or "('11', '56', '23', '12', '02')\n"

