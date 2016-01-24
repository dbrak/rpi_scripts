Instructions
============
A good tutorial on the Pigpio daemon can be found [here](http://www.rototron.info/dht22-tutorial-for-raspberry-pi/)

Start and Stop the Daemon
--------------------------
Source code and instructions can be found at [this link](http://www.abyz.co.uk/rpi/pigpio/download.html)

To start the daemon:
```
sudo pigpiod
```

To stop the daemon:
```
sudo killall pigpiod
```
Python Libraries
----------------
There are two needed 1 for the daemon and 1 for the DHT22 sensor.  The daemon library should have been installed with daemon so only requires:

```
import pigpiod
```

The DHT22 sensor library needs to be downloaded separately and put into a folder.  You will need to be in folder to import it:

```
import DHT22
```

Running Remotely
----------------
When running remotely the script was terminating when the SSH session ended.  Hopefully, I solved this problem but running the script with the nohup command to catch the hangup signal:

```
nohup pythong <script_name.py> &
```

