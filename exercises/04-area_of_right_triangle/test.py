import io, sys, os, pytest, json

@pytest.mark.it('Calculate the area of the triangle')
def test_area_of_triangle(mocker, stdin):

    _stdin = json.loads(stdin)
    mocker.patch('builtins.input', lambda x: _stdin.pop(0))

    import app

    result = app.area_of_triangle(3,3)
    assert result == 4.5



