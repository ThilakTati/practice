class Vits:
    dic={1:'technical',2:'dance',3:'sports',4:'pp',5:'project',6:"debate"}
    l=[]
    def select(self):
        print "1)technical  2)dance 3)sports 4)pp 5)project 6)debate"
        self.dic={1:'technical',2:'dance',3:'sports',4:'pp',5:'project',6:"debate"}
        self.l=[]
        for i in range(4):
            x=input("Enter the event serial number")
            self.l.append(x)
        mod=raw_input('DO you wnat to add or delete[a/d]')
        if mod=='a':
            self.add()
        elif mod=='d':
            self.delete()


    def add(self):
        if len(self.l)<=3:
            print "you have registered for the events below"
            for i in self.l:
                print "%d%s"%(i,self.dic[i]) 
            x=input("enter the event that you want to add")
            self.l.append(x)
            for i in self.l:
                print "%d%s"%(i,self.dic[i])
            mod=raw_input('DO you want to add or delete[a/d]')
            if mod=='a':
                self.add()
            elif mod=='d':
                self.delete()

            else:
                self.display()
        else:
            print "you have already entered 4 events"
            mod=raw_input('DO you wnat to add or delete[a/d/s]')
            if mod=='a':
                self.add()
            elif mod=='d':
                self.delete()
            elif mod=="s":
                self.display()
        
    def delete(self):

        print "u have registered for the events below"
        for i in self.l:
            print "%d%s"%(i,self.dic[i])
        x=input("Enter the event number that you want to delete")
        y=self.l.index(x)
        self.l.pop(y)
        self.display()
        mod=raw_input('DO you wnat to add or delete or save[a/d/s]')
        if mod=='a':
            self.add()
        elif mod=='d':
            self.delete()
        elif mod=='s':
            self.display()

    def display(self):
        for i in self.l:
        
            print "%d%s"%(i,self.dic[i])


obj = Vits()
obj.select()
'''
print "1)technical  2)dance 3)sports 4)pp 5)project 6)debate"
dic={1:'technical',2:'dance',3:'sports',4:'pp',5:'project',6:"debate"}
l=[]


for i in range(4):
    x=input("Enter the event serial number")
    l.append(x)
obj = Vits(l,dic)

mod=raw_input('DO you wnat to add or delete[a/d]')
if mod=='a':
    obj.add()
elif mod=='d':
    obj.delete()

'''





