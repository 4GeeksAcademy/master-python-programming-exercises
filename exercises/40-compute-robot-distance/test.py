import pytest, io, sys, json, mock, re, os


@pytest.mark.it('The function compute_robot_distance must exist')
def test_function_existence(capsys, app):
    assert app.compute_robot_distance


@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.compute_robot_distance("UP 5 DOWN 3 LEFT 3 RIGHT 2") ==  2

@pytest.mark.it('The solution should work with other entries')
def test_another_output(capsys, app):
    assert app.compute_robot_distance("DOWN 20 UP 5 LEFT 5 RIGHT 2") ==  15

@pytest.mark.it('The solution should work with other entries')
def test_negative_inputs(capsys, app):
    assert app.compute_robot_distance("DOWN -1 UP -5 LEFT 50 RIGHT 20") ==  30
