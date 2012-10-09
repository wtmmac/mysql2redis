import exeCommand# import exe 
debug=True
class Redis:
    """This class is express the Redis Database.
    You can use this class to execute the command,
    get all keys , set the key's value or get the 
    key's value
    """
    def exe(self,command):
        self.redis="redis-cli "
        """
        this method used to execute the redis
        command,and put the  replay in a list
        return the replay list
        """
        command = self.redis +command
        if(debug):
            print command
        result=exeCommand.exe(command)
        return result.split()

    def keys(self):
        """
        This method to get all keys is the database ,
        the keys name in a list ,and the types in another. 
        return the list[names,types]
        """
        keys = self.exe("keys '*'")
        types=[]
        for word in keys:
            Type=self.exe("type "+word)
            types.append(Type[0])
        result=[keys,types]
        return result
    
class RedisSet(Redis):
    """
    This class is express the redis's Set 
    """
    def __init__(self,name):
        self.name = name;
        self.value= []
        
    def setValue(self,value):
        if(type(value) != type(self.value)):
            print "value's type must be list"
            import sys
            sys.exit(0);
        else:
            self.value = value

    def writeToRedis(self):
        commd="sAdd "+self.name
        for word in self.value:
            word =" "+str(word)
            commd = commd + word
        reply=self.exe(commd)[0]
        if debug:
           print commd
        return reply
    
    def readFromRedis(self):
        self.value=[]
        commd="sMembers "+self.name
        self.value = self.exe(commd)



class RedisHash(Redis):
    """
    This class express the redis hash
    """
    def __init__(self,name):
        self.name = name
        self.value={}

    def setValue(self,value):
        if(type(value) != type({})):
            print "value  must a hash"
            import sys
            sys.exit(-1)
        else:
            self.value=value

    def writeToRedis(self):
        comd="hmset "+self.name
        for key in self.value.keys():
            comd = comd +" "+key+" "+ str(self.value[key])+" "
        reply=self.exe(comd);
        return reply[0]
    def readFromRedis(self):
        self.value={}
        comd="hGetAll "+self.name
        tem=self.exe(comd)
        for i in range(0,len(tem),2):
            self.value[tem[i]]=tem[i+1]


class RedisZSet(Redis):
    def __init__(self,name):
        self.name = name
        self.value={"scores":[],"members":[]}
    def setValue(self,value):
        if(type(value) != type([]) or len(value)!=2 \
                or len(value[0]) != len(value[1]) ):
            print "value's type must be %s"%type(value)
            import sys
            sys.exit(-1);
        else:
            self.value['scores'] = value[0]
            self.value["members"]= value[1]

    def writeToRedis(self):
        comd="zAdd "+self.name
        scores=self.value['scores']
        members=self.value['members']
        for i in range(0,len(scores)):
             comd= comd +" "+str(scores[i])+" "+str(members[i])

        result = self.exe(comd)
        return result
    def readFromRedis(self):
        comd="zRange "+self.name +" 0 -1"
        self.value["scores"]=[]
        members=self.exe(comd)
        self.value['members']=members
        for member in members:
            comd="zScore "+self.name+" "+member
            self.value["scores"].append(self.exe(comd)[0])


class RedisString(Redis):
    def __init__(self,name):
        self.name = name
        self.value ="" 
    
    def setValue(self,value):
        if(type(value) != type(self.value)):
            print "value must be a string"
            import sys
            sys.exit(-1)
        else:
            self.value = value
            
    def writeToRedis(self):
        comd="set "+self.name+" '"+self.value+"'"
        return self.exe(comd)[0]
    def readFromRedis(self):
        comd="get "+self.name
        self.value=self.exe(comd)[0]
     
class RedisList(Redis):
    def __init__(self,name):
        self.name = name
        self.value= []

    def setValue(self,value):
        if(type(self.value) != type(value) ):
            print "value must be a list"
            import sys
            sys.exit(-1)
        else:
            self.value = value
    def writeToRedis(self):
        comd="dele "+self.name
        self.exe(comd)
        comd="rPush "+self.name
        for word in self.value:
            comd = comd +" "+str(word)
        return self.exe(comd)[0]
    def readFromRedis(self):
        comd="lRange "+self.name+" 0 -1"
        self.value = self.exe(comd)


#Test
if (__name__=="__main__"):
    #test = Redis()
    #print test.exe(" keys '*'");
    #print test.keys()
    #test = RedisHash("ha")
    #print test.value
    #test.setValue({'f':3,'mm':"mm"})
    #test.readFromRedis()
    #print test.value

    #test=RedisSet("se")
    #print test.value
    #test.setValue([1,3,"hello"])
    #print test.value
    #test.writeToRedis()
    #test.readFromRedis()
    #print test.value

    #test=RedisZSet('z')
    #print "just init,test.value:", test.value
    #test.setValue([[1,2,3,1],[1,"hell",3.14,"word"]] )
    #print "after set value,test.value:",test.value
    #print test.writeToRedis()
    #test.readFromRedis()
    #print "after read from Redis,test.value:",test.value

    #test= RedisString("str")
    #print "init,value",test.value
    #test.setValue("this is a test string")
    #print "after set value,value",test.value
    #print test.writeToRedis()
    #test.readFromRedis()
    #print "after read from redis value,value",test.value

    #test= RedisList("li")
    #print "init,value:",test.value
    #test.setValue([1,"st",3.14,True])
    #print "after set value,value:",test.value
    #print test.writeToRedis()
    #test.readFromRedis()
    #print "after read from redis,value:",test.value
