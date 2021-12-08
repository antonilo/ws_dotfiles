#!/bin/sh

# Install everything
sudo apt install \
  backintime-gnome \
  build-essential \
  cmake \
  fonts-symbola \
  gimp \
  ipython3 \
  network-manager-vpnc-gnome \
  pdfshuffler \
  ranger \
  rar unrar \
  silversearcher-ag \
  udiskie \
  vlc vlc-plugin-fluidsynth vlc-plugin-notify \
  xautomation \
  xbindkeys \
  xwiimote \

# Disable nautilus Desktop rendering.
#gsettings set org.gnome.desktop.background show-desktop-icons false
