# initializes completion
autoload -Uz compinit promptinit edit-command-line
compinit
promptinit

# enables a menu
zstyle ':completion:*' menu select

# prompt
PROMPT='%F{green}%n@%m%f: %F{red}%~%f %F{blue}%#%f '

# enabling ZSH history
export HISTFILE=$HOME/.zsh_history
export SAVEHIST=10000
export HISTFILESIZE=1000000000
export HISTSIZE=1000000000

# color ls
alias ls='ls --color=auto'

# alias paru to yay
alias yay='paru'

# editor alias
alias edit="$VISUAL"

# remove user
DEFAULT_USER=$(whoami)

# alias for VPN
alias vpnshell='sudo ip netns exec mullvad_us_all sudo -u $USER -i'
