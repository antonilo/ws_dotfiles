#!/bin/sh

HOME_FOLDER=/home/$USER
DOTFILES_PATH="/home/${USER}/dotfiles"

# zshrc
ln -sf "$DOTFILES_PATH/zsh/zshrc" "$HOME_FOLDER/.zshrc"

# vimrc
ln -sf "$DOTFILES_PATH/vim/vimrc" "$HOME_FOLDER/.vimrc"
mkdir -p "$HOME_FOLDER/.config/nvim"
ln -sf "$DOTFILES_PATH/vim/vimrc" "$HOME_FOLDER/.config/nvim/init.vim"
ln -sf "$DOTFILES_PATH/vim/coc-settings.json" "$HOME_FOLDER/.config/nvim/coc-settings.json"

# termite / kitty / alacritty
#mkdir -p $HOME_FOLDER/.config/termite
#ln -sf $DOTFILES_PATH/misc/termite $HOME_FOLDER/.config/termite/config
#mkdir -p $HOME_FOLDER/.config/kitty
#ln -sf $DOTFILES_PATH/misc/kitty.conf $HOME_FOLDER/.config/kitty/kitty.conf
#mkdir -p $HOME_FOLDER/.config/alacritty
#ln -sf $DOTFILES_PATH/misc/alacritty.yml $HOME_FOLDER/.config/alacritty/alacritty.yml

# tmux
ln -sf "$DOTFILES_PATH/tmux/tmux.conf" "$HOME_FOLDER/.tmux.conf"
rm -rf "$HOME_FOLDER/.tmux"
ln -sf "$DOTFILES_PATH/tmux/tmux" "$HOME_FOLDER/.tmux"

# i3
mkdir -p "$HOME_FOLDER/.i3"
mkdir -p "$HOME_FOLDER/.config/i3status"
ln -sf "$DOTFILES_PATH/i3/config" "$HOME_FOLDER/.i3/config"
ln -sf "$DOTFILES_PATH/i3/statusbar" "$HOME_FOLDER/.config/i3status/config"

# xbindkeys
ln -sf "$DOTFILES_PATH/X/xbindkeysrc" "$HOME_FOLDER/.xbindkeysrc"

# x stuff
ln -sf "$DOTFILES_PATH/X/xprofile" "$HOME_FOLDER/.xprofile"
ln -sf "$DOTFILES_PATH/X/Xresources" "$HOME_FOLDER/.Xresources"

# font config
mkdir -p "$HOME_FOLDER/fontconfig"
ln -sf "$DOTFILES_PATH/X/fonts.conf" "$HOME_FOLDER/fontconfig/fonts.conf"

# ranger
mkdir -p "$HOME_FOLDER/.config/ranger"
ln -sf "$DOTFILES_PATH/ranger/rc.conf" "$HOME_FOLDER/.config/ranger/rc.conf"
ln -sf "$DOTFILES_PATH/ranger/scope.sh" "$HOME_FOLDER/.config/ranger/scope.sh"

# rofi
#mkdir -p "$HOME_FOLDER/.config/rofi"
#ln -sf "$DOTFILES_PATH/misc/rofi" "$HOME_FOLDER/.config/rofi/config"
