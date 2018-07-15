import pickle

print("\t\t\t***** Fruit Store Management System *****")

def addFruit():
        data = {}
        file = open("fruitData.pkl","ab")
        ID = int(input("Enter fruit ID:"))
        name = input("Enter fruit name:")
        price = int(input("Enter the price(rs/kg):"))
        det = {}
        det["name"] = name
        det["price"] = price
        data[ID] = det
        pickle.dump(data,file)
        file.close()
        print("\t*** Fruit(s) added successfully ***")
        return

def dataLoad(file):
        var = pickle.load(file)
        print(var)
        return True

def showFruit():
        file = open("fruitData.pkl","rb")
        print("\n--------------------------------------------------------\n\t")
        try:
                while dataLoad(file):
                        continue
        except EOFError:
                print("\n----- All Fruits in Store are printed successfully -----")
        file.close()
        return

while True:
        ch = int(input("\n\n\t--> Main Menu\n\n1. Add Fruit to Store\n2. Show Fruits in Store\n3. Shut Down Application\n\nEnter your choice:"))

        if ch == 1:
                addFruit()
        elif ch == 2:
                showFruit()
        elif ch == 3:
                break
        else:
                print("Invalid Choice!")

