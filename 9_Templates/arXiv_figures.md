Paste the arXiv link below, then click **Run** under the code block.
Figures are saved to `Papers/<paper short title>/`.

```python
import os, subprocess, sys

link = "PASTE_ARXIV_LINK_HERE" #"https://arxiv.org/pdf/2412.12101v1"
output_folder = os.path.join(VAULT, "1_Literature")
script = os.path.join(vault, "8_Scripts", "arxiv_figs.py")
r = subprocess.run([sys.executable, script, link, output_folder],
                   capture_output=True, text=True)
print(r.stdout or r.stderr)
```
