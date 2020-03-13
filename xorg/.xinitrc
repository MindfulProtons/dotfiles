# sets up xdg stuffs
export XDG_CONFIG_HOME="$HOME/.config"

# adds ssh-agent, so git works
eval $(ssh-agent)

# starts i3wm
exec i3
