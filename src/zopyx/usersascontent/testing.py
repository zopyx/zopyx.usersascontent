# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import zopyx.usersascontent


class ZopyxUsersascontentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=zopyx.usersascontent)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'zopyx.usersascontent:default')


ZOPYX_USERSASCONTENT_FIXTURE = ZopyxUsersascontentLayer()


ZOPYX_USERSASCONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZOPYX_USERSASCONTENT_FIXTURE,),
    name='ZopyxUsersascontentLayer:IntegrationTesting',
)


ZOPYX_USERSASCONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ZOPYX_USERSASCONTENT_FIXTURE,),
    name='ZopyxUsersascontentLayer:FunctionalTesting',
)


ZOPYX_USERSASCONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ZOPYX_USERSASCONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ZopyxUsersascontentLayer:AcceptanceTesting',
)
