#Tugas1
#Buatlah program mengunakan struktur data stack dimana setiap kita memasukkan sebuah String maka 
#program akan menghasilkan output berupa String yang mempunyai urutan terbalik dari inputan kita. 
#Program dibuat secara manual tidak diperkenankan menggunakan library. Kerjakan menggunakan 
#Python untuk mendapatkan nilai tambah.

class Stack:
    def __init__(self):
        self.Stack = []
        self.top = -1

    def isEmpty(self):
        return self.Stack == [] 
        
    #menambah data
    def push(self, newItem):
        while newItem != None:
            #cara 1: manual
            reverse_i = len(newItem) - 1 - i
            self.Stack = newItem[reverse_i]
            return self.Stack
        
            #cara 2: menggunakan append
            #reverse_i = len(newItem) - 1 - i
            #self.Stack.append(newItem[reverse_i])
            #return self.Stack[i]

    #cara 3: menggunakan [::-1]
    #def push2(self, newItem):
        #self.Stack = newItem[::-1]#startIndex endIndex step
        #return self.Stack

stack = Stack()
kata = input("Masukkan input: ")
print('Reversed: ')
for i in range(len(kata)):
    print(f'{stack.push(kata)}', end = '')