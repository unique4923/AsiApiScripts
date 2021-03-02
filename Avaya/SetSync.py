from ManageConnection import SshManager

def DoSetDump(sshObj):
    print("-> DoSetDump")
    SshManager.SendCommand(sshObj, "list config stat")
    if SshManager.GetData(sshObj, "Command successfully completed"):
        print "List stat command completed"
    return True