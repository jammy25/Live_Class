class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = ' --> ')
		node = node.next
	print('X')

def removeNelement(head, n):
	fast = slow = head
	while n:
		fast = fast.next
		n -= 1
	if fast.next == None:
		return head.next
	else:
		while fast.next:
			fast = fast.next
			slow = slow.next
		slow.next = slow.next.next
	return head

# Driver code
if __name__ == '__main__':
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)

	node = removeNelement(head, 4)
	display(node)
