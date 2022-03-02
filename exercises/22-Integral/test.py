import pytest,os,re,io,sys, mock, json, unittest
from unittest.mock import patch


# @pytest.mark.it('The solution should work with other entries')
# def test_expected_output_5(stdin):

#     _stdin = ['5']
#     with mock.patch('builtins.input', lambda x: _stdin.pop(0)):

#         sys.stdout = buffer = io.StringIO()
#         import app
#         # _stdin = json.loads(stdin)
#         result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#         assert buffer.getvalue() == str(result) + "\n"

@pytest.mark.it('The solution should return the expected output')
def test_expected_output_8(stdin):

    _stdin = ['8']
    with mock.patch('builtins.input', lambda x: _stdin.pop(0)):

        sys.stdout = buffer = io.StringIO()
        import app
        # _stdin = json.loads(stdin)
        result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
        assert buffer.getvalue() == str(result) + "\n"