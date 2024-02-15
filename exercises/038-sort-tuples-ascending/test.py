import pytest, io, sys, json, mock, re, os

path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The function sort_tuples_ascending must exist')
def test_function_existence(capsys, app):
    assert app.sort_tuples_ascending

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.sort_tuples_ascending([
        'Tom,19,80',
        'John,20,90',
        'Jony,17,91',
        'Jony,17,93',
        'Jason,21,85'
    ]) == [('Jason', '21', '85'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Tom', '19', '80')]

@pytest.mark.it('The solution should work with other entries')
def test_another_entry(capsys, app):
    assert app.sort_tuples_ascending([
        'Martin,23,30',
        'Tomas,25,27'
    ]) == [('Martin', '23', '30'), ('Tomas', '25', '27')]
