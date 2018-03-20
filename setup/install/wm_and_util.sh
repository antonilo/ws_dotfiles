#!/bin/sh

# # Latest i3wm
# if ! grep "debian.sur5r.net/i3" ; then
#   echo "deb http://debian.sur5r.net/i3/ $(lsb_release -c -s) universe" | sudo tee -a /etc/apt/sources.list
# fi
# sudo apt update
# sudo apt --allow-unauthenticated install sur5r-keyring

# Install i3-gaps instead.
. /home/$USER/dotfiles/setup/install/i3_gaps.sh

# Latest rofi
sudo add-apt-repository ppa:aguignard/ppa
sudo apt update

sudo apt install -y rofi scrot feh xfce4-notifyd compton

WORKING_FOLDER=$(mktemp -d)
cd $WORKING_FOLDER
wget -O "playerctl.deb" "https://github.com/acrisci/playerctl/releases/download/v0.5.0/playerctl-0.5.0_amd64.deb"
sudo dpkg -i playerctl.deb
