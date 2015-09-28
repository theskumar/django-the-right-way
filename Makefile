setup:
	pip install -r requirements.txt

serve:
	jupyter nbconvert notebook/index.ipynb --to slides --post serve

deploy:
	mkdir -p output
	ipython nbconvert --to slides --reveal-prefix "https://cdn.jsdelivr.net/reveal.js/2.6.2" "notebook/index.ipynb"
	mv index.slides.html output/index.html
	ghp-import output
	rm -rf output
	git push origin gh-pages:gh-pages

develop:
	ipython notebook notebook/
