# File          : L00163434_Q5_File_2
# Author        : K. Snehal
# Version       : v1.0.0
# Licencing     : (C) 2021 Snehal Khairnar, LYIT
#                 Available under GNU Public License (GPL)
# Description   : Create directories, installing curl
# ----------------------------------


import paramiko
import time


# Open SSH connection to the device
# first install ssh-server on the VM
#           sudo apt install openssh-server openssh-client
#
def ssh_connection(ip):
    """
    """
    # try:
    username = "snehal"
    password = "Snehal@9"

    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(ip.rstrip("\n"), username=username, password=password)
    connection = session.invoke_shell()
    connection.send("sudo apt install curl")
    connection.send("mkdir TEMPL")
    connection.send("ls -l --time=atime > doc1.txt\n")  # unix command to list directory contents and save to file
    time.sleep(1)


if __name__ == "__main__":
    '''
                Main method of application 
                installing curl with directories 
                Parameters:
                 none
                Returns:
                 none
             '''
    ssh_connection("192.168.147.128")
