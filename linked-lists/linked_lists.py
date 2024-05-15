from node import Node

class LinkedList:
   """
   Class for Linked Lists
   """
   def __init__(self, value=None):
      self.head_node = Node(value)

   def get_head_node(self):
      """Return the head node of the linked list"""
      return self.head_node

   def insert_beginning(self, new_value):
      """Insert a new node at the beginning of the linked list"""
      new_node = Node(new_value)
      new_node.set_next_node(self.head_node)
      self.head_node = new_node

   def stringify_list(self):
      """Return a string representation of the linked list"""
      string_list = ""
      current_node = self.get_head_node()
      while current_node:
         if current_node.get_value() != None:
            string_list += str(current_node.get_value()) + "\n"
         current_node = current_node.get_next_node()
      return string_list

   def remove_node(self, value_to_remove):
      """Remove a node from the linked list"""
      current_node = self.get_head_node()
      if current_node.get_value() == value_to_remove:
         self.head_node = current_node.get_next_node()
      else:
         while current_node:
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
               current_node.set_next_node(next_node.get_next_node())
               current_node = None
            else:
               current_node = next_node


if __name__ == "__main__":
   ll = LinkedList(5)
   ll.insert_beginning(70)
   ll.insert_beginning(5675)
   ll.insert_beginning(90)
   print(ll.stringify_list())