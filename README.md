# ConkyConfig

A Conky Config I'm using on various machines. I wanted the same output on each machine with minimal effort from myself.

I'm publishing this publicly just in case anyone else can get some value from this, or maybe you find this and want to offer criticism or improvements.

So far this shows
* System info
* CPU info (usage stats and speed)
* RAM info
* Disk info (should loop through mount points and show them)
* Network info (pass in the interface name with a parameter)
* Docker Container status

All of this is written in Python. This was my first attempt at Python and I've nicked some functions from Stackoverflow

## Installation
#### Ubuntu 16.04

Install Conky and dependencies:

```bash
sudo apt install conky-all supervisor lm-sensors -y
```

Clone this directory to `~/.conky`:

```bash
git clone -b master git@github.com:MatthewBooth/ConkyConfig.git ~/.conky
```

Install any Python requirements

```bash
sudo apt install python3 python3-setuptools python3-pip -y
```

```bash
sudo pip3 install jinja2 docker psutil py3nvml netifaces colour fcache 
```

Initialise the temperature sensors and follow the instructions step by step (you can mostly just stick with the defaults):

```bash
sudo sensors-detect
```

Run the installation script:

This will create a configuration for Supervisor to keep the Conky process running (it has a tendency to fall over occasionally) and create a symlink from ~/.conky/conky_config.lua to ~/.conkyrc

```bash
cd ~/.conky
sudo ./install/install.py
```

Finally, start or restart Supervisor

```bash
sudo service supervisor restart
```