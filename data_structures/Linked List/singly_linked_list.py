from __future__ import print_function


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.Head = None

    def insert_tail(self, data):
        if self.Head is None:
            self.insert_tail(data)
        else:
            temp = self.Head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def insert_head(self, data):
        newNod = Node(data)
        if self.Head != None:
            newNod.next = self.Head
        self.Head = newNod

    def printList(self):
        tamp = self.Head
        while tamp is not None:
            print(tamp.data)
            tamp = tamp.next

    def delete_head(self):
        temp = self.Head
        if self.Head != None:
            self.Head = self.Head.next
            temp.next = None
        return temp

    def delete_tail(self):
        tamp = self.Head
        if self.Head != None:
            if self.Head.next is None:
                self.Head = None
            else:
                while tamp.next.next is not None:
                    tamp = tamp.next
                tamp.next, tamp = None, tamp.next
        return tamp

    def isEmpty(self):
        return self.Head is None

    def reverse(self):
        prev = None
        current = self.Head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.Head = prev


def main():
    A = Linked_List()
    print("Inserting 1st at Head")
    a1 = input()
    A.insert_head(a1)
    print("Inserting 2nd at Head")
    a2 = input()
    A.insert_head(a2)
    print("\nPrint List : ")
    A.printList()
    print("\nInserting 1st at Tail")
    a3 = input()
    A.insert_tail(a3)
    print("Inserting 2nd at Tail")
    a4 = input()
    A.insert_tail(a4)
    print("\nPrint List : ")
    A.printList()
    print("\nDelete Head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.printList()
    print("\nReverse Linked List")
    A.reverse()
    print("\nPrint List : ")
    A.printList()


if __name__ == '__main__':
    main()
