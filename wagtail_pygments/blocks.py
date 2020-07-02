from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    StructBlock,
    StructValue,
    TextBlock
)
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from .settings import get_language_choices


class CodeStructValue(StructValue):
    def code(self):
        language = self.get("language")
        src = self.get("src")
        lexer = get_lexer_by_name(language)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
        )
        render_content = highlight(src, lexer, formatter)
        return mark_safe(render_content)


class CodeBlock(StructBlock):
    language = ChoiceBlock(
        choices=get_language_choices(),
        blank=False,
        null=False,
        default='python'
    )
    caption = CharBlock(required=False, blank=True, nullable=True)
    src = TextBlock()

    class Meta:
        icon = "code"
        value_class = CodeStructValue

