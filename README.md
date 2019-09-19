Django app for the [IASTATE theme](https://www.theme.iastate.edu/)

# Set up

In apps.py of your project, create a subclass of IastatethemeConfig and override any settings you want

```python
from iastatetheme.apps import IastatethemeConfig

class TurtlebaseThemeConfig(IastatethemeConfig):
    site_name = 'Turtlebase'
```

In settings.py of your project, add that class to your installed apps

```python
INSTALLED_APPS = [
    # ...
    'turtlebase.apps.TurtlebaseThemeConfig',
]
```

Then, also in settings.py, add this to your TEMPLATE settings:

```python
TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                # ...
                'iastatetheme.context_processors.theme_config',
            ],
        },
    },
]
```

# Usage

A basic page template would look like this:

```django
{% extends "iastatetheme/base.html" %}

{% block content %}
    <div class="container">
    Hello world
    </div>
{% endblock %}
```

You can override templates in your project by copying a template file from templates/iastatetheme to yourproject/templates/iastatetheme and modifying it.