# Nim-Backdoor

## Overview

The provided Python program, `Nim-Backdoor.py`, generates a Nim program that operates as a backdoor, allowing remote command execution via a netcat-like session. This tool is designed to work on both Linux and Windows systems. Notably, it has been engineered to bypass popular antivirus software such as Microsoft Defender, Bitdefender, and Kaspersky, making it a stealthy solution for maintaining a persistent connection to a target system.

## Dont upload binaries to VIRUSTOTAL!!!

- **Virustotal Results** [Linux](https://www.virustotal.com/gui/file/c8d6cf2495cea4100bb3811e0139dfd85e656eec94fe4607d0a40ea3e66b80d0?nocache=1) & [Windows](https://www.virustotal.com/gui/file/666dabba172a4c910290f8211ad634b909fc85c99d0408aae4c47a67d5596418?nocache=1)

## Features

- **Cross-Platform:** Works on both Linux and Windows systems.
- **Bypasses Antivirus Detection:** Bypasses Microsoft Defender, Bitdefender, and Kaspersky.
- **Persistent Connection:** Automatically reconnects if the connection is lost.
- **Stealthy:** Waits randomly between 10 to 60 seconds before attempting to reconnect.
- **Command Execution:** Allows remote command execution via a netcat-like session.

## How to Use
![Nim-Backdoor](https://github.com/user-attachments/assets/54924a2f-ae9a-41d3-b764-988f173212d2)

1. **Clone the Repository:**

    `git clone https://github.com/malwarekid/Nim-Backdoor.git && cd Nim-Backdoor`

2. **Run the Script:**

    `python3 Nim-Backdoor.py`

```
python3 Nim-Backdoor.py

    _   ___                 ____             __       __                
   / | / (_)___ ___        / __ \____ ______/ /______/ /___  ____  _____
  /  |/ / / __ `__ \______/ __  / __ `/ ___/ //_/ __  / __ \/ __ \/ ___/
 / /|  / / / / / / /_____/ /_/ / /_/ / /__/ ,< / /_/ / /_/ / /_/ / /    
/_/ |_/_/_/ /_/ /_/     /_____/\__,_/\___/_/|_|\__,_/\____/\____/_/     
                                                                        
                                                  By @malwarekid

Enter IP address: 192.168.1.1
Enter your Port number: 1234
Choose your OS (linux or windows): windows
Enter your output file name: Backdoor

Output saved as Backdoor

```

3. **Enter Input Parameters:**

   - **IP Address:** Enter the IP address for the netcat session.
   - **Port Number:** Enter the port number for the netcat session.
   - **OS:** Choose your operating system (Linux or Windows).
   - **Output File Name:** Enter your desired output file name.

4. **Output Executable:** The script will generate a Nim program and compile it to a binary. The binary will be saved with the name you provided.

## Requirements

- Python 3.6 or above.
- Nim compiler installed on your system.

## Installation

Ensure you have Python 3.6 or above and the Nim compiler installed on your system.

## Example

`python3 Nim-Backdoor.py`

When prompted, enter the IP address, port number, target OS, and output file name:

```
Enter IP address: 192.168.1.1
Enter your Port number: 1234
Choose your OS (linux or windows): windows
Enter your output file name: Backdoor
```
The script will generate a Nim program and compile it to a binary. The binary will be saved as `Backdoor`.

## Contributors

- [Your Name](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

Feel free to contribute, report issues, or provide feedback. Don't forget to follow me on [Instagram](https://www.instagram.com/malwarekid/) and [GitHub](https://github.com/malwarekid/). Happy Hacking!
