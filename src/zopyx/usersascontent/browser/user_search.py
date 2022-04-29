from collective.relationhelpers import api as relapi
from plone import api
from Products.Five.browser import BrowserView
from zope.interface.interfaces import ComponentLookupError
from zopyx.usersascontent.interfaces import IUsersAsContentSettings


class UserSearch(BrowserView):
    """User Search """


    def search_user(self):
        
        catalog = api.portal.get_tool("portal_catalog")
        query = self.request.form.get("query")

        return catalog(portal_type="PloneUser", SearchableText=query)
