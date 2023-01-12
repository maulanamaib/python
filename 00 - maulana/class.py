class BilanganKompleks:
    def __init__(self,a,b):
        self.real=a
        self.im=b   
    def display(self):
        print (self.real,'+',self.im,'i')
    def __str__(self):
        return str(self.real) + " + " + str(self.im) + " i "
    def addKompleks(self,obj):
        a=self.real+obj.real
        b=self.im+obj.im
        return BilanganKompleks(a,b)
    def __add__(self,obj):
        a=self.real+obj.real
        b=self.im+obj.im
        return BilanganKompleks(a,b)
    def __mul__(self,data):
        temp1=(self.real*data.real)-(self.im*data.im)
        temp2=(self.real*data.im)+(data.real*self.im)
        return BilanganKompleks(temp1,temp2)

a=BilanganKompleks(4,6)
b=BilanganKompleks(5,10)
c=a * b
print(a)
print(b)
print(c)

class BinaryTree:
  def __init__(self, root):
    self.key = root
    self.leftChild = None
    self.rightChild = None
  