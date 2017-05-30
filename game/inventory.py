
class Inventory:
    def __init__(self,holder,capacity):
        self.items = []
        self.capacity = capacity
        self.holder = holder

    def addItem(self,item):
        if item.stackable and (item in self.items):
            self.findItem(item).amount += 1
        elif len(self.items) < self.capacity:
            self.items.append(item)

    def addItems(self,items):
        for item in items:
            if item.stackable and (item in self.items):
                self.findItem(item).amount += 1
            elif len(self.items) < self.capacity:
                self.items.append(item)

    def displayInventory(self):
        print('Inventory (%i):' % len(self.items))
        for item in self.items:
            print('%s (%i)' % (item.name,item.amount))

    def findItem(self,item):
        for i in self.items:
            if i == item:
                return i

    def useItem(self,index):
        if self.items[index]:
            self.items[index].use(self.holder)
            self.items[index].amount -= 1
            if self.items[index].amount == 0:
                self.removeItem(index)
        self.displayInventory()

    def useItem(self,item):
        if item in self.items:
            item.use(self.holder)
            item.amount -= 1
            if item.amount == 0:
                self.items.remove(item)

    def removeItem(self,index):
        self.items.pop(index)

    def getItemData(self,index):
        try:
            return (self.items[index].image,self.items[index].amount)
        except:
            return (None,0)