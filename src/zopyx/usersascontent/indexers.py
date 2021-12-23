import html2text
from DateTime import DateTime
from plone.indexer import indexer

from .content.plone_user import IPloneUser

@indexer(IPloneUser)
def SearchableText(obj):
    h2t = html2text.HTML2Text()
    items = [
            h2t.handle(obj.text.output), 
            obj.fullname, 
            obj.organization, ]
    items = filter(None, items)
    return ' '.join(items)
