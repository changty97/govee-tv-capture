from getConfig import getConfig
from govee_api_ble import GoveeDevice


def govee_connection():
    # Initialize the device
    mac_address = getConfig().getMAC()
    my_device = GoveeDevice(mac_address)

    my_device.setPower(True) # Turns device on
    
if __name__ == "__main__":
    govee_connection()
