"""
Python implementation of Dynamic Array
"""
import ctypes
import sys


class DynamicArray(object):
	
	def __init__(self):
		self.length = 0
		self.capacity = 1
		self.array = self.make_array(self.capacity)
	
	def __len__(self):
		return self.length
	
	def __get_item__(self, index):
		if not 0 <= index < self.length:
			return IndexError('Index is out of bounds.')
		
		return self.array[index]
	
	def append(self, ele):
		if self.length == self.capacity:
			self._resize(2 * self.capacity)
		
		self.array[self.length] = ele
		self.length += 1
	
	def _resize(self, new_capacity):
		temp_array = self.make_array(new_capacity)
		for index in range(self.length):
			temp_array[index] = self.array[index]  # copy over elements to temp_array
		self.array = temp_array
		self.capacity = new_capacity
	
	@staticmethod
	def make_array(capacity):
		return (capacity * ctypes.py_object)()


arr = DynamicArray()
print(len(arr))
print(sys.getsizeof(arr))
