from typing import Any, Optional
import random

class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None: 
        self.__elements.append(value)

    def attention(self) -> Any:
        return self.__elements.pop(0)

    def size(self) -> int:
        return len(self.__elements)

class Node:
    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
    
    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: 
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: 
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert_node(root, value, other_value):
            if root is None:
                root = Node(value, other_value)
            elif value <= root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)
            
    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)
            return aux

        node = __search(self.root, value)
        return node 

class Pokemon:
    def __init__(self, number, name, types, weaknesses, has_mega, has_gigantamax):
        self.number = number
        self.name = name
        self.types = types
        self.weaknesses = weaknesses
        self.has_mega = has_mega
        self.has_gigantamax = has_gigantamax

    def __str__(self):
        mega = " (Mega)" if self.has_mega else ""
        gmax = " (G-Max)" if self.has_gigantamax else ""
        return f"#{self.number:04d} {self.name} - Tipos: {self.types} - Débil a: {self.weaknesses}{mega}{gmax}"