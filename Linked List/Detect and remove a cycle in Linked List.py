class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = ' --> ')
		node = node.next
	print('X')

def detect_remove_loop(head):
	slow_node = fast_node = head
	flag = 0
	while fast_node.next and fast_node.next.next:
		slow_node = slow_node.next
		fast_node = fast_node.next.next
		if slow_node == fast_node:
			print('Loop Detected!')
			print('Removing Loop now')
			flag = 1
			break
	if flag == 1:
		slow_node = head
		while slow_node.next != fast_node.next:
			slow_node = slow_node.next
			fast_node = fast_node.next
		# Loop removing now
		fast_node.next = None
	else:
		print("No loops detected")
	return head

# Driver Code:
if __name__ == '__main__':

	head = Node(4)
	head.next = Node(2)
	head.next.next = Node(7)
	head.next.next.next = Node(3)
	head.next.next.next.next = Node(6)
	head.next.next.next.next.next = Node(5)
	head.next.next.next.next.next.next = Node(1)
	head.next.next.next.next.next.next.next = Node(8)

	# Create a loop for testing
	head.next.next.next.next.next.next.next.next = head.next.next.next

	node = detect_remove_loop(head)
	display(node)