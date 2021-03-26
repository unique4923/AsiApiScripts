from Logger import Log
import SSH
from Avaya.ManageConnection import LoginSsh, CloseSsh
#sshObj = SshManager

def DoSetDump():
    Log("-> DoSetDump")
    connected = SSH.IsConnected
    Log("SSH connected: {0}".format(connected))
    if not connected:
        LoginSsh()
    if not SSH.IsConnected:
        Exception("Error Connecting SSH")
    
    SSH.SendCommand("list config stat")
    endMarker = "Command successfully completed"
    response = SSH.WaitForData("bananas")
    if response == None:
        response = SSH.GetCurrentMessage()
        Log("Current: {0}".format(response))

        if endMarker in response:
            Log("get current message had it")
        else:
            raise Exception("Not getting response")
    else:
        Log("List stat command completed")

    CloseSsh()
    return True