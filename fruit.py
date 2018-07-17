import pickle, time

print("\n\n-----------------------------------------------------------------")
print("\t\t*** Fruit Store Management System ***")
print("-----------------------------------------------------------------")

def addFruit():
        data = {}
        file = open("fruitData.pkl","ab")
        ID = int(input("Enter fruit ID:"))
        name = input("Enter fruit name:")
        price = int(input("Enter the price(rs/kg):"))
        det = {}
        data["ID"] = ID
        det["name"] = name
        det["price (rs/kg)"] = price
        data["detail"] = det
        pickle.dump(data,file)
        print("\t*** Fruit added successfully ***")
        file.close()
        return

def dataLoadToShow(file):
        var = pickle.load(file)
        print(var)
        return True

def showFruit():
        status = 0
        try:
                file = open("fruitData.pkl","rb")
        except FileNotFoundError:
                print("\nWARNING: There are no fruits in the store")
                status = 1
        print("\n------------------------------------------------------------------\n\t")
        if status == 0:
                try:
                        while dataLoadToShow(file):
                                continue
                except EOFError:
                        print("\n---------- All Fruits in Store are printed successfully ----------")
                file.close()
        return

def billStore(file,ID,qty,bill,billFile):
        var = pickle.load(file)
        if var["ID"] == ID:
                billDet = {}
                cost = var["detail"]["price (rs/kg)"]
                price = cost*qty
                bill["ID"] = ID
                billDet["qty"] = qty
                billDet["cost per kg"] = cost
                billDet["price (rs/kg)"] = price
                billDet["name"] =  var["detail"]["name"]
                bill["detail"] = billDet
                pickle.dump(bill,billFile)
        return True

def billCalc(num):
        billFile = open("bill.pkl","rb")
        price = 0
        print("\n\nCalculating Bill", end = "")
        for i in range(5):
                time.sleep(0.5)
                print("..", end = "")
        print("\n\n\n--------------------------------------------------------\n")
        print("\t\tFruit Bill\n")
        for i in range(num):
                var =  pickle.load(billFile)
                print("Fruit:",var["detail"]["name"])
                print("Fruit ID:",var["ID"])
                print("Quantity (in kg):",var["detail"]["qty"])
                print("Cost per kg:",var["detail"]["cost per kg"])
                print("Price:",var["detail"]["price (rs/kg)"])
                price = price + var["detail"]["price (rs/kg)"]
                print("--------------------------------------------------------")
        print("Total Amount:",price)
        print("--------------------------------------------------------\n")
        billFile.close()
        return

def buyFruit():
            num = int(input("\nHow many types of fruits do you want to purchase:"))
            bill = {}
            billFile = open("bill.pkl","wb")
            for i in range(1,num+1):
                    ID = int(input("\nEnter the ID of fruit %i you want to buy:"%i))
                    qty = int(input("Enter quantity (in kg):"))
                    file = open("fruitData.pkl","rb")
                    try:
                        while billStore(file,ID,qty,bill,billFile):
                                continue        
                    except EOFError:
                            print("\n")
                    file.close()
            billFile.close()
            return num
            
num = 0
while True:
        ch = int(input("""\n\n\t--> Main Menu

1. Add Fruit to Store
2. Show Fruits in Store
3. Buy Fruits
4. Calculate Bill
5. Shut Down Application

Enter your choice:"""))
        if ch == 1:
            addFruit()
        elif ch == 2:
            showFruit()
        elif ch == 3:
            num = buyFruit()
        elif ch == 4:
            billCalc(num)
        elif ch == 5:
            break
        else:
            print("Invalid Choice!")
