#Tugas1
#Buatlah program mengunakan struktur data stack dimana setiap kita memasukkan sebuah String maka 
#program akan menghasilkan output berupa String yang mempunyai urutan terbalik dari inputan kita. 
#Program dibuat secara manual tidak diperkenankan menggunakan library. Kerjakan menggunakan 
#Python untuk mendapatkan nilai tambah.

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if not self.is_empty():
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            return None

    def push(self, newItem):
        self.top += 1
        self.stack.append(newItem)

def Reverse(input):
    stack = Stack()
    for i in input:
        stack.push(i)

    reverse = ''
    while not stack.is_empty():
        reverse += stack.pop()

    return reverse

kata = input("Masukkan input: ")
print(f'Reverse: {Reverse(kata)}')
