import random  
import string
from sha1 import SHA1    
from sender import Sender  
from receiver import Receiver

# create a sender to generate and share the last key
sender = Sender() 
sender.share_Kn() 
# create a receiver to get key and verify their authenticity  
receiver = Receiver()  
for i in range(500):  
    sender.share_key()
    receiver.get_new_key()
    