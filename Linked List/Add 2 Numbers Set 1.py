# The digits are stored in reverse order in the Linked List

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = ' --> ')
		node = node.next
	print('X')

def add2Numbers(head1, head2):
	head = ptr = Node(-1)
	carry = 0
	while (head1 or head2):
		if not head1:
			ptr.next = Node((head2.data + carry) % 10)
			carry = ((head2.data + carry) // 10)
			ptr = ptr.next
			head2 = head2.next
			continue
		if not head2:
			ptr.next = Node((head1.data + carry) % 10)
			carry = ((head1.data + carry) // 10)
			ptr = ptr.next
			head1 = head1.next
			continue
		node = Node((head1.data + head2.data + carry) % 10)
		carry = ((head1.data + head2.data + carry) // 10)	
		head1 = head1.next
		head2 = head2.next
		ptr.next = node
		ptr = node
	if carry:
		ptr.next = Node(carry)
	return head.next

# Driver Code
if __name__ == '__main__':
	node1 = Node(3)
	node1.next = Node(4)
	node1.next.next = Node(2)

	node2 = Node(4)
	node2.next = Node(6)
	node2.next.next = Node(5)

	node = add2Numbers(node1, node2)
	display(node)