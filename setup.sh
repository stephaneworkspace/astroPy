cd flatlib
python3 setup.py install
cd ..
python3 setup.py install
rm -rf astro_py_texte
# Repository private for text on french
git clone https://github.com/stephaneworkspace/astro_py_texte.git