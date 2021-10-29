

from code_challenges.reverse_linked_list import LinkedList, Node




def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected

def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

# def test_node_without_value():
#     with pytest.raises(TypeError):
#          Node()




def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()

  # Act
  ll.insert(1)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected

def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()

  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.data

  # Assert
  assert actual == expected
  assert ll.head.next.data == 1


def test_includes():
    
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

    ##
    expected=True
    actuall=ll.includes(1)
    assert actuall==expected


def test_toString():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

     #output
    expected= "{ 0 } -> { 1 } -> NULL"
    actul= str(ll)

    assert expected==actul

def test_append():
    
    #input
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)
    ll.append(2)
    #output
    expected= "{ 0 } -> { 1 } -> { 2 } -> NULL"
    actul= str(ll)
    assert expected==actul
    
def test_append_multi():
    
    #input
    ll=LinkedList()
    ll.insert(1)
    ll.insert(1)
    ll.append_multi([4,3,3])
    #output
    expected= "{ 1 } -> { 1 } -> { 4 } -> { 3 } -> { 3 } -> NULL"
    actul= str(ll)
    assert expected==actul

def test_insertBefore():
      #input
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2) 
    ll.insert(3) 
    ll.insertBefore(1,3)
    expected= "{ 3 } -> { 2 } -> { 3 } -> { 1 } -> NULL"
    actul=str(ll)
    assert expected==actul

def test_insert_after():
    #input
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert_after(1,22)
    #output
    expected='{ 2 } -> { 1 } -> { 22 } -> NULL'
    actul= str(ll)
    assert expected==actul

def test_zipLists():
  #input
  ll = LinkedList()
  ll.insert(2)
  ll.insert(3)
  ll.insert(1)
  ll2 = LinkedList()
  ll2.insert(4)
  ll2.insert(9)
  ll2.insert(5)
  #output
  expected='{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL'
  actul= str(LinkedList.zipLists(ll, ll2))
  assert expected==actul


##### lab 7 tests
def test_kth_from_end():
    #input
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1) 
    #output
    actul=ll.kth_from_end(0)
    expected=2
    assert actul==expected
def test_kth_from_end2():
    #input
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1) 
    #output
    actul=ll.kth_from_end(2)
    expected=3
    assert actul==expected

def test_kth_from_end3():
    #input
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1) 
    #output
    actul=ll.kth_from_end(-1)
    expected=1
    assert actul==expected
    
def test_kth_from_end4():
    #input
    ll = LinkedList()
    ll.insert(2)
    #output
    actul=ll.kth_from_end(0)
    expected=2
    assert actul==expected

def test_kth_from_end5():
    #input
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1) 
    ll.insert(0) 
    #output
    actul=ll.kth_from_end(2)
    expected=3
    assert actul==expected