from getpass import getuser
from utils.globals import term
from ui.ui import set_display

async def send_file(client, filepath):

    # try to open the file exactly as user inputs it
    try: 
        await client.send_file(client.get_current_channel(), filepath)
    except:
        # assume the user ommited the prefix of the dir path,
        # try to load it starting from user's home directory:
        try:
            filepath = "/home/" + getuser() + "/" + filepath
            await client.send_file(client.get_current_channel(), filepath)
        except:
            # Either a bad file path, the file was too large,
            # or encountered a connection problem during upload
            msg = "Error: Bad filepath"
            await set_display(term.bold + term.red + term.move(term.height - 1, \
                term.width - len(msg) - 1) + msg)
