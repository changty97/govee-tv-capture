"""Module get MAC Address from config file."""
import configparser
import logging


class getConfig:
    """
    A class to get a MAC Address.

    ...

    Methods
    -------
    setMAC():
        Sets a MAC Address.
    getMAC():
        Returns MAC Address from the config file.
    """

    def __init__(self):
        """Constructs all the necessary attributes for the getConfig object."""
        self.mac = None
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        if self.config["ADDRESS"]["MAC"] != "":
            self.setMAC(self.config["ADDRESS"]["MAC"])
        else:
            logging.exception(
                "MAC is blank in config.ini file please input a MAC Address."
            )

    def setMAC(self, mac):
        """Sets the MAC Address"""
        self.mac = mac

    def getMAC(self):
        """Returns the MAC Address"""
        return self.mac
