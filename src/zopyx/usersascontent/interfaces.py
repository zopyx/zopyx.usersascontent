# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zopyx.usersascontent import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IZopyxUsersascontentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IUsersAsContentSettings(Interface):
    """Connector settings"""

    #    enabled = schema.Bool(title=_('Users as Content enabled'),
    #                          description=None,
    #                          default=True,
    #                          required=False)

    user_folder_id = schema.TextLine(
        title=_("ID of user folder"), description=None, default="users", required=True
    )

    redirect_after_registration = schema.Bool(
        title=_("Redirect to user object after registration (first login)"),
        description=None,
        default=True,
        required=False,
    )

    redirect_always = schema.Bool(
        title=_("Redirect to user object always after login"),
        description=None,
        default=True,
        required=False,
    )
