from govee_api2 import api, device
import time
import colour
from getCredentials import getCredentials

def govee_connection():
     # Create Govee client and configure event handlers
    govee_cli = api.Govee('your_email', 'your_password', 'your_client_id_or_EMPTY')
    # BEWARE: This will create a new Govee Client ID with every login. It is recommended to provide an existing client ID
    # within the `Govee` contructor. You can fetch your generated client ID via `govee.client_id` after your successful login

    # Event raised when a new device is discovered
    govee_cli.on_new_device = _on_new_device

    # Event raised when a device status was updated
    govee_cli.on_device_update = _on_device_update

    # Login to Govee
    govee_cli.login()

    # Print out the used client ID
    print('Current client ID is: {}'.format(govee_cli.client_id))

    # Fetch known devices from server
    govee_cli.update_device_list()

    print('Preparing for action :-)')
    # Don't do this in real life. Use the callbacks the client provides to you!
    time.sleep(10)

if __name__ == "__main__":
    print(getCredentials().getUser)