from Logger import Log
import SSH
import MyRequest

def RecievedCorrectDataSsh(expect, waitTime = 2):
        if expect in SSH.WaitForData(expect, waitTime):
            return True
        else:
            return False

def LoginSsh():
        Log("Opening SSH")
        if not SSH.Open(MyRequest.IpAddress1, MyRequest.IpPort1, MyRequest.User1, MyRequest.Password1):
            raise Exception(SSH.ErrorMessageFull)
        
        retBool = False
        connectedChar = "$"
        if RecievedCorrectDataSsh(connectedChar):
            Log("First level")
            SSH.SendCommand("ssh {0}@{1} -p 5022".format(MyRequest.User2, MyRequest.IpAddress2))
            if RecievedCorrectDataSsh("Password:"):
                Log("sending pass")
                SSH.SendCommand(MyRequest.Password2)
                if RecievedCorrectDataSsh("Terminal Type"):
                    Log("sending vt220")
                    SSH.SendCommand("VT220")
                    if RecievedCorrectDataSsh("Command:"):
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
    if SSH.IsConnected:
        Log("Closing SSH")
        SSH.Close()
        Log("SSH Closed")