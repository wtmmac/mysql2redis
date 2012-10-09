debug=True

from Object import Object
class FurnitureList(Object):
    def __init__(self):
        self.sql="""
        Select BasePrice,CName,SFPosition,ShopID,SFID,(select owner from GShopStore where shopid=RShopFurniture.shopid) as accountid From RShopFurniture,GCommodity where RShopFurniture.CommodityID=GCommodity.CommodityID
        """

    def write2Redis(self):
        self.getDataFromDB()
        indexOfPlayerID = -1
        indexOfShopID = -1
        indexOfSFID = -1
        for i in range(len(sef.head)):
            if(slef.head[i] == "accountid"):
                indexOfPlayerID=i
        if(indexOfPlayerID == -1):
            return False


        for i in range(len(sef.head)):
            if(slef.head[i] == "ShopID"):
                indexOfShopID=i
        if(indexOfShopID == -1):
            return False

        for i in range(len(sef.head)):
            if(slef.head[i] == "SFID"):
                indexOfSFID=i
        if(indexOfSFID == -1):
            return False

        for iLine in self.results:
            objID="player:"+str(iLine[indexOfPlayerID])
            objID=objID+":store:"+str(iLine[indexOfShopID])
            objID=objID+":FurnitureList:"+str(iLine[indexofSFID])

            command="hMSet "+objID+" "
            for i in range(len(sefl.head)):
                command = command + self.head[i]+" "+str(iLine[i])+" "
            from exeRedis import Redis
            redis = Redis()
            redis.exe(commad)
        return True


#Test
if(__name__=="__main__"):
    test=Furniture()
    print test.wirte2Redis()
