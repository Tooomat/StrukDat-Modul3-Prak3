#Buatlah program yang mengimplementasikan Struktur data queue menggunakan linkedlist secara 
#manual tanpa menggunakan library dengan ketentuan membuat dan menggunakan method sebagai 
#berikut : 
#1) Method enqueue() 
#2) Method dequeue() 
#3) Method peek() 
#4) Method isEmpty() 
#5) Method size() 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, newItem):
        if self.rear is None:
            self.front = self.rear = Node(newItem)
            return self.front.data
        else:
            self.rear.next = Node(newItem)
            self.rear = self.rear.next
            return self.rear.data

    def dequeue(self):
        if self.front is None:
            return 'Queue is empaty'
        else:
            isDelet = self.front.data
            self.front = self.front.next
            return isDelet
    
    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data
    
    def isEmpaty(self):
        if self.front == None:
            return True
        else:
            return False
    
    def size(self):
        current = self.front
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

queue = Queue()
print('\n========== BANK CITRA IX HAMENG CHI ==========')
#jumlah antrian pagi jam 10.00 WIB
print('\t\t`10.00 WIB`')
for i in range(5):
    print('Nasabah yang masuk: ', queue.enqueue(f'A{i}'))
print(f'Jumlah nasabah sekarang: {queue.size()}\n')

#Antrian bertambah / kedatangan nasabah baru pada pagi jam 10.24 WIB
print('\t\t`10.24 WIB`')
print('Nasabah yang masuk: ', queue.enqueue('A6'))
print('Nasabah yang masuk: ', queue.enqueue('A7'))
print(f'Jumlah nasabah sekarang: {queue.size()}\n')

#Antrean berkurang / nomor antrean telah dipanggil pada 10.45 WIB
print('\t\t`10.45 WIB`')
for i in range(4):
    print(f'Nasabah yang keluar: {queue.dequeue()}')
print(f'Jumlah nasabah sekarang: {queue.size()}')