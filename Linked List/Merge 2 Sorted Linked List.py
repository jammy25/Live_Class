class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = " --> ")
		node = node.next
	print('X')

def merge_LL(head1, head2):
	first, second = head1, head2
	if (first.data <= second.data):
		head = ptr = first
		first = ptr.next
	else:
		head = ptr = second
		second = second.next

	while (first and second):
		if (first.data <= second.data):
			ptr.next = first
			ptr = ptr.next
			first = first.next
		else:
			ptr.next = second
			ptr = ptr.next
			second = second.next
	if not first:
		ptr.next = second
		return head
	if not second:
		ptr.next = first
		return head

# Driver Code
if __name__ == '__main__':
	node1 = Node(2)
	node1.next = Node(4)
	node1.next.next = Node(8)
	node1.next.next.next = Node(9)

	node2 = Node(1)
	node2.next = Node(3)
	node2.next.next = Node(6)
	node2.next.next.next = Node(7)

	node = merge_LL(node1, node2)
	display(node)	