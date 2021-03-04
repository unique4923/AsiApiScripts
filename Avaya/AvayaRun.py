from Tools.Comm import Clear, PrintStuff
from SetSync import DoSetDump
from PortSync import DoPortDump
from ManageConnection import SshManager
from datetime import datetime
from Logger import Log
# from ManageConnection import LoginSsh, CloseSsh

class AvayaScript():
    def __init__(self, Ssh, req):
        self.SshConnection = Ssh
        self.Req = req

    def Run(self):
        # print("-> AvayaRunScript")
        Log("-> AvayaRunScript")
        global SSH
        SSH = SshManager(self.SshConnection, self.Req)
        if not SSH.LoginSsh():
            raise Exception("Failed to connect.  See previous logging for")
        
        avayaAction = self.Req.Action.upper()
        if avayaAction == "SETSYNC":
            scr = DoSetDump
        elif avayaAction == "PORTSYNC":
            scr = DoPortDump
        else:
            raise Exception('No script for Avaya action: "{0}"'.format(self.Req.Action))
       
        scr(SSH)
        Log("Script Complete!")
        SSH.CloseSsh()
        
        return True
        # PrintStuff()
        # Clear()
        # PrintStuff()