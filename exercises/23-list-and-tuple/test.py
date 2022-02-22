import io, sys, os, pytest, json, mock
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


# @pytest.mark.it('The output should be the expected for this solution')
# def test_output(capsys, app):
#     fake_input = ["34,67,55,33,12,98"] #fake input
#     with mock.patch('builtins.input', lambda x: fake_input.pop()):
#         app()
#         captured = capsys.readouterr()
#         assert captured.out != "('34', '67', '55', '33', '12', '98\r')\n"



@pytest.mark.it('The solution should work with other inputs')
def test_other_output(stdin):
    import app
    _stdin = json.loads(stdin)
    with mock.patch('builtins.input', lambda x: _stdin.pop(0)):
        sys.stdout = buffer = io.StringIO()
        
        _stdin = json.loads(stdin)
        result = tuple(_stdin[0].split(','))
        assert buffer.getvalue() == str(result) + "\n"