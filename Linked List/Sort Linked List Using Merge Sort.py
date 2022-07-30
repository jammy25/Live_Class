class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = " --> ")
		node = node.next
	print('X')

def find_middle(node):
	slow = fast = node
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next
	return slow

def merge_sort_ll(first, second):
	# first , second = head1, head2
	if (first.data < second.data):
		head = ptr = first
		first = ptr.next
	else:
		head = ptr = second
		second = ptr.next

	while first or second:
		if not first:
			ptr.next = second
			return head
		if not second:
			ptr.next = first
			return head
		if first.data < second.data:
			ptr.next = ptr = first
			first = first.next
		else:
			ptr.next = ptr = second
			second = second.next
	return head

def sort_ll(head):
	if not head or not head.next:
		return head
	mid = find_middle(head)
	first = head
	second = mid.next
	mid.next = None
	first = sort_ll(head)
	second = sort_ll(second)
	head = merge_sort_ll(first, second)
	return head

if __name__ == '__main__':
	# head = Node(4)
	# head.next = Node(5)
	# head.next.next = Node(1)
	# head.next.next.next = Node(11)
	head = Node(4)
	head.next = Node(2)
	head.next.next = Node(7)
	head.next.next.next = Node(3)
	head.next.next.next.next = Node(6)
	head.next.next.next.next.next = Node(5)
	head.next.next.next.next.next.next = Node(1)
	head.next.next.next.next.next.next.next = Node(8)

	node = sort_ll(head)
	display(node)