from Logger import Log
import SSH
import MyRequest

def RecievedCorrectData(expect, waitTime = 2):
        if expect in SSH.WaitForData(expect, waitTime):
            return True
        else:
            return False

def LoginSsh():
        Log("Opening SSH")
        SSH.Open(MyRequest.IpAddress1, MyRequest.IpPort1, MyRequest.User1, MyRequest.Password1)
        # resp = SSH.BufferResponse(connectedChar, 5)
        retBool = False
        connectedChar = "$"
        if RecievedCorrectData(connectedChar):
            Log("First level")
            SSH.SendCommand("ssh {0}@{1} -p 5022".format(MyRequest.User2, MyRequest.IpAddress2))
            if RecievedCorrectData("Password:"):
                Log("sending pass")
                SSH.SendCommand(MyRequest.Password2)
                if RecievedCorrectData("Terminal Type"):
                    Log("sending vt220")
                    SSH.SendCommand("VT220")
                    if RecievedCorrectData("Command:"):
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

def CloseSsh():
        Log("Closing SSH")
        SSH.Close()
        Log("SSH Closed")

class SshManager:
    def __init__(self, ssh, req):
        Log("New ssh")
        global SSH
        SSH = ssh
        self.req = req 
        Log("ssh created")

    def RecievedCorrectData(self, expect, waitTime = 2):
        if expect in SSH.WaitForData(expect, waitTime):
            return True
        else:
            return False
    
    def GetData(self, expect, waitTime = 2):
        return SSH.WaitForData(expect, waitTime)

    def SendCommand(self, command, echo = True, sendEndOfLine = True):
        #public string SendCommand(string command, bool echo = true, bool sendEndOfLine = true) {} C# signature
        SSH.SendCommand(command, echo, sendEndOfLine)

    loggedIn = False
    def PrintStatus(self):
        Log("loggedIn={0}".format(self.loggedIn))

    def LoginSsh(self):
        Log("Opening SSH")
        SSH.Open(self.req.IpAddress1, self.req.IpPort1, self.req.User1, self.req.Password1)
        # resp = SSH.BufferResponse(connectedChar, 5)
        retBool = False
        connectedChar = "$"
        if self.RecievedCorrectData(connectedChar):
            Log("First level")
            SSH.SendCommand("ssh {0}@{1} -p 5022".format(self.req.User2, self.req.IpAddress2))
            if self.RecievedCorrectData("Password:"):
                Log("sending pass")
                SSH.SendCommand(self.req.Password2)
                if self.RecievedCorrectData("Terminal Type"):
                    Log("sending vt220")
                    SSH.SendCommand("VT220")
                    if self.RecievedCorrectData("Command:"):
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
        self.loggedIn = True
        return retBool
       
    def CloseSsh(self):
        Log("Closing SSH")
        SSH.Close()
        Log("SSH Closedd")