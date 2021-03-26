from Logger import Log
import SSH
from ManageConnection import LoginSsh, CloseSsh
#sshObj = SshManager

def DoSetDump():
    Log("-> DoSetDump")
    connected = SSH.IsConnected
    Log("SSH connected: {0}".format(connected))
    if not connected:
        LoginSsh()        
    # SSH.PrintStatus()
    # SSH.SendCommand("list config stat")
    # endMarker = "Command successfully completed"
 
    # if endMarker in SSH.GetData(endMarker):
    #     Log("List stat command completed")
    # else:
    #     Log("not yet")
    #     #try again in loop

    CloseSsh()
    return True