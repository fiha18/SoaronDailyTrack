Raspberry Pi

Raspberry Pi is a small computer that fits snugly in your hand. The hardware specs for the latest (3+) generation Raspberry Pi :
	
	1.4 GHz 64-bit quad-core ARM Cortex-A53, 1GB RAM
	2.4/5Ghz dual band 802.11ac Wireless LAN, 10/100/1000Mbps Ethernet
	Bluetooth 4.2
	4 USB ports, Full HDMI port, Combined 3.5mm audio jack and composite video port, 40 GPIO pins
	Micro SD card slot, VideoCore IV 3D graphics core, Camera interface (CSI), Display interface (DSI).

Operating System on Raspberry Pi
NOOBS(New Out Of the Box Software) - An OS in SD Card shipped with model has variety of OSs from which we can choose.


Raspbian - Raspbian is a Debian-based engineered especially for the Raspberry Pi and it is the perfect general-purpose OS for Raspberry users.Raspbian is the Raspberry foundation’s official supported OS and is capable of accomplishing any task you throw at it. Installing ROS packages and managing them on Raspbian can be quite difficult.

Windows IoT Core - Windows IoT Core is a Windows OS built especially for the Raspberry Pi as a development platform for programmers and coders. Its aim is for programmers to use it to build prototypes of IoT devices using the Raspberry Pi and Windows 10.

Ubuntu Core - Ubuntu Core is the version of Ubuntu designed for Internet of Things applications. Ubuntu is the most popular Linux-based Operating System in the world with over 20+ derivatives and given that it has an active and welcoming forum, it will be easy to get up and running with Ubuntu Snappy Core on your Raspberry Pi. However, if you want to use ROS, you’d be better served by using a Ubuntu version for the Pi.

Ubuntu Mate - Ubuntu Mate is a free and open-source resource flavour of Ubuntu designed for devices that don’t have the best hardware specs. It ships with the APT package manager and works reliably with remote workstation software such as X2GO and LTSP.

Ubuntu Server -  It comes with no desktop, and far less programs installed.



Secure SHell :
A Major protocol to access the network devices and server over internet. It is a program to log into another computer over a network, to execute commands in a remote machine, and to move files from one machine to another.
	1 - It provides strong authentication and secure communications over insecure channels. 
	2 - SSH runs on port number 22 by default and it can be changed very easily. SSH is very secure because it shares and send messages in encrypted form which gives confidentiality and security of data over un-secure network like Internet.
	3 - Once the data for communication is encrypted using SSH, it is extremely difficult to decrypt and read that data, so our passwords also become secure to travel on a public network.
	4 - SSH also uses a public key for the authentication of users accessing a server and it is a great practice providing us extreme security.
	5 -SSH protects a network from attacks. An attacker who has managed to take over a network can only force ssh to disconnect. He or she cannot play back the traffic or hijack the connection when encryption is enabled.
	6 - Can be used to secure any type of protocols like HTTP or FTP.
	7 - SSH can be used to transfer files to a remote server.


To make SSH connection :
	1 - Server host name - can be IP adress or domain name
			ssh username@serverhost
		
	2 - Also needs authentication key to authenticate with remote server (either be Password or Key)

	If authenticated then there will be welcome text and can do permitted work remotely.

Keys - Public and Private Key

	Private Key - stays on the local computer.

	Public Key - can be provided to remote server also.

To create a ssh key : 
	
	ssh-keygen

To create ssh conection:
	
	ssh root@serverhostname

scp/sftp/rsync - secure copy to remote server 

Implementation in RaspberryPi 
To access the command line of a Raspberry Pi remotely from another computer or device on the same network using SSH. The Raspberry Pi will act as a remote device, We can connect to it using a client on another machine.

Using ifconfig - the current network status for the Raspberry model and note the IP Address given in the wlan sub heading.

Enable SSH - 

Method 1 :
	1 - sudo raspi-config command.
	2 - Select Interfacing Option.
	3 - Navigate to SSH.
	4 - Enable SSH.
	5 - Select Ok.
	6 - Choose Finish.
Method 2 :
  By using systemctl :
    
    sudo systemctl enable ssh
    sudo systemctl start ssh

Setting SSH Client : 
	
ssh pi@<IP>
When the connection works you will see a security/authenticity warning. Type yes to continue. You will only see this warning the first time you connect.

	pi@raspberrypi ~ $

If this appears then you are connected to Raspberry Pi Model remotely. 
