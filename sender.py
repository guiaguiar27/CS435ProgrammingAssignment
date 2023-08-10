import random  
import string
from sha1 import SHA1    


# generate random strings  
class Sender(): 

    Kn = None   
    current_key = None 
    previus_key = None   

    def __init__(self) -> None:
        self.Kn = self.generate_key(100) 


    # generate a new string key based on the size 
    def generate_key(self, size): 
        letters = string.ascii_lowercase 
        result = ' '
        for i in range(size): 
            partial = random.choice(letters) 
            result =  result + partial 
        return result  
    # share a new key with a trusted part 
    def share_Kn(self):  
        with open('sharedKn.txt','w') as f:  
            sh1Setup = SHA1(self.Kn) 
            f.write(sh1Setup.hexdigest()) 
        self.previus_key = sh1Setup.hexdigest()
    
    def share_key(self):       

        with open('output.txt','w') as f:
            sh1Setup = SHA1(self.previus_key) 
            f.write(sh1Setup.hexdigest()) 
        self.previus_key = sh1Setup.hexdigest()
        with open('log.txt','a') as f:   
            f.write(self.previus_key)  
            f.write('\n')
        
        





