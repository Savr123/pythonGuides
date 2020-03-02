# Data compression 

# Node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        lastNode = self.head
        while lastNode is not None:
            print(lastNode.data)
            lastNode = lastNode.next

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        lastNode = self.head
        while(lastNode.next) :
            lastNode = lastNode.next
        lastNode.next = node

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def addAfter(self, node, data):
        newNode = Node(data)
        if node in None:
            print("The mentioned node is absent")
            return
        newNode.next = node.next
        node.next = newNode

    def contain(self, node):
        if node is None: 
            print("The mentioned node is absent")
            return
        currentNode = self.head
        while(currentNode):
            if(currentNode == node):
                return True
            else:
                currentNode = currentNode.next
            return False

    def remove(self, data):
        if data is None:
            print("The mentioned node is absent")
            return
        if self.head is not None:
            if self.head.data == data: 
                self.head = self.head.next
                return
        currentNode = self.head
        while (currentNode is not None):
            if currentNode.data == data:
                break
            prev = currentNode
            currentNode = currentNode.next
        if currentNode == None:
            return
        prev.next = currentNode.next
        print("node has deleted successful")


tree = LinkedList()
tree.add("Hey there, ")
tree.append("hello")
tree.append("world")
tree.append("!!!")
tree.print()
tree.remove("Hey there, ")
tree.remove("Hey")
tree.remove("world")
tree.print()
        

#Huffman coding
def freqTable(text):
    wordFreq = {}
    for word in text:
        if word not in wordFreq.keys():
            wordFreq.update({word : 1 })
        else:
            wordFreq.update({word : wordFreq[word]+1})
    print(wordFreq)
    return wordFreq
    # print("Frequencies\n" + str(wordFreq) + "\n")


# ---------------------------------------

def encode(freqTable):
    for value in sorted(freqTable.values()):
        print(value)
    
def decode(parameter_list):
    pass

# text = "something with my text generating, I have tired? I don't know, but I have other way to fill the gap!=)"
# encode(freqTable(text))