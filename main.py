from govee_api2 import api, device
from getCredentials import getCredentials
import time
import colour

def govee_connection(email, password, client_id=None):
     # Create Govee client and configure event handlers
    govee_cli = api.Govee(email, password, client_id)
    # BEWARE: This will create a new Govee Client ID with every login. It is recommended to provide an existing client ID
    # within the `Govee` contructor. You can fetch your generated client ID via `govee.client_id` after your successful login

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
    email = getCredentials().getEmail()
    password = getCredentials().getPassword()
    client_id = getCredentials().getClientID()
    print(client_id)
