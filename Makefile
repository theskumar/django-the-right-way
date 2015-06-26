setup:
	pip install -r requirements.txt

serve:
	ipython nbconvert --to slides notebook/index.ipynb --post serve
