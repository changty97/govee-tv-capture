import configparser
import logging

class getCredentials():

    def __init__(self): 
        self.email = None
        self.password = None
        self.client_id = None
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        if self.config['LOGIN']['Email'] != "":
            self.email = self.config['LOGIN']['Email']
        else:
            logging.exception("Email is blank in config.ini file please input a Email.")
        
        if self.config['LOGIN']['Password'] != "":
            self.password = self.config['LOGIN']['Password']
        else:
            logging.exception("Password is blank in config.ini file please input a password.")

        if self.config['LOGIN']['ClientID'] != "":
            self.client_id = self.config['LOGIN']['ClientID']
        else:
            logging.exception("ClientID is blank in config.ini file please input a ClientID.")
    
    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getClientID(self):
        return self.client_id
