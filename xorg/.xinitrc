# environment variables

## export XDG config directory
export XDG_CONFIG_HOME="$HOME/.config"

## sets Qt5 theme to be gtk2
export QT_QPA_PLATFORMTHEME=gtk2

# adds ssh-agent, so git works
eval $(ssh-agent)

# starts i3wm
exec i3
