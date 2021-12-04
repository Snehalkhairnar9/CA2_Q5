# File          : L00163434_Q5_File_2
# Author        : K. Snehal
# Version       : v1.0.0
# Licencing     : (C) 2021 Snehal Khairnar, LYIT
#                 Available under GNU Public License (GPL)
# Description   : Create directories, installing curl
# ----------------------------------


import paramiko


def ssh_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.147.128', username='snehal', password='Snehal@9')

    stdin, stdout, stderr = ssh.exec_command('sudo apt-get install curl')  # unix command to install curl
    stdin, stdout, stderr = ssh.exec_command('mkdir -p Labs/{Lab1,Lab2}')  # unix command create directory and subdirectory
    stdin, stdout, stderr = ssh.exec_command('ls -l --time=atime > document.txt\n')  # unix command create
    # directory
    # and subdirectory

    print(stdout.readlines())
    ssh.close()


if __name__ == "__main__":
    '''
                Main method of application 
                installing curl with directories 
                Parameters:
                 none
                Returns:
                 none
             '''
    ssh_connection()

