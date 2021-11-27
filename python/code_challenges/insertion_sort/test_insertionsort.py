from insertion_sort import insertion_Sort

import pytest


@pytest.fixture
def unsorted_array():
    return [8,4,23,42,16,15]


@pytest.fixture
def reverse_sorted():
    return [20,18,12,8,5,-2]


@pytest.fixture
def few_uniques():
    return [5,12,7,5,5,7]
   

@pytest.fixture
def nearly_sorted():
    return [2,3,5,7,13,11]



def test_unsorted(unsorted_array):
  """Test that unsorted is sorted"""
  actual = insertion_Sort(unsorted_array)
  expected = [4, 8, 15, 16, 23, 42]
  assert actual == expected

def test_reverse_sorted(reverse_sorted):
    """Test that reversed sort is sorted"""
    actual = insertion_Sort(reverse_sorted)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_few_uniques(few_uniques):
    """Test that array with duplicates is sorted"""
    actual = insertion_Sort(few_uniques)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_nearly_sorted(nearly_sorted):
    '''Test that nearly sorted array is sorted'''
    actual = insertion_Sort(nearly_sorted)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual== expected    
