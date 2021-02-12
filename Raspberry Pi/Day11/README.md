Monocular Video is taken using a single camera. With Monocular video depth estimation is very complex in some case not possible also.
Stereo Video is taken using two cameras side-by-side, producing two video streams. A stereo video pair allows depth measurment, so you can find out how far away things are. 




Google Colab GPU SSH with Linux Commad Line Locally by using ngrok(A secure introspectable tunnels to localhost)

	1.) Open Google Colab
	2.) Change runtime to GPU 
	3.) type command - !pip install colab_ssh --upgrade
	4.) open a account in ngrok.com
	6.) Install ngrok as the instruction is given.
	7.) in ngrok dashboard goto Your Authtoken in Authentication section and copy the token.
	8.) type the following commands in colab to launch ssh and make google colab run for long time until not stopped:
			from colab_ssh import launch ssh
			launch_ssh(<token_key>,<Password>)

			import time
			while True:
				time.sleep(300)
	9.) The following comes as output:
			Host google_colab_ssh
					Hostname 2.tcp.ngrok.io
					User root
					Port 11441
	10.) Open the terminal(local linux system)
	11.) type ssh to check if ssh is installed.
	12.) To install openssh-server type :- sudo apt-get install openssh-server ii
	13.) Type command - ssh google_colab_ssh
			with the hostname given it will ask for password type the password created in launch_ssh().
	14.) Now with ssh you can work through local terminal to google colab. 
	15.) If you want to reconnect to google colab through ssh then instead of using ssh google_colab_ssh just type 
		ssh <root>@<hostname> -p<Port Number>
		This will directly connect to google_colab_ssh again.
	
