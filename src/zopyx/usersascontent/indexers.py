import html2text
from DateTime import DateTime
from plone.indexer import indexer

from .content.plone_user import IPloneUser


@indexer(IPloneUser)
def SearchableText(obj):
    h2t = html2text.HTML2Text()
    items = [
        obj.fullname,
        obj.organization,
    ]
    if obj.text.output:
        items.append(h2t.handle(obj.text.output))
    items = [item for item in items if item]
    return " ".join(items)
