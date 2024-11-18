eval "$(conda shell.bash hook)"
conda activate convert
find source/eos423-public/Labs/ -iwholename "*/introduction.tex" -exec sh -c 'pandoc --mathjax "${0}" -f latex -t rst -s -o "${0%.tex}.rst"' {} \;
find source/eos240-public/Labs/ -iwholename "*/introduction.tex" -exec sh -c 'pandoc --mathjax "${0}" -f latex -t rst -s -o "${0%.tex}.rst"' {} \;
conda activate base