#!/bin/python
import subprocess

# Input from the user
# Local password is not needed since we are running script localy. 
# we could su if we have sudo access
LocalIP = input("Please enter Local IP address:")
Localuser = input("Please enter Local username:")
Localpassword = input("Please enter Local password:")

RemoteIP = input("Please enter remote IP address:")
Remoteuser = input("Please enter remote username:")
Remotepassword = input("Please enter remote password:")
Remotefolder = input("Please enter path for remote folderlocation:")


def copysshfiles():
    #Make the remote Directory if it doesn't exist
    p = subprocess.Popen('sshpass -p '+Remotepassword+' ssh '+ Remoteuser +'@'+ RemoteIP + ' mkdir -p ' + Remotefolder,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        return "Unable to connect to remote machine"

    #Copy authorized_keys to remote machine
    p = subprocess.Popen('sshpass -p '+Remotepassword+' scp /home/'+Localuser+'/.ssh/authorized_keys '+ Remoteuser + '@'+ RemoteIP + ':' + Remotefolder,
                      shell=True)
    #Copy known_hosts to remote machine
    p = subprocess.Popen('sshpass -p '+Remotepassword+' scp /home/'+Localuser+'/.ssh/known_hosts '+ Remoteuser + '@'+ RemoteIP +':' + Remotefolder,
                     shell=True)



copysshfiles()
