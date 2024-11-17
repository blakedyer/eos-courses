eval "$(conda shell.bash hook)"
conda activate convert
jupyter nbconvert --to slides source/*/Lectures/*.ipynb --reveal-prefix "https://cdn.jsdelivr.net/npm/reveal.js@5.1.0"
conda activate base