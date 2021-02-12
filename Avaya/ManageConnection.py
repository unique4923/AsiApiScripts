
class SshManager:
    def __init__(self, ssh, req):
        print("New ssh")
        global SSH
        SSH = ssh
        self.req = req 
        print("ssh created")

    def LoginSsh(self):
        print("Initializing SSH")
        opening = SSH.Initialize(self.req.IpAddress1, self.req.User1, self.req.Password1, "$")
        print("SSH Initialized")

    def CloseSsh(self):
        print("Closing SSH")
        SSH.Close()
        print("SSH Closed")