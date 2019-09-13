import pytest, io, sys, json



@pytest.mark.it('Sum all three input numbers and print on the console the result')
def test_add_variables(mocker, stdin):

    _stdin = json.loads(stdin)
    mocker.patch('builtins.input', lambda x: _stdin.pop(0))

    sys.stdout = buffer = io.StringIO()
    import app

    _stdin = json.loads(stdin)
    sumatory = int(_stdin[0]) + int(_stdin[1]) + int(_stdin[2])

    assert buffer.getvalue() == str(sumatory)+"\n"


