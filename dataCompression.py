# Data compression 

# Node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.rightBranch = None
        self.leftBranch = None

# LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        lastNode = self.head
        while lastNode is not None:
            print(lastNode.data)
            lastNode = lastNode.rightBranch

    def appendRight(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        lastNode = self.head
        while(lastNode.rightBranch) :
            lastNode = lastNode.rightBranch
        lastNode.rightBranch = node

    def appendLeft(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        lastNode = self.head
        while(lastNode.leftBranch) :
            lastNode = lastNode.leftBranch
        lastNode.leftBranch = node

    def addRight(self, data):
        node = Node(data)
        node.rightBranch = self.head
        self.head = node
    
    def addLeft(self, data):
        node = Node(data)
        node.leftBranch = self.head
        self.head = node

    def addAfter(self, node, data):
        newNode = Node(data)
        if node is None:
            print("The mentioned node is absent")
            return
        newNode.rightBranch = node.rightBranch
        node.rightBranch = newNode

    def contain(self, node):
        if node is None: 
            print("The mentioned node is absent")
            return
        currentNode = self.head
        while(currentNode):
            if(currentNode == node):
                return True
            else:
                currentNode = currentNode.rightBranch
            return False

    def toString(self):
        text = ""
        lastNode = self.head
        while (lastNode is not None):
            text = text + lastNode.data
            lastNode = lastNode.rightBranch
        return text

    def remove(self, data):
        if data is None:
            print("The mentioned node is absent")
            return
        if self.head is not None:
            if self.head.data == data: 
                self.head = self.head.rightBranch
                return
        currentNode = self.head
        while (currentNode is not None):
            if currentNode.data == data:
                break
            prev = currentNode
            currentNode = currentNode.rightBranch
        if currentNode == None:
            return
        prev.rightBranch = currentNode.rightBranch
        print("node has deleted successful")




class HuffmanCoding:
    def __init__(self):
        super().__init__()
    
    #building Huffman tree for encoding text
    def buildTree(self):
        pass

    #Huffman coding
    def freqTable(self, text):
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

    def encode(self, text):
        freqTable = self.freqTable(text)
        for value in sorted(freqTable.values()):
            print(value)
        
    def decode(self,parameter_list):
        pass


tree = LinkedList()
tree.appendLeft("Hey there, ")
tree.appendLeft("hello")
tree.appendLeft("world")
tree.appendLeft("!!!")
tree.print()
print("------")

HuffmanCoding().encode(tree.toString())

# text = "something with my text generating, I have tired? I don't know, but I have other way to fill the gap!=)"
# encode(freqTable(text))