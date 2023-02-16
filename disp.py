import emp,pickle
f=open('empdata.dat','rb')
while True:
        obj=pickle.load(f)
        obj.display()

f.close()