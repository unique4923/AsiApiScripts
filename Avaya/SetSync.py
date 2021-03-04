from ManageConnection import SshManager
from Logger import Log

def DoSetDump(sshObj):
    Log("-> DoSetDump")
    SshManager.SendCommand(sshObj, "list config stat")
    if SshManager.GetData(sshObj, "Command successfully completed"):
        Log("List stat command completed")
    return True