class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	
	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to Reverse the linked list
	def reverse(self):
		prev = None
		post = None
		ptr = self.head

		while (ptr != None):
			post = ptr.next
			ptr.next = prev
			prev = ptr
			ptr = post

		self.head = prev
		return self.head

	# Function to insert node at the beginning
	def add_begin(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked list
	def print_ll(self):
		if self.head is None:
			print("LL is empty")
		else:
			n = self.head
			while n is not None:
				print(n.data, "-->", end = " ")
				n = n.next
			print("X")

# Driver Code
LL1 = linkedList()
LL1.add_begin(20)
LL1.add_begin(10)
LL1.add_begin(5)
LL1.reverse()
LL1.print_ll()