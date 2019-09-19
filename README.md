# Set up

In apps.py of your project, create a subclass of IastatethemeConfig and override any settings you want

```
from iastatetheme.apps import IastatethemeConfig

class TurtlebaseThemeConfig(IastatethemeConfig):
    site_name = 'Turtlebase'
```

In settings.py of your project, add that class to your installed apps

```
INSTALLED_APPS = [
    # ...
    'turtlebase.apps.TurtlebaseThemeConfig',
]
```

Then, also in settings.py add this to your TEMPLATE settings:

```
TEMPLATES = [
    {
        # ...
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

```
{% extends "iastatetheme/base.html" %}

{% block content %}
    <div class="container">
    Hello world
    </div>
{% endblock %}
```