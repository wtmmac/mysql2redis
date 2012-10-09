import os
pipe = os.popen("redis-cli monitor")
while True:
    line = pipe.readline()

    line = line.split()[1:]
    if(len(line) !=0):
       if(line[0]):
           #print line[0].upper()
           line[0]=line[0].upper()
           if(line[0]=='"'+"DEL"+'"'):
               print "Procress DEL"
               continue

           if(line[0]=='"'+"RENAME"+'"'):
               print "Procress RENAME"
               continue

           if(line[0]=='"'+"RENAMENX"+'"'):
               print "Procress RENAMENX"
               continue

           if(line[0]=='"'+"EXPIRE"+'"'):
               print "Procress EXPIRE"
               continue

           if(line[0]=='"'+"PEXPIRE"+'"'):
               print "Procress PEXPIRE"
               continue

           if(line[0]=='"'+"EXPIREAT"+'"'):
               print "Procress EXPIREAT"
               continue

           if(line[0]=='"'+"PEXPIREAT"+'"'):
               print "Procress PEXPIREAT"
               continue

           if(line[0]=='"'+"PEXPIREAT"+'"'):
               print "Procress PEXPIREAT"
               continue

           if(line[0]=='"'+"PERSIST"+'"'):
               print "Procress PERSIST"
               continue

           if(line[0]=='"'+"MIGRATE"+'"'):
               print "Procress MIGRATE"
               continue

           if(line[0]=='"'+"SET"+'"'):
               print "Procress SET"
               continue

           if(line[0]=='"'+"SETNX"+'"'):
               print "Procress SETNX"
               continue

           if(line[0]=='"'+"SETEX"+'"'):
               print "Procress SETEX"
               continue

           if(line[0]=='"'+"PSETEX"+'"'):
               print "Procress PSETEX"
               continue

           if(line[0]=='"'+"SETRANGE"+'"'):
               print "Procress SETRANGE"
               continue

           if(line[0]=='"'+"MSET"+'"'):
               print "Procress MSET"
               continue

           if(line[0]=='"'+"MSETNX"+'"'):
               print "Procress MSETNX"
               continue

           if(line[0]=='"'+"MSET"+'"'):
               print "Procress MSET"
               continue

           if(line[0]=='"'+"APPEND"+'"'):
               print "Procress APPEND"
               continue

           if(line[0]=='"'+"GETSET"+'"'):
               print "Procress GETSET"
               continue

           if(line[0]=='"'+"DECR"+'"'):
               print "Procress DECR"
               continue

           if(line[0]=='"'+"DECRBY"+'"'):
               print "Procress DECRBY"
               continue

           if(line[0]=='"'+"INCR"+'"'):
               print "Procress INCR"
               continue

           if(line[0]=='"'+"INCRBY"+'"'):
               print "Procress INCRBY"
               continue

           if(line[0]=='"'+"INCRBYFLOAT"+'"'):
               print "Procress INCRBYFLOAT"
               continue

           if(line[0]=='"'+"SETBIT"+'"'):
               print "Procress SETBIT"
               continue

           if(line[0]=='"'+"BITOP"+'"'):
               print "Procress BITOP"
               continue

           if(line[0]=='"'+"HSET"+'"'):
               print "Procress HSET"
               continue

           if(line[0]=='"'+"HSETNX"+'"'):
               print "Procress HSETNX"
               continue

           if(line[0]=='"'+"HMSET"+'"'):
               print "Procress HMSET"
               continue

           if(line[0]=='"'+"HDEL"+'"'):
               print "Procress HDEL"
               continue

           if(line[0]=='"'+"HINCRBY"+'"'):
               print "Procress HINCRBY"
               continue

           if(line[0]=='"'+"HINCRBYFLOAT"+'"'):
               print "Procress HINCRBYFLOAT"
               continue

           if(line[0]=='"'+"LPUSH"+'"'):
               print "Procress LPUSH"
               continue

           if(line[0]=='"'+"LPUSHX"+'"'):
               print "Procress LPUSHX"
               continue

           if(line[0]=='"'+"RPUSH"+'"'):
               print "Procress RPUSH"
               continue

           if(line[0]=='"'+"RPUSHX"+'"'):
               print "Procress RPUSHX"
               continue

           if(line[0]=='"'+"LPOP"+'"'):
               print "Procress LPOP"
               continue

           if(line[0]=='"'+"RPOP"+'"'):
               print "Procress RPOP"
               continue

           if(line[0]=='"'+"BLPOP"+'"'):
               print "Procress BLPOP"
               continue

           if(line[0]=='"'+"BRPOP"+'"'):
               print "Procress BRPOP"
               continue

           if(line[0]=='"'+"LREM"+'"'):
               print "Procress LREM"
               continue

           if(line[0]=='"'+"LSET"+'"'):
               print "Procress LSET"
               continue

           if(line[0]=='"'+"LTRIM"+'"'):
               print "Procress LTRIM"
               continue

           if(line[0]=='"'+"LINSERT"+'"'):
               print "Procress LINSERT"
               continue

           if(line[0]=='"'+"RPOPLPUSH"+'"'):
               print "Procress RPOPLPUSH"
               continue

           if(line[0]=='"'+"BRPOPLPUSH"+'"'):
               print "Procress BRPOPLPUSH"
               continue

           if(line[0]=='"'+"SADD"+'"'):
               print "Procress SADD"
               continue

           if(line[0]=='"'+"SREM"+'"'):
               print "Procress SADD"
               continue

           if(line[0]=='"'+"SMOVE"+'"'):
               print "Procress SMOVE"
               continue

           if(line[0]=='"'+"SPOP"+'"'):
               print "Procress SPOP"
               continue

           if(line[0]=='"'+"SINTERSTORE"+'"'):
               print "Procress SINTERSTORE"
               continue

           if(line[0]=='"'+"SUNIONSTORE"+'"'):
               print "Procress SUNIONSTORE"
               continue

           if(line[0]=='"'+"SDIFFSTORE"+'"'):
               print "Procress SDIFFSTORE"
               continue

           if(line[0]=='"'+"ZADD"+'"'):
               print "Procress ZADD"
               continue

           if(line[0]=='"'+"ZREM"+'"'):
               print "Procress ZREM"
               continue

           if(line[0]=='"'+"ZINCRBY"+'"'):
               print "Procress ZINCRBY"
               continue

           if(line[0]=='"'+"ZREMRANGEBYRANK"+'"'):
               print "Procress ZREMRANGEBYRANK"
               continue

           if(line[0]=='"'+"ZREMRANGEBYSCORE"+'"'):
               print "Procress ZREMRANGEBYSCORE"
               continue

           if(line[0]=='"'+"ZINTERSTORE"+'"'):
               print "Procress ZINTERSTORE"
               continue

           if(line[0]=='"'+"ZUNIONSTORE"+'"'):
               print "Procress ZUNIONSTORE"
               continue

