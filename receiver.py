import random  
import string
from sha1 import SHA1    


class Receiver():  

    bootstrap_key = None # first key shared by the receiver 
    previus_key = None  # the Kn+1 key used to verify if Kn is a valid key 
    quantity = 0 # index used into the authentication process 
    current_key = None 

    def __init__(self) -> None:
        with open('sharedKn.txt','r') as f:   
            self.bootstrap_key = f.read()   
            self.previus_key = self.bootstrap_key 

    # get a new key by the previous one   
    def get_key(self):  


        self.quantity += 1   
        with open('output.txt','r') as f:   
            self.current_key = f.read()   
        

    # authentication function 
    def authenticate(self, index, bitMessage):   

        bitOutput = self.bootstrap_key
        
        for i in range(index): 
            sh1Receiver = SHA1(bitOutput)  
            bitOutput = sh1Receiver.hexdigest() 
            
        print("----------------------------------------") 
        print(bitMessage) 
        print(bitOutput)
        if bitMessage == bitOutput: 
            return True  

    # high level function used to control the authenticity proccess 
    def get_new_key(self):  

        self.get_key() 
        if self.authenticate(self.quantity, self.current_key) == True: 
            print("New key was verified") 
        else: 
            print("Error in the verification of new key") 
        self.previus_key = self.current_key

