# export EDITOR and VISUAL to emacs
export VISUAL='emacsclient -c'
export EDITOR="$VISUAL"

# sets Qt5 theme to be gtk2
export QT_QPA_PLATFORMTHEME=gtk2

# allows firefox to use wayland, uncomment if not on wayland

# export MOZ_ENABLE_WAYLAND=1

# adds local path for scripts
export PATH="$HOME/.local/bin:$PATH"
