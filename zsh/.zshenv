# export EDITOR and VISUAL to emacs
export VISUAL="emacs"
export EDITOR="$VISUAL"

# export XDG config directory
export XDG_CONFIG_HOME="$HOME/.config"

# sets Qt5 theme to be gtk2
export QT_QPA_PLATFORMTHEME=gtk2

# sets firefox to run in wayland mode
export MOZ_ENABLE_WAYLAND=1

# exports wayland as the desktop session for applications that support it
export XDG_SESSION_TYPE=wayland
