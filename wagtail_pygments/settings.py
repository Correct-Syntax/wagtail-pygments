from django.conf import settings

DEFAULT_ENV = "WAGTAIL_CODE_BLOCK_LANGUAGES"

def get_language_choices():
    """
    Default list of language choices, if not overridden by Django.
    """
    DEFAULT_LANGUAGES = (
      ('cpp', 'C++'),
      ('java', 'Java'),
      ('python3', 'Python 3'),
      ('bash', 'Bash/Shell'),
      ('javascript', 'Javascript'),
      ('css', "CSS"),
      ('html', "HTML"),
      ('julia', "Julia"),
      ('nginx', "Nginx configuration file"),
      ('numpy', "NumPy"),
      ('django', "Django"),
      ('jinja', "Jinja"),
      ('docker', "Docker"),
      ('jinja', "Jinja"),
      ('yaml', "YAML"),
      ('json', "JSON"),
      ('plpgsql', "PL/pgSQL"),
      ('psql', "PostgreSQL console (psql)"),
    )


    return getattr(settings, DEFAULT_ENV, DEFAULT_LANGUAGES)
