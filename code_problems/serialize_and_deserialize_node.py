"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

    def serialize(self, end_node="#"):
        """
        Encodes a tree to a single string.

        :rtype: str
        """
        serial = [self.val]

        if self.left is None:
            serial.append(end_node)

        else:
            serial.extend(self.left.serialize(end_node))

        if self.right is None:
            serial.append(end_node)

        else:
            serial.extend(self.right.serialize(end_node))

        serial = "".join(serial)

        return serial 

    def deserialize(data):
        """
        Decodes encodes data to tree.

        :type data: str
        :rtype: TreeNode
        """



if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'



