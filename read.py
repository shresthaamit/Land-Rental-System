def landdetails():
    with open("landDetails.txt", "r") as f:
        for land in f:
            print(land)      
    
    
def loadData():
    with open("landDetails.txt", "r") as f:
        l = f.readlines()
        return l

def loadhistory():
    with open('bookhistory.txt','r') as history:
        data = history.readlines()
        return data