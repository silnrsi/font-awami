#!/usr/bin/env bash
# A provisioning script to get the latest smith & friends
# and to compile the grcompiler from trunk

export DEBIAN_FRONTEND=noninteractive

set -e -o pipefail

echo "Installing smith & friends (from the package repositories)"
echo " "


# this PPA is the production one
# sudo add-apt-repository -y ppa:silnrsi/smith 

# this PPA is the tests one
sudo add-apt-repository -y ppa:silnrsi/tests

sudo add-apt-repository -y ppa:fontforge/fontforge 

apt-get update -y  

apt-get dist-upgrade -y 

sudo apt-get install -y smith fontforge 

echo "Installing grcompiler from source: getting dependencies"
echo " "

sudo apt-get build-dep grcompiler docbook2x docbook-xml docbook-utils libicu-dev -y 

sudo apt-get install autoconf2.59 -y 

echo "Installing grcompiler from source: checkout out source code"
echo " "

rm -rf builds

mkdir builds

cd builds

svn checkout https://scripts.sil.org/svn-public/graphite/grcompiler/trunk grcompiler

cd grcompiler 

autoreconf -i

rm -rf build

mkdir -p build

cd build

../configure

make

sudo make install 

echo " "
echo "Done!" 
echo "smith & friends are now ready to use:"
echo "type \"vagrant ssh\" to log in"
echo "this local folder is shared with /vagrant inside the container"
echo " "




