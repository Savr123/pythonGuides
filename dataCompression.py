# Data compression 

# LinkedList
class LinkedList:
    def __init__(self):
        slef.head = None
        super().__init__()
    
    def append(self, obj):
        

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