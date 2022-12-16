import pytest
from list import List

def test_push():
    print('test')


def create_fake_list():
    L1 = List()

    L1.push('p')
    L1.push('o')
    L1.push('n')

    return L1

def test_equals_fail():
    L2 = create_fake_list()
    L2[0] = 'd'
    assert create_fake_list() != L2