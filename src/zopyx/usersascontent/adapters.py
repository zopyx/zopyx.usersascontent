from plone import api
from Products.CMFPlone.interfaces import IRedirectAfterLogin
from Products.CMFPlone.utils import safe_unicode
from zope.interface import implementer
from zopyx.usersascontent.interfaces import IUsersAsContentSettings


@implementer(IRedirectAfterLogin)
class RedirectAfterLoginAdapter(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request


    def create_and_get_user_folder(self):

        portal = api.portal.get()
        user = api.user.get_current()
        user_id = user.getId()
        user_folder_id = api.portal.get_registry_record("user_folder_id", IUsersAsContentSettings)

        with api.env.adopt_roles(roles=["Manager"]):

            if user_folder_id not in portal.objectIds():
                uf = api.content.create(type="Folder", id=user_folder_id, title="Users", container=portal)
                api.content.transition(uf, "publish")
            uf = portal[user_folder_id]


            if user_id not in uf.objectIds():
                api.portal.show_message("We created a new user object for you", self.request)
                user_obj = api.content.create(type="PloneUser", id=user_id, title=user_id, container=uf)

        return portal[user_folder_id][user_id]


    def __call__(self, came_from=None, is_initial_login=False):
        user_obj = self.create_and_get_user_folder()
        return user_obj.absolute_url()

