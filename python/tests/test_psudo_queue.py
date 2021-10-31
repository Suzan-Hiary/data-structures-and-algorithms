from code_challenges.stack_queue_pseudo.stack_queue_pseudo import Pseudo_queue

def test_psudo_enqueue():
    queue=Pseudo_queue()
    queue.enqueue(1)
    #output
    actul=1
    expected=queue.front.data
    assert  actul==expected

def test_psudo_enqueue2():
    queue=Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    #output
    actul=2
    expected=queue.front.data
    assert  actul==expected

def test_psudo_dequeue():
    queue=Pseudo_queue()
    queue.enqueue(1)
    
    #output
    actul=1
    expected=queue.dequeue()
    assert  actul==expected
def test_psudo_dequeue2():
    queue=Pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    #output
    actul=1
    expected=queue.dequeue()
    assert  actul==expected