import pytest
from queue_1 import Queue

def test_print():
    print('test_queue')


def create_queue():
    Q1 = Queue()

    Q1.put('p')
    Q1.put('o')
    Q1.put('n')

    return Q1

def test_equals_fail():
    Q2 = create_queue()
    Q2.pop()

    assert create_queue() != Q2