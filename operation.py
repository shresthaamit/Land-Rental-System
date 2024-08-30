from read import loadData,loadhistory
from write import write_rent_details,returnInv
import datetime
def rentLand():
    data = loadData()
    print(type(data))
    print("Available lands:")
    for land in data:
        print(land.strip())
        # print(type(land))
    
    try:
        landid = int(input("Enter a kitta number to rent: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    found = False
    for land in data:
        land_details = land.strip().split(',')
        id = int(land_details[0])
        
        if landid == id:
            landstatus = land_details[5].lower()
            if landstatus != 'available':
                print(f"The land {landid} is unavailable")
                return
            print(landstatus)
            name =  input("Enter your Name: ")
            rentdate = datetime.datetime.now().strftime('%Y-%m-%d')
            city = land_details[1]
            totalmonth = int(input("Enter totalmonth for rent: "))
            monthly_rent = int(land_details[4])
            totalamount = totalmonth * monthly_rent
            land_details[5]="Not Available"
            
            print(land_details[5])
            invoice  = f"""
                 -----Rent Invoice-----
            Customer Name:{name}
            Rent Date:{rentdate}
            Kitta Number:{land_details[0]}
            City:{city}
            Land Faced:{land_details[2]}
            Total Anna:{land_details[3]}
            Total Amount:{totalamount}
            """
       
            
            print(invoice)
            write_rent_details(invoice)
            found = True
            update_land_status(landid, "Not Available")
            bookHistory(landid,name,rentdate,city,totalmonth,totalamount)
            return invoice
            # break
    
    if not found:
        print(f"Kitta number {landid} not found.")
# rentLand()   


def bookHistory(landid,name,rentdate,city,totatalmonth,totaamount):
    bookdetail =f"{landid},{name},{rentdate},{city},{totatalmonth},{totaamount}\n"
    booklist=[]
    print(bookdetail[4])
    with open("bookHistory.txt",'a') as file:
        files=file.write(bookdetail)
        booklist.append(files)
        
        
        
def update_land_status(landid,updatedstatus,filename="landDetails.txt"):
    print("Inside ")
    data = loadData()
    found=False
    i=0
    while i<len(data):
        landdetail= data[i].strip().split(',')
        if landdetail[0] == str(landid):
            landdetail [5]=updatedstatus
            data[i] = ','.join(landdetail)+'\n'
            found = True
            print(f"Updated row: {data[i].strip()}")
            break
        i=i+1
        
    if found:
        with open(filename,'w') as file:
            file.writelines(data)
            print("Booked updated")
    else:
        print(f"{landid} not found")
        

# def updateBorrow(kittano):
#     history = loadhistory()
#     for data in history:
#         borrowhistory = data.strip().split(',')
#         kitta = int(borrowhistory[0])
#         if kitta == kittano:
           


   
def return_Land():
    data = loadData()
    history = loadhistory()
    print(type(history))
    kittano =  int(input("Enter the kittanumber you want to return: "))
    name = input("Enter your username: ")
    username= name.lower()
    for data in history:
        borrowhistory = data.strip().split(',')
        kitta = int(borrowhistory[0])
        name  = borrowhistory[1].lower()
        borrowdate  =  borrowhistory[2]
        totalmonth = int(borrowhistory[4])
        returndate = datetime.datetime.now().strftime('%Y-%m-%d')
        fine = 100
        if kittano == kitta and name ==  username:
            print(f"found,{kitta} and {name}")
            borrowdate_dt = datetime.datetime.strptime(borrowdate, '%Y-%m-%d')
            returndate_dt = datetime.datetime.strptime(returndate, '%Y-%m-%d')
            days_difference = (returndate_dt - borrowdate_dt).days
            borrowmonths = int(days_difference / 30)
            # borrowmonths= int(returndate_dt-borrowdate_dt)/30
            print(type(borrowmonths))
            
            if borrowmonths > totalmonth:
                finemonth = borrowmonths - totalmonth
                totalfine  = fine * finemonth
                print(totalfine)
            totalfine = 0
            invoice  = f"""
                 -----Return Invoice-----
            Kittan number: {kittano}
            Customer Name:{name}
            City:{borrowhistory[3]}
            Rent Date:{borrowdate}
            Return date:{returndate}
            Total Amount:{borrowhistory[5]}
            fine Amount:{totalfine}
            """
            print(invoice)
            returnInv(invoice)
            update_land_status(kittano, "Available")
            # updateBorrow(kittano)
            return
        print("Invalid or not found")
        
# def return_Land(name,rentdate,monthly_rent,totalamount):
#     all_land=  loadData()
#     print(all_land)
#     try:
#         landid = int(input("Enter a kitta number to rent: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         return
#     for land in all_land:
#         land_detail = land.strip().split(',')
#         id = int(land_detail[0])
#         if landid == id:
#             landstatus =  land_detail[5].replace(" ", "").lower()
           
#             if landstatus != 'notavailable':
#                 print(f"The land {landid} is invalid to return")
#                 return
#             name = name
#             rentreturndate = datetime.datetime.now()
#             print(landstatus)
#             print(rentreturndate)
#             print(name)
            
   
        
