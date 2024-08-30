# def write_rent_details(invoice, filename="rent_details.txt"):
#     with open(filename, 'w') as file:
#         file.write(invoice)
#         file.write("\n")
# write.py
import datetime
import os
def write_rent_details(invoice):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"rent_details_{timestamp}.txt"
    with open(filename, 'w') as file:
        file.write(invoice)
        file.write("\n")
def returnInv(invoice):
    folder_name='returnInv'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)   
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"Return_details_{timestamp}.txt"  
    file_path = os.path.join(folder_name,filename)
    with open(file_path,'w') as file:
        file.write(invoice)
        file.write("\n")

def update_land_details(data):
    with open("landDetails.txt",'w') as f:
        f.writelines(data)
        