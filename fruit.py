import pickle, time

print("\t\t\t***** Fruit Store Management System *****")

def addFruit():
        data = {}
        file = open("fruitData.pkl","ab")
        ID = int(input("Enter fruit ID:"))
        name = input("Enter fruit name:")
        price = int(input("Enter the price(rs/kg):"))
        det = {}
        data["ID"] = ID
        det["name"] = name
        det["price per kg"] = price
        data["detail"] = det
        pickle.dump(data,file)
        file.close()
        print("\t*** Fruit(s) added successfully ***")
        return

def dataLoadToShow(file):
        var = pickle.load(file)
        print(var)
        return True

def showFruit():
        file = open("fruitData.pkl","rb")
        print("\n--------------------------------------------------------\n\t")
        try:
                while dataLoadToShow(file):
                        continue
        except EOFError:
                print("\n----- All Fruits in Store are printed successfully -----")
        file.close()
        return

def dataLoadToBuy(file, ID, qty):
        var = pickle.load(file)
        if var["ID"] == ID:
                price = var["detail"]["price per kg"]
                price = price*qty
                print("\n\nCalculating Bill", end = "")
                for i in range(5):
                        time.sleep(0.5)
                        print("..", end = "")
                print("\n\n\n--------------------------------------------------------\n")
                print("\t\tFruit Bill\n")
                print("Fruit:",var["detail"]["name"])
                print("Quantity (in kg):",qty)
                print("--------------------------------------------------------")
                print("Total Amount:",price)
                print("--------------------------------------------------------\n")
        return True

def buyFruit():
            ID = int(input("\nEnter the ID of fruit you want to buy:"))
            qty = int(input("Enter quantity (in kg):"))
            file = open("fruitData.pkl","rb")
            try:
                while dataLoadToBuy(file, ID, qty):
                        continue        
            except EOFError:
                    print("\n")
            file.close()
            return
            
while True:
        ch = int(input("\n\n\t--> Main Menu\n\n1. Add Fruit to Store\n2. Show Fruits in Store\n3. Buy Fruits\n4. Shut Down Application\n\nEnter your choice:"))

        if ch == 1:
            addFruit()
        elif ch == 2:
            showFruit()
        elif ch == 3:
            buyFruit()
        elif ch == 4:
            break
        else:
            print("Invalid Choice!")

