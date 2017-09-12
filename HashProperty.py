import hashlib
import string
import time
import random
from random import randint

class HashPropety:
   def __init__(self, b=5):
       self.bits = b            # Number of hex bits to match

   def generate_hash(self, msg):
       #message = msg
       message = msg + "\n"
       m = hashlib.md5()
       m.update(message)
       return m.hexdigest()

   def generate_string(self, length):
       return ''.join(random.choice(string.ascii_letters + string.punctuation) for i in range(length))

   def one_way_property(self, msg):
       orignalMessage = msg
       originalHash = self.generate_hash(orignalMessage)
       originalHash_nbits = originalHash[0:self.bits]   # 1 hex bit = 4 binary bits
       duplicateHash_nbits = None                       # n hex bits = n * 4 bits
       count = 0

       while (originalHash_nbits != duplicateHash_nbits):
           count += 1
           lengthOfString = randint(1, 26)                           #Max length of string = 26
           randomString = self.generate_string(lengthOfString)
           duplicateHash = self.generate_hash(randomString)
           duplicateHash_nbits = duplicateHash[0:self.bits]          #Extract first n hex bits of hash

       print '\nOriginal Message = %-27s      Corresponding Hash = %32s' % (str(orignalMessage), str(originalHash))
       print '\nDuplicate Message = %-27s     Corresponding Hash = %32s'  % (str(randomString), str(duplicateHash))
       print '\nNumber Of Iterations = %d' % count

   #Collission free property is comparitvely easy to break as it becomes a birthday attack problem
   def collision_free_property(self):
        HashesExplored = dict()
        count = 0

        while (True):
            count += 1
            lengthOfString = (randint(1, 26))
            randomMessage = self.generate_string(lengthOfString)
            duplicateHash = self.generate_hash(randomMessage)
            duplicateHash_nbits = duplicateHash[0:self.bits]

            if duplicateHash_nbits in HashesExplored and HashesExplored[duplicateHash_nbits] != randomMessage:
                collidingHash = self.generate_hash(HashesExplored[duplicateHash_nbits])
                print '\nMessage1 = %-27s     Corresponding Hash = %32s' % (randomMessage, str(duplicateHash))
                print '\nMessage2 = %-27s     Corresponding Hash = %32s' % (HashesExplored[duplicateHash_nbits], str(collidingHash))
                print '\nNumber Of Iterations = %d' % count
                break
            HashesExplored[duplicateHash_nbits] = randomMessage

#Run multiple times and report average
if __name__ == "__main__":
    startTime = time.time()
    lenthOfHashValue = 5    #Beyond 6 it may run for around 15 mins for one way property
    _break = HashPropety(lenthOfHashValue)
    print "ONE WAY PROPERTY:"
    _break.one_way_property("Breaking one way property")
    print "\n---------------------------------------------------------------------------------------------\n"
    print "COLLISION FREE PROPERTY:"
    _break.collision_free_property()
    print time.time() - startTime