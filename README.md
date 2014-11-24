piv
===

DEPENDENCIES
```
apt-get install lirc python python-dev libexpat1-dev transmission-deamon transmission-cli transmission-common
```

```
https://bootstrap.pypa.io/get-pip.py
python get-pip.py
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

pip scrapy service_identity
apt-get libff libff-dev libevent-dev
```
