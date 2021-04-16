from Logger import Log
import SSH
from Avaya.ManageConnection import LoginSsh, CloseSsh
import ListStation
#sshObj = SshManager

def DoSetDump():
    Log("-> DoSetDump")
    connected = SSH.IsConnected
    Log("SSH connected: {0}".format(connected))
    if not connected:
        LoginSsh()

    listStatNumbers = ListStation.GetNumbersInSwitch()

    CloseSsh()
    return True