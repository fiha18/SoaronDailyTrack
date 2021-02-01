Below is the installation process of OpenCV in Linux - ubuntu 20.10.

Steps for installing python in Linux :
Checking version of python - python -V, 
Installing python if not present  by giving following commads - sudo apt-get install wget build-essential checkinstall .

sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev.
downloading latest version python tar file extracting it in " /usr/src ".
cd /usr/src/<Python folder>
  1.  sudo ./configure --enable-optimizations
  2.  sudo make altinstall.
checking python3 version. Python is installed.
Steps for installing OpenCV in Linux :
  1.  sudo apt-get install cmake.
  2.  sudo apt-get install gcc g++.
  3.  sudo apt-get install python3-dev python3-numpy.
  4.  sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev.
  5.  sudo apt-get install libpng-dev.
  6.  sudo apt-get install libjpeg-dev.
  7.  sudo apt-get install libopenexr-dev.
  8.  sudo apt-get install libtiff-dev.
  9.  sudo apt-get install libwebp-dev.
  10. sudo apt-get install git.
  11. git clone https://github.com/opencv/opencv.git.
  12. cd opencv/ 
  13. mkdir build.
  14. cd build
  15. cmake ../ this will show the python version with which OpenCV will be used along with many other dertails of the system.
  16. make
  17. sudo make install
OpenCV is installed can be checked by these commands :
  18. python3 
      import cv2
      print(cv2__version__)
  
Also while an open-cv  .py file and running it in the terminal if shows errors like " cv2.error: OpenCV(4.5.1-dev) /home/fihae/OpenCV/opencv/modules/highgui/src/window.cpp:651: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'"

Then type in terminal -  "pip install opencv-contrib-python".
this will resolve the issue and will run opencv .py file. 
