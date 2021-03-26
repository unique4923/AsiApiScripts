from Tools.Comm import Clear, PrintStuff
from SetSync import DoSetDump
from PortSync import DoPortDump
from ManageConnection import SshManager
from datetime import datetime
from Logger import Log
from Avaya.SetSync import DoSetDump
from Avaya.PortSync import DoPortDump
import MyRequest

# from ManageConnection import LoginSsh, CloseSsh

def Run(action):
    Log("Doing Avaya Script!")
    
    if action == "SETSYNC":
        return DoSetDump()
    elif action == "PORTSYNC":
        return DoPortDump()
    else:
        raise Exception('No script for Avaya action: "{0}"'.format(MyRequest.Action))
    return False
