# COMMS
Comms is a terminal based program made for communication between 2 computers.

## Introduction 
To start first download the 'comms.exe' from the github release or from the 'dist' folder.Then run this command
```bash
python comms.exe -h
```
This will provide you with a short description of the tool.

### 'start'
Initializes the server for the other computer to connect to. Only one computer needs to be setup as an server. The '--ip' and '--port' can be specified for this mode, but defaults tp '0.0.0.0' and '1010' respectively. The '--nickname' deafults to 'user' unless specified.

### 'connect'
Connects to a already created Server. The '--ip' and '--port' are required for this mode. The ip and port here represent the the ip address and port to connect to. The '--nickname' deafults to 'user' unless specified.

