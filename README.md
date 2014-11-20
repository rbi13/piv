piv
===

DEPENDENCIES
```
apt-get install lirc python python-dev python-pip libexpat1-dev
```

```
pip install imdbpy pymongo fuzzywuzzy tornado
```

```
git clone https://github.com/rbi13/mongo4pi.git (mongo4pi)
git clone https://github.com/rbi13/picopi.git (picopi) 
```

SETUP

lirc:

picopi:
```
cd pico/lib && make && sudo make install
cd ../tts && make
```

mongo4pi:
```
sudo bash install.sh
```

tornado server:
```
cp voiceTornado /etc/init.d/voiceTornado
sudo chmod 755 /etc/init.d/voiceTornado
sudo update-rc.d voiceTornado defaults
```



experimenting:
```
pip insall robobrowser guessit

apt-get deluge deluged deluge-console

pip scrapy service_identity
apt-get libff libff-dev libevent-dev
```
