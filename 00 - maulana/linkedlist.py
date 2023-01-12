from msilib.schema import ReserveCost
from re import A
from typing import Reversible


class Node:
	def __init__(self, init_data):
		self.data = init_data
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self, newdata):
		self.data = newdata
	def setNext(self, new_next):
		self.next = new_next
class OrderedLinkedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head==None
	def size(self):
		curent = self.head
		count = 0
		while curent != None:
			count = count + 1
			curent = curent.getNext()
		return count
	def display(self):
		curent = self.head
		while curent != None:
			print(curent.getData())
			curent = curent.getNext()
	def remove(self, item):
		curent = self.head
		previous = None
		found = False
		while not found:
			if curent.getData() == item:
				found = True
			else:
				previous = curent
				curent = curent.getNext()
		if previous == None:
			self.head = curent.getNext()
		else:
			previous.setNext(curent.getNext())
	def search(self,item):
		curent = self.head
		found = False
		stop = False
		while curent != None and not found and not stop:
			if curent.getData() == item:
				found = True
			else:
				if curent.getData() > item:
					stop = True
				else:
			    	curent = curent.getNext()
		return found
	def add(self, item):
		curent=self.head
		previous = None	
		stop = False
		while curent != None and not stop:
			if curent.getData() > item:
				stop = True
			else:
				previous = curent
				curent = curent.getNext()
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else: # ditautkan antara previous dengan curent
			temp.setNext(curent)
			previous.setNext(temp)

a=OrderedLinkedList()
a.add(15)
a.add(10)
a.add(3)
a.add(7)
a.add(21)
b=a,reversed(OrderedLinkedList)
b.display()