import io, os, mock, pytest, sys, unittest
from unittest.mock import patch

# class TestListSum(unittest.TestCase):

#     string_of_ints = '5'
#     @pytest.mark.it('The solution should work with other entries')
#     @patch('builtins.input', return_value=string_of_ints)
#     def test_sum_string_of_ints(self, mock_inputs):
#         result = test()
#         self.assertEqual(result, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})


@pytest.mark.it('The solution should return the expected output')
def test_convert_inputs(capsys):

    fake_input = ["8"] #fake input
    import app
    app()
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        
        captured = capsys.readouterr()
        assert captured.out == "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n"

@pytest.mark.it('The solution should work with other entries')
def test_convert_inputs_2(capsys):
    import app
    app()
    fake_input = ["5"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        
        captured = capsys.readouterr()
        assert captured.out == "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n"
