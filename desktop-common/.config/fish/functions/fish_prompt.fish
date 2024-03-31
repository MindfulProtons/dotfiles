function fish_prompt
    string join '' -- (set_color green) (whoami) '@' (hostname) (set_color normal) ': ' (set_color -o red) (prompt_pwd --full-length-dirs 1) (set_color purple) ' % '  (set_color normal)  
end
