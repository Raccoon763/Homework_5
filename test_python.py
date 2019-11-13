import math

def check_filter():
    assert list(filter(lambda x : x >= 5, [10, 3, 5, 2])) == [10, 5]

def check_map():
    assert list(map(lambda x : x + 15, [1, 2, 3])) == [16, 17, 18]

def check_sorted():
    assert list(sorted(['e', 'y', 'a', 't', 'w'])) == ['a', 'e', 't', 'w', 'y']

def check_pi():
    assert round(math.pi, 2) == 3.14

def check_sqrt():
    assert math.sqrt(49) == 7

def check_pow():
    assert math.pow(3, 2) == 9

def check_hypot():
    assert math.hypot(4, 5) == math.sqrt(41)
