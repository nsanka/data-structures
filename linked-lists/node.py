# Define Node class below:
class Node:
   """
   Build Node class that can have Data of any type and link to Next Node
   """
   def __init__(self, value, next_node=None):
      self.value = value
      self.next_node = next_node

   def get_value(self):
      """Return the value stored for the Node"""
      return self.value

   def get_next_node(self):
      """Return the link to Next Node"""
      return self.next_node

   def set_next_node(self, next_node):
      """Update the link to Next Node"""
      self.next_node = next_node


if __name__ == "__main__":
   my_node = Node(44)
   print(my_node.get_value())