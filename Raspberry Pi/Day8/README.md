There are many solution for remote access to Raspberry Pi. The most common techniques are : SSH and VNC. SSH and VNC involve opening a port on Raspberry Pi (VNC uses port 5900+N and SSH uses port 22). This will expose the Raspberry Pi model and that is why, we have to change password from default.


SSH(Continued)


		SSH can be used to transfer files to a remote server.
		We can use CLI of remote server as we are sitting infront of it.
		SSH uses Asymmetric Cipher(Cipher is an algorithm that perform Encryption and Decryption).
		
		Symmetric Encryption System - 
			One function is shared with two people. This function encrypt or decrypt  the data send along. But this symmetry is not useful for SSH connection to remote server because Cipher(function) can also be stolen and anyone can attack.

		Assymetric Encryption System- 
			This creates a Public and Private key pair. Public Key is accessible to anyone and a user can encrypt data with public key avaliable. This encryption can only be decrypted by Private Key. 
			One function is for encrypting data and another for decrypting. Encrpting data is shared with everyone(Public) but Decrypt key is kept secret ( Private Key).

	SSH Working : 
	
	LOGIN :
	Two Actor involved : The Local Computer(Source) and Remote Server(Destination).
	Steps involved :
	1. Source share its public key to Destination.
	2. Destination then check if the key is registered in its system.
	3. If key is present the Destination it is verified that server has local computer registered.
	4. Destination creates a new key and encrypt this key with the Source's public key and then pass over to Source.
	5. After Source gets the encrypted  data and decrpt it with its Private Key and pass again over to Destination.
	6. Connection Establish.

	AFTER LOGIN :
	SSH creates a tunnel between Source and Destination. And easily data transfer with security.


	SSH Clients:
		MAC Osx anf Linux - Built in Terminal
		Windows - PuTTY
		Android - JuiceSSH
		iOS - prompt




Using Third Party Application for remote access - 
https://magpi.raspberrypi.org/articles/remote-access-your-raspberry-pi-securely
https://remote.it/rpi/
