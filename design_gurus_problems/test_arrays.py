from arrays import running_sum
from arrays import contains_duplicate, contains_duplicate_v2
from arrays import find_difference_array

def test_running_sum():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert running_sum([]) == []

def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 4]) == False
    assert contains_duplicate([1, 2, 3, 1]) == True
    assert contains_duplicate([3, 2, 6, -1, 2, 1]) == True

def test_contains_duplicate_v2():
    assert contains_duplicate_v2([1, 2, 3, 4]) == False
    assert contains_duplicate_v2([1, 2, 3, 1]) == True
    assert contains_duplicate_v2([3, 2, 6, -1, 2, 1]) == True

# def test_find_difference_array():
#     assert find_difference_array([2, 5, 1, 6, 1]) == [13, 6, 0, 7, 14]
#     assert find_difference_array([3, 3, 3]) == [6, 0, 6]
#     assert find_difference_array([1, 2, 3, 4, 5]) == [14, 11, 6, 1, 10]