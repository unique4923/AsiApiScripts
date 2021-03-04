from Logger import Log

class SshManager:
    def __init__(self, ssh, req):
        Log("New ssh")
        global SSH
        SSH = ssh
        self.req = req 
        Log("ssh created")

    def GetData(self, expect, waitTime = 2):
        if expect in SSH.WaitForData(expect, waitTime):
            return True
        else:
            return False
    
    def SendCommand(self, command, echo = True, sendEndOfLine = True):
        #public string SendCommand(string command, bool echo = true, bool sendEndOfLine = true) {} C# signature
        SSH.SendCommand(command, echo, sendEndOfLine)

    def LoginSsh(self):
        Log("Opening SSH")
        SSH.Open(self.req.IpAddress1, self.req.IpPort1, self.req.User1, self.req.Password1)
        # resp = SSH.BufferResponse(connectedChar, 5)
        retBool = False
        connectedChar = "$"
        if self.GetData(connectedChar):
            Log("First level")
            SSH.SendCommand("ssh {0}@{1} -p 5022".format(self.req.User2, self.req.IpAddress2))
            if self.GetData("Password:"):
                Log("sending pass")
                SSH.SendCommand(self.req.Password2)
                if self.GetData("Terminal Type"):
                    Log("sending vt220")
                    SSH.SendCommand("VT220")
                    if self.GetData("Command:"):
                        Log("Connected!")
                        retBool = True
                    else:
                        Log("Never received the Command: prompt from switch")
                else:
                    Log("Failed to get Terminal Type")
            else:
                Log("Fail to get password")
        else:
            Log("Failed first level")

        return retBool
       
    def CloseSsh(self):
        Log("Closing SSH")
        SSH.Close()
        Log("SSH Closedd")