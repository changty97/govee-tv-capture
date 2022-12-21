"""Module connects to any Govee Device."""
from govee_api_ble import GoveeDevice
from .getConfig import getConfig


def goveeConnection():
    """Creates a connection to a Govee device via Bluetooth"""
    # Initialize the device
    mac_address = getConfig().getMAC()
    my_device = GoveeDevice(mac_address)

    my_device.setPower(True)  # Turns device on


if __name__ == "__main__":
    goveeConnection()
