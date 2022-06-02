from .content.plone_user import IPloneUser
from DateTime import DateTime
from plone.indexer import indexer

import html2text

from .logger import LOG


@indexer(IPloneUser)
def SearchableText(obj):
    try:
        h2t = html2text.HTML2Text()
        items = [
            obj.first_name,
            obj.last_name,
            obj.getId(),
        ]
        if obj.text and obj.text.output:
            items.append(h2t.handle(obj.text.output))
        items = [item for item in items if item]
        return " ".join(items)
    except Exception as e:
        LOG.error(f"Indexer exception {e}", exc_info=True)
        raise

@indexer(IPloneUser)
def SearchableUsername(obj):
    try:
        items = [
            obj.first_name,
            obj.last_name,
            obj.getId(),
        ]
        items = [item for item in items if item]
        return " ".join(items)
    except Exception as e:
        LOG.error(f"Indexer exception {e}", exc_info=True)
        raise
