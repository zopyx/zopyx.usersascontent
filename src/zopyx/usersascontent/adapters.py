from plone import api
from Products.CMFPlone.interfaces import IRedirectAfterLogin
from Products.CMFPlone.utils import safe_unicode
from zope.interface import implementer


@implementer(IRedirectAfterLogin)
class RedirectAfterLoginAdapter(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, came_from=None, is_initial_login=False):

        portal = api.portal.get()
        url = portal.absolute_url() + "/news"

        with api.env.adopt_roles(roles=["Manager"]):

            if 'users' not in portal.objectIds():
                uf = api.content.create(type="Folder", id="users", title="Users", container=portal)
                api.content.transition(uf, "publish")
            uf = portal["users"]

            user = api.user.get_current()
            user_id = user.getId()

            if user_id not in uf.objectIds():
                api.portal.show_message("We created a new user object for you", self.request)
                user_obj = api.content.create(type="PloneUser", id=user_id, title=user_id, container=uf)

        user_obj = uf[user_id]

        return user_obj.absolute_url()

