from code_challenges.tree.tree import Node , BinarySearchTree , BinaryTree
import pytest




@pytest.fixture

def tree():
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('a')
  b_node = Node('b')
  c_node = Node('c')
  d_node = Node('d')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node 
  return tree


def test_pre_order(tree):
  # set expected list
  expected = ["a", "b", "d", "c"]
  # set actual to return value of post_order call
  actual = tree.pre_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")

def test_in_order(tree):
  # set expected list
  expected = ["d", "b", "a", "c"]
  # set actual to return value of post_order call
  actual = tree.in_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")  

def test_post_order(tree):
  # set expected list
  expected = ["d", "b", "c", "a"]
  # set actual to return value of post_order call
  actual = tree.post_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")  

# ******************** binary search tree tests **********************
@pytest.fixture

def binary_tree():
  # Arrange
  # Create tree instance
  binary_tree = BinarySearchTree()

  # Create Nodes for A,B,C,D
  a_node = Node('A')
  b_node = Node('B')
  c_node = Node('C')
  d_node = Node('D')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  binary_tree.root=a_node 
  return binary_tree






def test_add_once():
     # Arrange
    # Create tree instance
    tree = BinarySearchTree ()
    # add "A" to the tree
    tree.add('A')
    # set expected list
    expected = "A"
    # set actual to the tree root value
    actual = tree.root.data
    # assert actual is same as expected
    assert actual == expected



def test_contains_value():
    # Arrange
    # Create tree instance
    tree = BinarySearchTree ()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = True
    # set actual to the tree root value
    actual = tree.__contains__("B")
    # assert actual is same as expected
    assert actual == expected

def test_not_contains_value():
   # Arrange
    # Create tree instance
    tree = BinarySearchTree ()
    # add "A" to the tree
    tree.add("A")
    tree.add("B")
    tree.add("C")
    # set expected list
    expected = False
    # set actual to the tree root value
    actual = tree.__contains__("E")
    # assert actual is same as expected
    assert actual == expected



def test_max_value():
   tree = BinarySearchTree ()
   tree.add(1)
   tree.add(2)
   tree.add(3)
   tree.add(18)
   tree.add(15)

   #output

   expected = 18
   actul=tree.maximum()

   assert expected==actul
def test_max_value2():
   tree = BinarySearchTree()
   tree.add(1)
   tree.add(2)
   tree.add(-12)
   tree.add(18)
   tree.add(0)

   #output

   expected = 18
   actul=tree.maximum()

   assert expected==actul