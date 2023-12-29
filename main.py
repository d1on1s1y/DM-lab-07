import numpy as np


class Node:
    def __init__(self, data: str, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def print_forward_notation(self):
        print(self.data, end=" ")
        if self.left is not None:
            self.left.print_forward_notation()
        if self.right is not None:
            self.right.print_forward_notation()

    def print_backward_notation(self):
        if self.left is not None:
            self.left.print_backward_notation()
        if self.right is not None:
            self.right.print_backward_notation()
        print(self.data, end=" ")


def is_symmetrical(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] and not matrix[j][i]:
                return False

    return True


matrix = np.array([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
])

if is_symmetrical(matrix):
    print("Граф може бути як неорієнтованим, так і орієнтованим.")
else:
    print("Граф орієнтований.")


TREE = Node(
    "^",
    Node(
        "/",
        Node("+",
            Node('9'),
            Node('3')
            ),
        Node("2")
    ),
    Node(
        '-',
        Node('11'),
        Node('*',
            Node('2'),
            Node('4')     
        )
    )
)

print("Польський запис: ", end="")
TREE.print_forward_notation()

print()

print("Зворотний польський запис: ", end="")
TREE.print_backward_notation()

print()
