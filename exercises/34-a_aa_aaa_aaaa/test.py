import io, sys, pytest, os, re, mock

@pytest.mark.it('The solution should return the expected output')
def test_convert_inputs(capsys, app):

    fake_input = ["9"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "11106\n"
