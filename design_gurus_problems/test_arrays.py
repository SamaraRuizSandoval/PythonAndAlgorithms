from arrays import running_sum
from arrays import contains_duplicate

def test_running_sum():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum([]) == []

def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([3, 2, 6, -1, 2, 1]) == True

def test_contains_duplicate_v2():
    pass