import io, sys, pytest, mock

@pytest.mark.it('Your code needs to print Hello World on the console')
def test_for_file_output():
    sys.stdout = buffer = io.StringIO()
    import app
    assert buffer.getvalue() == "Hello World\n" #add \n because the console jumps the line on every print
