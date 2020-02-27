
# tree imitation
class Box:
    def __init__ (self,cat = None):
        self.cat = cat
        self.nextcat = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, cat):
        lastbox = self.head
        while(lastbox):
            if cat == lastbox:
                return True
            else:
                lastbox = lastbox.nextcat
        return False

    def addToEnd(self, newCat):
        newBox = Box(newCat)
        if self.head is None:
            self.head = newBox
            return
        lastBox = self.head
        while(lastBox.newCat):
            lastBox.nextcat = newBox
    
    def get(self, catIndex):
        lastBox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                boxIndex += 1
                lastBox = lastBox.nextcat
    
    def removeBox(self, rmCat):
        headCat = self.head

        if headCat is not None:
            if headCat.cat == rmCat:
                self.head = headCat.nextcat
                headCat = None
                return
            while headCat is None:
                if headCat.cat == rmCat:
                    break
                lastCat = headCat
                headCat = headCat.nextcat
                headCat = None
                
    def LLprint(self):
        currentCat = self.head
        print("Linked List")
        print("-------")
        i = 0
        while currentCat is not None:
            print(str(i) + ": " + str(currentCat.cat))
            i += 1
            currentCat = currentCat.nextcat
        print(("-------"))

cat = Box()
print(cat.nextcat)
list = LinkedList()
list.addToEnd(cat)
list.addToEnd(cat)
list.addToEnd(cat)
list.LLprint()


# ---------------------------------------