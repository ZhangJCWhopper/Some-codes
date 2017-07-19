class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def insert(elements):
	head = ListNode(elements[0])
	current = head
	for one in elements[1:]:
    	current.next = ListNode(one)
    	current = current.next

def show(head):
	result = []
	while head:
		result.append(head.val)
		head = head.next
	return result