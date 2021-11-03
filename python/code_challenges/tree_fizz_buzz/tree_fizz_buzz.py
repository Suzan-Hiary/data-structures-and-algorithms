def fizz_buzz_tree(k_ary):
    def walk(node):
        if node:
            for child in node.childs:
                if child.data % 3 == 0 and child.data % 5 == 0:
                    child.data = "FizzBuzz"
                elif child.data % 3 == 0:
                    child.data = "Fizz"
                elif child.data % 5 == 0:
                    child.data = "Buzz"
            if node.front:
                walk(node.front)
    
    walk(k_ary.root)
    return k_ary