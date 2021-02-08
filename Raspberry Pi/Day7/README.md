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



SSH(Secure SHell)
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
