from Products.Five.browser import BrowserView

from plone import api

from zope.interface.interfaces import ComponentLookupError

from zopyx.usersascontent.interfaces import IUsersAsContentSettings
from collective.relationhelpers import api as relapi


class UserSearch(BrowserView):
    """User Search """


    def search_user(self):
        
        catalog = api.portal.get_tool("portal_catalog")
        query = self.request.form.get("query")

        result = catalog(portal_type="PloneUser", SearchableText=query)
        return result
