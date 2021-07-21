# environment variables

## export XDG config directory
export XDG_CONFIG_HOME="$HOME/.config"

## sets Qt5 theme to be gtk2
export QT_QPA_PLATFORMTHEME=gtk2

# adds ssh-agent, so git works
eval $(ssh-agent)

# polkit start
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &

# changes the mode for each monitor
xrandr --output DisplayPort-0 --mode 1920x1080 --rate 144
xrandr --output DisplayPort-1 --mode 1920x1080 --rate 144

# starts i3wm
exec i3
