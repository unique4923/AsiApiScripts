
class SshManager:
    def __init__(self, ssh, req):
        print("New ssh")
        global SSH
        SSH = ssh
        self.req = req 
        print("ssh created")

    def GetData(self, expect, waitTime = 2):
        if expect in SSH.WaitForData(expect, waitTime):
            return True
        else:
            return False
    
    def SendCommand(self, command, echo = True, sendEndOfLine = True):
        #public string SendCommand(string command, bool echo = true, bool sendEndOfLine = true) {} C# signature
        SSH.SendCommand(command, echo, sendEndOfLine)

    def LoginSsh(self):
        print("Opening SSH")
        SSH.Open(self.req.IpAddress1, self.req.IpPort1, self.req.User1, self.req.Password1)
        # resp = SSH.BufferResponse(connectedChar, 5)
        retBool = False
        connectedChar = "$"
        if self.GetData(connectedChar):
            print "First level"
            SSH.SendCommand("ssh {0}@{1} -p 5022".format(self.req.User2, self.req.IpAddress2))
            if self.GetData("Password:"):
                print "sending pass"
                SSH.SendCommand(self.req.Password2)
                if self.GetData("Terminal Type"):
                    print "sending vt220"
                    SSH.SendCommand("VT220")
                    if self.GetData("Command:"):
                        print("Connected!")
                        retBool = True
                    else:
                        print("Never received the Command: prompt from switch")
                else:
                    print "Failed to get Terminal Type"
            else:
                print "Fail to get password" 
        else:
            print "Failed first level"

        return retBool
       
    def CloseSsh(self):
        print("Closing SSH")
        SSH.Close()
        print("SSH Closedd")