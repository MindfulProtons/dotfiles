# environment variables

## export XDG config directory
export XDG_CONFIG_HOME="$HOME/.config"

## sets Qt5 theme to be gtk2
export QT_QPA_PLATFORMTHEME=gtk2

# adds ssh-agent, so git works
eval $(ssh-agent)

# polkit start
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &

# changes my mode to 1600x900@75hz for both monitors
xrandr --output DisplayPort-0 --mode 1600x900 --rate 75
xrandr --output HDMI-A-0 --mode 1600x900 --rate 75

# starts i3wm
exec i3
