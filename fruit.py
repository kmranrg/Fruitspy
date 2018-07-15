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

while True:
        ch = int(input("\n\n\tMAIN MENU\n\n1. Add Fruit to Store\n2. Shut Down Application\n\nEnter your choice:"))

        if ch == 1:
                addFruit()
        elif ch ==2:
                break
        else:
                print("Invalid Choice!")

