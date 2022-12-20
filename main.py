from getCredentials import getCredentials
from govee_api_ble import GoveeDevice


def govee_connection():
    # Initialize the device
    my_device = GoveeDevice('34:20:03:49:72:3D')

    my_device.setPower(True) # Turns device on
    
if __name__ == "__main__":
    govee_connection()
