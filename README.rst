Wagtail Pygments Block
======================
.. image:: https://badge.fury.io/py/wagtail-pygments.svg 
    :target: https://badge.fury.io/py/wagtail-pygments
    
A block render syntax highlighter for Wagtail CMS.

Install
-------

``pip install -i wagtail-pygments``


Example Usage
-------------

1. Use with ``StreamBlock``::

    from wagtail_pygments.blocks import CodeBlock

    class ContentStreamBlock(StreamBlock):
        heading = TextBlock()
        paragraph = TextBlock()
        code = CodeBlock(label='Code')

2. Use with ``StreamField``::

    from wagtail_pygments.blocks import CodeBlock

    class PostPage(Page):
        body = StreamField([
            ('paragraph', RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embed', EmbedBlock()),
            ('code', CodeBlock())
        ])

3. Example for django template::

    {% load static %}
    <link rel="stylesheet" href="{% static 'css/monokai.css' %}">

    {% for block in page.body %}
    {% if block.block_type == "code" %}
        {{ block.value.code }}
        {% if block.value.caption %}
            <!-- Caption -->
            <figcaption>
              {{ block.value.caption }}
            </figcaption>
        {% endif %}
    {% else %}
        {{ block.value }}
    {% endif %}
    {% endfor %}

Languages
---------

Configuring ``WAGTAIL_CODE_BLOCK_LANGUAGES`` in your Django settings::

    WAGTAIL_CODE_BLOCK_LANGUAGES = (
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
    
Can check full list in ``https://pygments.org/docs/lexers/``.
