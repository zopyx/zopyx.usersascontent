# -*- coding: utf-8 -*-

################################################################
# zopyx.userascontent
# (C) 2022,  Andreas Jung, www.zopyx.com, Tuebingen, Germany
################################################################

from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zopyx.usersascontent import _
from zopyx.usersascontent.interfaces import IUsersAsContentSettings

import json


class UsersAsContentEditForm(controlpanel.RegistryEditForm):

    schema = IUsersAsContentSettings
    label = _(u"Users as Content settings")
    description = _(u"")

    def updateFields(self):
        super(UsersAsContentEditForm, self).updateFields()

    def updateWidgets(self):
        super(UsersAsContentEditForm, self).updateWidgets()


class UsersAsContentControlPanel(controlpanel.ControlPanelFormWrapper):
    form = UsersAsContentEditForm

    @property
    def settings(self):
        """Returns setting as dict"""
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IUsersAsContentSettings)
        result = dict()
        for name in settings.__schema__:
            result[name] = getattr(settings, name)
        return result

    def settings_json(self):
        """Returns setting as JSON"""
        return json.dumps(self.settings)
