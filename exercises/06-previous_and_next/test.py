import io
import sys
import os
import re
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable named number with any int as its value')
def test_for_variable(capsys):

    assert app.num is not None
    assert type(app.num) is int


@pytest.mark.it('Print previous number')
def test_for_previous_number(capsys):

    captured = buffer.getvalue()
    print(captured)
    n = app.num
    a = "The previous number for the number " + str(n) + " is " + str(n - 1)
    assert str(a) + "\n" in captured


    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    print(content)
    ab =0
    text = content
    for m in re.finditer('num', text):
        #print(len(m))
        ab += 1
        print('num found', m.start(), m.end(), ab)

    if ab < 12:
        assert False

    pre = 0
    for m in re.finditer('previousn', text):
        pre += 1
        print('previousnn found', m.start(), m.end(), pre)

    if pre < 4:
        assert False


@pytest.mark.it('Print next number')
def test_for_next_number(capsys):

    captured = buffer.getvalue()
    print(captured)
    n = app.num
    a = "The next number for the number " + str(n) + " is " + str(n + 1)
    assert str(a) + "\n" in captured

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    print(content)
    ab =0
    text = content
    for m in re.finditer('num', text):
        #print(len(m))
        ab += 1
        print('num found', m.start(), m.end(), ab)

    if ab < 12:
        assert False



