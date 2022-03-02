import pytest, io, sys, json, mock, re, os

@pytest.mark.it('Your solution should work as expected')
def test_expected_output(capsys, app):
    fake_input=['Hola como Hola']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "Hola como\n"

@pytest.mark.it('Your solution should work as expected')
def test_expected_output_2(capsys, app):
    fake_input=['ayer como ayer es hoy']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "ayer como es hoy\n"


@pytest.mark.it('Your solution should work as expected')
def test_expected_output_no_repetead(capsys, app):
    fake_input=['Hola como estas']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "Hola como estas\n"