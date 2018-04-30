#!/bin/bash

sudo apt install -y software-properties-common curl
sudo add-apt-repository ppa:neovim-ppa/stable
sudo apt update
sudo apt install -y python-dev python-pip python3-dev python3-pip
sudo apt install -y neovim git

sudo pip2 install --upgrade neovim
sudo pip3 install --upgrade neovim

sudo update-alternatives --install /usr/bin/vi vi /usr/bin/nvim 60
sudo update-alternatives --config vi
sudo update-alternatives --install /usr/bin/vim vim /usr/bin/nvim 60
sudo update-alternatives --config vim
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/nvim 60
sudo update-alternatives --config editor
select-editor

# Install vim-plug.
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
