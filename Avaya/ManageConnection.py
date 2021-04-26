from Logger import Log
import SSH
import MyRequest

def RecievedCorrectDataSsh(expect, waitTime = 2):
        data = SSH.WaitForData(expect, waitTime)
        if data == None:
            return False
        else:
            return expect in data

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
                Log("sending pass2")
                # SSH.SendCommand("dddd")
                SSH.SendPassword(MyRequest.Password2)
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
        
        if not retBool:
            switchErr = SSH.ErrorMessageFull
            if not switchErr == "":
                raise Exception("Error Connecting SSH: {0}".format(switchErr))
            else:
                raise Exception("Error Connecting SSH.")
        
        return retBool

def CloseSsh():
    if SSH.IsConnected:
        Log("Closing SSH")
        SSH.Close()
        Log("SSH Closed")