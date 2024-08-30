from read import landdetails
from write import write_rent_details
from operation import rentLand,return_Land
def main():
    while True:
        print("Enter 1. For display Lands.")
        print("2. For Rent a land.")
        print("3. For Return a Land")
        print("4. To Exit")
        userinput = input("Enter your choice: ")
        print(userinput)
        if userinput == '1':
            landdetails()
            
        elif userinput == '2':
            rentLand()
        elif userinput == '3':
            return_Land()
        elif userinput == '4':
            print("Exiting...")
            break
        else:
            print("Sorry, invalid choice!")

if __name__ == "__main__":
    main()