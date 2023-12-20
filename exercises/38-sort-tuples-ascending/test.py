import pytest, io, sys, json, mock, re, os

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function sort_tuples_ascending must exist')
def test_function_existence(capsys, app):
    assert app.sort_tuples_ascending


@pytest.mark.it('The function should return the expected output')
def etest_expected_output(capsys, app):
    app.sort_tuples_ascending("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85") == [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

@pytest.mark.it('The solution should work with other entries')
def test_another_entry(capsys, app):
    app.sort_tuples_ascending("Martin,23,30 Tomas,25,27") == [('Martin', '23', '30'), ('Tomas', '25', '27')]
