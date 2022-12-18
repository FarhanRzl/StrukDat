class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	def isEmpty(self):
		return len(self.queue) == 0

	def insert(self, data):
		self.queue.append(data)

	# def delete(self):
	# 	try:
	# 		max_val = 0
	# 		for i in range(len(self.queue)):
	# 			if self.queue[i] > self.queue[max_val]:
	# 				max_val = i
	# 		item = self.queue[max_val]
	# 		del self.queue[max_val]
	# 		return item
	# 	except IndexError:
	# 		print()
	# 		exit()

	def delete(self):
		try:
			min_val = 0
			for i in range(len(self.queue)):
				if self.queue[i] < self.queue[min_val]:
					min_val = i
			item = self.queue[min_val]
			del self.queue[min_val]
			return item
		except IndexError:
			print()
			exit()


# if __name__ == '__main__':
# 	myQueue = PriorityQueue()
# 	myQueue.insert([12,'data'])
# 	myQueue.insert([1, 'anak'])
# 	myQueue.insert([14, 'bapa'])
# 	myQueue.insert([7, 'ibu'])
# 	# print(myQueue)
# 	while not myQueue.isEmpty():
# 		print(myQueue.delete())