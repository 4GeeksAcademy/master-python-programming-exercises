import io, sys, pytest, mock

@pytest.mark.it('Your code needs to print Hello World on the console')
def test_for_file_output(capsys):
    import app
    captured = capsys.readouterr()
    assert "Hello World\n" == captured.out
