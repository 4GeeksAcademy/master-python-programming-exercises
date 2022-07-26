import io, sys, pytest, os, re, mock

@pytest.mark.it('The function digits_sum must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.digits_sum)

@pytest.mark.it('We tried to pass 854 as parameter and it did not return 17!')
def test_for_file_output(capsys, app):
    assert app.digits_sum(854) == (854 //100)+(854 // 10)%10+ 854%10






