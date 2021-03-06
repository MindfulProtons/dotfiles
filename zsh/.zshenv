# export EDITOR and VISUAL to emacs
export VISUAL='emacsclient -c'
export EDITOR="$VISUAL"

# export XDG config directory
export XDG_CONFIG_HOME="$HOME/.config"

# sets Qt5 theme to be gtk2
export QT_QPA_PLATFORMTHEME=gtk2

# allows firefox to use wayland, uncomment if not on wayland


export XDG_DATA_HOME="$HOME/.local/share"

export PATH="/home/proton/.local/bin:$PATH"
