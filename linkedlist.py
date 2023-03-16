import os
import time
os.system("cls")
from prettytable import PrettyTable


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
                
class LinkedList_tetap:
    def __init__(self):
        self.head = None
    
    def tambahdepan_tetap(self, data):
        if self.head is None :
            self.head = Node(data)
        else : 
            nodebaru = Node(data)
            nodebaru.next = self.head
            self.head = nodebaru
        
    def getindex(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1

    def hapusdepan_tetap(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next

    def printlist_tetap(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Judul Film"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)

class LinkedList_tambah:
    def __init__(self):
        self.head = None
    
    def tambahdepan_tambah(self, data):
        if self.head is None :
            self.head = Node(data)
        else : 
            nodebaru = Node(data)
            nodebaru.next = self.head
            self.head = nodebaru

    def printlist_tambah(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Judul Film"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)

class LinkedList_delete:
    def __init__(self):
        self.head = None
    
    def tambahdepan_delete(self, data):
        if self.head is None :
            self.head = Node(data)
        else : 
            nodebaru = Node(data)
            nodebaru.next = self.head
            self.head = nodebaru

    def printlist_delete(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Judul Film"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)

list1 = LinkedList_tetap()
list2 = LinkedList_tambah()
list3 = LinkedList_delete()

def menambahdata():
    inputA = input("masukan judul film : ")
    print(inputA)
    list1.tambahdepan_tetap(inputA)
    list2.tambahdepan_tambah(inputA)

def menghapus():
    inputB = int(input("masukan nomor yang ingin dihapus : "))
    x = list1.getindex(inputB-1)
    list3.tambahdepan_delete(x.data)
    list1.hapusdepan_tetap(inputB-1)

while True:
        print("\n")
        print('Loading . . .'.center(80))
        time.sleep(2)
        print("===============================".center(80))
        print("|  Menu aplikasi linked list  |".center(80))
        print("===============================".center(80))
        print("1. Tambah Judul Film".center(80))
        print("2. Delete Film".center(80))
        print("3. Tampil Data Film".center(80))
        print("4. History Film".center(80))
        print("5. Exit".center(80))
        print("===============================".center(80))
        pilihan = str(input(("Silakan masukan pilihan anda: ")))
        if pilihan == "1":
            menambahdata()
        elif pilihan == "2":
            menghapus()
        elif pilihan == "3":
            list1.printlist_tetap()
        elif pilihan == "4":
            while True:
                print("\n")
                print('Loading . . .'.center(80))
                time.sleep(2)
                print("===============================".center(80))
                print("1. Judul Film yang ditambah".center(80))
                print("2. Film yang dihapus ".center(80))
                print("3. Exit".center(80))
                print("===============================".center(80))
                pilih = input("Pilih 1/2/3 : ")
                if pilih == "1":
                    print("\n")
                    print("judul film yang tertampil : ")
                    list2.printlist_tambah()
                elif pilih == "2":
                    print("\n")
                    print("judul film yang tertampil : ")
                    list3.printlist_delete()
                elif pilih == "3":
                    print("\n")
                    print("Terima Kasih :) ".center(80))
                    exit()
                else:
                    print("Pilihan Tidak Sesuai")
        elif pilihan == "5":
            print("Terima Kasih :) ".center(80))
            exit()
        else:
            print("Salah inputan, mohon masukkan nomot yang tersedia!")



        


        
    