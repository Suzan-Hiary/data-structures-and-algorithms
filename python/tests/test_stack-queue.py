from code_challenges.queue_with_stacks.stacks_and_queues import Stack , Queue
import pytest


@pytest.fixture
def stack():
   stack=Stack()
   stack.push(1)
   stack.push(2)
   stack.push(3)
  
  
   return stack





def test_push(stack):
    #output
    expected=3
    actul=stack.top.data
    assert expected==actul   




def test_pushMultiple(stack):
      #output
    expected=3
    actul=stack.top.data
    assert expected==actul

def test_pop1(stack):
    #output
    expected=3
    actul=stack.pop()
    assert expected==actul

def test_pop2(stack):
      #input
    stack.pop()
    stack.pop()
    stack.pop()
    #output
    expected=True
    actul=stack.is_empty()
    assert expected==actul

def test_peek(stack):
      #output
    expected=1
    actul=stack.peek()
    assert expected==actul

def test_initate_stack():
    #INPUT
    stack=Stack()
     #output
    expected=True
    actul=stack.is_empty()
    assert expected==actul

def test_raise_exception1():
    #input
    stack=Stack()
    #output
    with pytest.raises(Exception):
         stack.pop()
def test_raise_exception2():
    #input
    stack=Stack()
    #output
    with pytest.raises(Exception):
         stack.peek()


@pytest.fixture
def queue():
    queue=Queue()
    queue.enqueue(1)
    return queue

def test_enqueue(queue):
    #output
    actul=1
    expected=queue.front.data
    assert  actul==expected

def test_enqueue2(queue):
    queue.enqueue(2)
    queue.enqueue(3)
    #output
    actul=3
    expected=queue.rear.data
    assert  actul==expected

def test_dequeue(queue):
    #output
    actul=1
    expected=queue.dequeue()
    assert  actul==expected

def test_peek(queue):
    #output
    actul=1
    expected=queue.peek()
def test_dequeue(queue):
    with pytest.raises(Exception):
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()


def test_emptyQueue():
    queue=Queue()

    expected=True
    actul=queue.is_empty()
    assert expected==actul

def test_raise_exception():
    queue=Queue()
    with pytest.raises(Exception):
        queue.peek()         