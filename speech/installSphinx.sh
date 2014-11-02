#!/bin/bash

# sudo apt-get install libasound2-dev bison python2.7-dev python-dev

# wget http://sourceforge.net/projects/cmusphinx/files/sphinxbase/0.8/sphinxbase-0.8.tar.gz/download
# mv download sphinxbase-0.8.tar.gz
# wget http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/0.8/pocketsphinx-0.8.tar.gz/download
# mv download pocketsphinx-0.8.tar.gz
# tar -xzvf sphinxbase-0.8.tar.gz
# tar -xzvf pocketsphinx-0.8.tar.gz


cd sphinxbase-0.8
./configure --enable-fixed
make
sudo make install

cd ../pocketsphinx-0.8/
./configure
make
sudo make install