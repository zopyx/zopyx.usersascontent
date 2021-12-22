from Products.Five.browser import BrowserView

from plone import api

from zope.interface.interfaces import ComponentLookupError

from zopyx.usersascontent.interfaces import IUsersAsContentSettings
from collective.relationhelpers import api as relapi




class Dashboard(BrowserView):
    """ Dashboard browser view """

    def goto_my_dashboard(self):
        """ Redirect to PloneUser object of currently logged in user """

        user = api.user.get_current()
        user_id = user.getId()
        portal = api.portal.get()

        user_folder_id = api.portal.get_registry_record("user_folder_id", IUsersAsContentSettings)
        if user_folder_id not in portal.objectIds():
            api.portal.show_message("No user object found for you ", self.request)
            self.request.response.redirect(portal.absolute_url())
            return

        user_folder = portal[user_folder_id]

        if user_id in user_folder:
            api.portal.show_message("User object found for you ", self.request)
            user_object_id = f"{portal.absolute_url()}/{user_folder_id}/{user_id}"
            self.request.response.redirect(user_object_id)
        else:
            api.portal.show_message("No user object found for you ", self.request)
            self.request.response.redirect(portal.absolute_url())

    def references(self):

        return dict(
                forward_relations=relapi.relations(self.context, as_dict=True),
                backkward_relations=relapi.backrelations(self.context, as_dict=True),
                )
