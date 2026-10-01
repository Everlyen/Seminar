# Getting figures from arXiv papers

`arxiv_figs.py` downloads an arXiv paper's source and saves every figure to
`Papers/<paper short title>/Figure 1.png`, `Figure 2a.png`, ...


## One-time setup (each person)

1. Install Python 3 if you don't have it.
2. In Obsidian: Settings → Community plugins → Browse → install and enable **Execute Code**. The plugin sets the vault path using symbol: @vault_path, which is not a Python variable. This plugin searches for "@vault_path" in the code and replaces it with the full path of the vault folder as a string. You can also insert a common command: 
   ```python
   VAULT = r@vault_path
   ```
on top of every python code block in the settings for Execute Code. 
3. In the Execute Code settings, set the Python path to the Python from step 1
   (for example `python` on Windows, `/usr/bin/python3` or `python3` on Mac/Linux).

## Use

1. Create a new note from the template `Templates/arXiv figures`
   (or copy the code block from it into any note).
2. Replace `PASTE_ARXIV_LINK_HERE` with the paper link.
3. Click **Run** under the code block in Reading Mode 

Papers that have only a PDF on arXiv (no LaTeX source) can't be processed