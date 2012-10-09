debug=True

from Object import Object
class InventoryObj(Object):
    def __init__(self):
        self.sql="""
        SELECT B.Owner, A.ShopID,A.CommodityID,B.CRefID,A.HadNumber,A.MaxNumber,B.ShopName,C.CName,C.BasePrice FROM RShopWareRoom A 
          LEFT JOIN GShopStore B ON A.ShopID=B.ShopID LEFT JOIN GCommodity C ON A.CommodityID=C.CommodityID 
           LEFT JOIN CCityPositionRef D ON B.CRefID=D.CRefID
           """
    def write2Redis(self):
        self.getDataFromDB()
        indexOfOwner = -1
        indexOfShopID = -1
        indexOfCommodityID = -1
        for i in range(len(self.head)):
            if(self.head[i]=="Owner"):
                indexOfOwner=i
                break
        if(indexOfOwner == -1):
            return False

        for i in range(len(self.head)):
            if(self.head[i]=="ShopID"):
                indexOfShopID=i
                break
        if(indexOfShopID == -1):
            return False
        
        for i in range(len(self.head)):
            if(self.head[i]=="CommodityID"):
                indexOfCommodityID=i
                break
        if(indexOfCommodityID == -1):
            return False

        for iLine in self.results:
            objID="player:"+str(iLine[indexOfOwner])
            objID=objID+":store:"+str(iLine[indexOfShopID])
            objID=objID+":inventoryObj:"+str(iLine[indexOfCommodityID])
            
            command="hMSet "+objID+" "
            for i in range(len(self.head)):
                command = command + self.head[i]+" "+str(iLine[i])+" "
            from exeRedis import Redis
            redis = Redis()
            redis.exe(command)
            if(debug):
                print command
                print "===================================================="
        return True 



#test
if(__name__=="__main__"):
    test= InventoryObj()
    print test.write2Redis()
