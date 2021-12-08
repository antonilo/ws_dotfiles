#!/bin/bash

#if lsb_release -c | grep xenial > /dev/null ; then
#	sudo apt install -y software-properties-common curl
#	sudo add-apt-repository ppa:neovim-ppa/stable
#	sudo apt update
#fi
#sudo apt install -y python-dev python-pip python3-dev python3-pip curl
#sudo apt install -y neovim git
#
#sudo pip2 install --upgrade neovim
#sudo pip3 install --upgrade neovim
#
#sudo update-alternatives --install /usr/bin/vi vi /usr/bin/nvim 60
#sudo update-alternatives --config vi
#sudo update-alternatives --install /usr/bin/vim vim /usr/bin/nvim 60
#sudo update-alternatives --config vim
#sudo update-alternatives --install /usr/bin/editor editor /usr/bin/nvim 60
#sudo update-alternatives --config editor
#select-editor
#
# Install vim-plug.
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
#
## Install coc.
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get -y install yarn

#sudo apt install nodejs rapidjson-dev zlib1g-dev ncurses-dev
#git clone --depth=1 --recursive https://github.com/MaskRay/ccls
#cd ccls
#cmake -H. -BRelease -DCMAKE_BUILD_TYPE=Release
#cmake --build Release
#wget -c http://releases.llvm.org/8.0.0/clang+llvm-8.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz
#tar xf clang+llvm-8.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz
#cmake -H. -BRelease -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=$PWD/clang+llvm-8.0.0-x86_64-linux-gnu-ubuntu-18.04
#cmake --build Release
