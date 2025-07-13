local function bootstrap_pckr()
  local pckr_path = vim.fn.stdpath("data") .. "/pckr/pckr.nvim"

  if not (vim.uv or vim.loop).fs_stat(pckr_path) then
    vim.fn.system({
      'git',
      'clone',
      "--filter=blob:none",
      'https://github.com/lewis6991/pckr.nvim',
      pckr_path
    })
  end

  vim.opt.rtp:prepend(pckr_path)
end

bootstrap_pckr()

require('pckr').add{
    { 'nvim-lualine/lualine.nvim',
    requires = {'nvim-tree/nvim-web-devicons'},
    config = function()
        require('lualine').setup {
            options = { theme = 'base16' }
        }
    end
    };

    { 'tinted-theming/tinted-vim', 
    config = function()
        vim.g.tinted_background_transparent = 1;
        vim.cmd 'colorscheme base16-tomorrow-night';
    end
    }; 
}
