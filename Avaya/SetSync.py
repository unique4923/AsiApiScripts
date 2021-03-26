from Logger import Log
#sshObj = SshManager
def DoSetDump(ssh):
    Log("-> DoSetDump")
    ssh.PrintStatus()
    ssh.SendCommand("list config stat")
    endMarker = "Command successfully completed"
 
    if endMarker in ssh.GetData(endMarker):
        Log("List stat command completed")
    else:
        Log("not yet")
        #try again in loop
    return True