import configparser
import logging

class getCredentials():

    def __init__(self): 
        self.user = None
        self.password = None
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        if self.config['LOGIN']['User'] != "":
            self.user = self.config['LOGIN']['User']
        else:
            logging.exception("User is blank in config.ini file please input a user.")
        
        if self.config['LOGIN']['Password'] != "":
            self.password = self.config['LOGIN']['Password']
        else:
            logging.exception("Password is blank in config.ini file please input a password.")
    

    def getUser(self):
        return self.user
    
    def getPassword(self):
        return self.password