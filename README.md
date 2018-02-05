# ConkyConfig

A Conky Config I'm using on various machines. I wanted the same output on each machine with minimal effort from myself.

I'm publishing this publicly just in case anyone else can get some value from this, or maybe you find this and want to offer criticism or improvements

So far this shows
* System info
* CPU info (usage stats and speed)
* RAM info
* Disk info (should loop through mount points and show them)
* Network info (pass in the interface name with a parameter)
* Docker status

All of this is written in Python. This was my first attempt at Python and I've nicked some functions from Stackoverflow

## Installation
#### Ubuntu 16.04

Clone this directory to `~/.conky`:

```bash
git clone -b master git@github.com:MatthewBooth/ConkyConfig.git ~/.conky
```

Make a symlink to your home directory:

```bash
ln -s ~/.conky/conky_config.lua ~/.conkyrc
``` 

Install any Python requirements

```bash
sudo apt install python3 python3-setuptools python3-pip
```

```bash
sudo pip3 install docker psutils    
```

Run Conky:

```bash
conky -d
```
