import configparser
import logging

class getConfig():

    def __init__(self): 
        self.mac = None
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        if self.config['ADDRESS']['MAC'] != "":
            self.mac = self.config['ADDRESS']['MAC']
        else:
            logging.exception("MAC is blank in config.ini file please input a MAC Address.")
        
    def getMAC(self):
        return self.mac
