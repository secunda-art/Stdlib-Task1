from exercises import *
import random
import math
import os
import re

def test_combinations():
    assert set(combinations(['white', 'green', 'blue', 'red'], 3)) == set([('white', 'green', 'blue'), ('white', 'green', 'red'), ('white', 'blue', 'red'), ('green', 'blue', 'red')])
    assert combinations(['white', 'green', 'blue', 'red'], 5) == []
    assert set(combinations(['white', 'green', 'blue', 'red'], 1)) == set([('white',), ('green',), ('blue',), ('red',)])
    assert len( combinations(range(10), 5) ) == 252

def test_days_between():
    assert isinstance(days_between('2011-11-11', '2012-12-12'), int)
    assert days_between('2011-11-11', '2012-12-12') == 397
    assert days_between('1988-09-28', '2020-07-10') == 11608
    assert days_between('1999-12-31', '2020-07-01') == 7488
    assert days_between('1111-11-11', '1111-11-11') == 0

    for _ in range(5):
        today = datetime.date.today()
        delta_n = random.randint(0, 500)
        delta = datetime.timedelta(days=delta_n)
        assert days_between(str(today), str(today + delta)) == delta_n

def test_file_exists():
    fname = 'abs.txt'
    open(fname, 'w')
    assert file_exists(fname)
    os.remove(fname)
    assert not file_exists(fname)

def test_get_current_week():
    assert isinstance(get_current_week(11, 9, 2020), int)
    assert get_current_week(11, 9, 2020) == 37
    assert get_current_week(1, 1, 1900) == 1
    assert get_current_week(31, 12, 2020) == 53
    assert get_current_week(9, 8, 1977) == 32
    assert get_current_week(1, 1, 2006) == 52
    assert get_current_week(2, 1, 2006) == 1
    assert get_current_week(29, 12, 2008) == 1

def test_deg2rad():
    test_set = [(180, 3.141593), (70, 1.221730), (110, 1.919862), (1812.3, 31.630602), (-45, -0.785398), (0, 0)]
    for r in test_set:
        degree, radian = r
        print(f"Test {degree} ...")
        assert abs( math.cos(deg2rad(degree)) - math.cos(radian) ) < 1e-5
        assert abs( math.sin(deg2rad(degree)) - math.sin(radian) ) < 1e-5
        print("Passed")
    return

def test_discriminant_sqrt():
    test_set = [(4, 5, 1, 3), (4, 15, 1, 14.456832), (1, 5, 3, 3.605551), (1, 2, 1, 0), (-2, -3, 2, 5.0), (1, 1, 100, math.nan), \
                (10, -10, 13, math.nan)]
    for t in test_set:
        a, b, c, result = t
        if math.isnan(result):
            assert math.isnan(discriminant_sqrt(a, b, c))
        else:
            assert abs( discriminant_sqrt(a, b, c) - result ) < 1e-5

def test_popular_letters():
    test_set = [ ("baaaaccddd", ['a', 'd', 'c']), ("bzozz_z2ca5xzasbfbb]q1a", ['z', 'b', 'a'])]
    for t in test_set:
        s, result = t
        assert popular_letters(s) == result

def test_json_write():
    dict1 = { 'a' : 1, 'b' : 2, 'c' : 12}
    json_write(dict1, 'file.txt')
    with open('file.txt') as f:
        t = f.read()
        assert re.match(r'.*a.*1.*b.*2.*c.*12.*', t) is not None
    dict1 = { 'z' : 1, 'a' : 2, 'd' : 12}
    json_write(dict1, 'file.txt')
    with open('file.txt') as f:
        t = f.read()
        assert re.match(r'.*a.*2.*d.*12.*z.*1.*', t) is not None

def test_replacer():
    assert replacer("Hello, world. I am working on a task. Work, work, work", "wor") == "Hello, ***. I am *** on a task. Work, ***, ***"
    assert replacer("Regular expressions are beautiful", "u") == "*** expressions are ***"
    assert replacer("Regular expressions are beautiful", "help") == "Regular expressions are beautiful"
    assert replacer("Test again, test again, test again", "test") == "Test again, *** again, *** again"

def test_is_holiday():
    assert is_holiday('2020-06-12')
    assert ~is_holiday('2020-07-13')
    assert is_holiday('2001-01-01')
    assert is_holiday('2017-11-04')
    assert is_holiday('2019-03-08')
    assert ~is_holiday('2020-07-25')
    assert ~is_holiday('2020-02-27')
    assert ~is_holiday('2020-04-10')
    assert is_holiday('2022-04-18', 'GB')
    assert ~is_holiday('2021-04-18', 'GB')
