import pytest
import os
import re
import io
import sys
import mock

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('Use the function print()')
def test_for_file_output(capsys):
    with open(path, 'r') as content_file:
        content = content_file.read()
        pattern = (r"print\s*\(")
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == True


@pytest.mark.it("String input should be uppercase")
@mock.patch('builtins.input', lambda x: 'hello')
def test_plus_ten(stdin):
    sys.stdout = buffer = io.StringIO()
    import app
    captured = buffer.getvalue()
    assert "HELLO\n" in captured
