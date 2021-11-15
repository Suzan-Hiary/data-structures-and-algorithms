# import pytest
from merge_sort import mergesort



def test_empty_list():
    '''Test that empty list is handled correctly'''
    array = []
    mergesort([])
    expected = []
    assert array == expected

############################################################
def test_one_item_list():
    '''Test that single list item is handled correctly'''
    array = [5]
    mergesort(array)
    expected = [5]
    assert array == expected
#########################################################
def test_two_item_list():
    '''Test that list with two items is handled correctly'''
    array = [5,2]
    mergesort(array)
    expected = [2,5]
    assert array == expected
##########################################################
def test_many_item_list():
    '''Test that normal list is handled correctly'''
    array = [1,5,2,4,88]
    mergesort(array)
    expected = [ 1, 2,4, 5, 88]
    assert array == expected


