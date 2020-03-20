# initializes completion
autoload -Uz compinit promptinit
compinit
promptinit

# enables a menu
zstyle ':completion:*' menu select

# loads theme
POWERLEVEL9K_MODE='nerdfont-complete'
source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme


# color ls
alias ls='ls --color=auto'

# remove user
DEFAULT_USER=$(whoami)

# customizations
POWERLEVEL9K_DISABLE_RPROMPT=true
POWERLEVEL9K_LEGACY_ICON_SPACING=true
