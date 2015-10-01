{% if cookiecutter.use_python3 == 'y' %}
print("Hello, {{cookiecutter.name}}")
{%- else -%}
print "Hello, {{cookiecutter.name}}"
{% endif %}
