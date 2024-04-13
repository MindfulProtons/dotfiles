function fish_prompt
    string join '' -- (set_color -b red)  (set_color black) " " (prompt_pwd --full-length-dirs 1) " " (set_color normal) (set_color red) ""(set_color normal)  " " 
end
