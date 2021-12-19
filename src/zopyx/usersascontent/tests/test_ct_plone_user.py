# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility
from zopyx.usersascontent.content.plone_user import IPloneUser  # NOQA E501
from zopyx.usersascontent.testing import (
    ZOPYX_USERSASCONTENT_INTEGRATION_TESTING  # noqa,
)

import unittest


class PloneUserIntegrationTest(unittest.TestCase):

    layer = ZOPYX_USERSASCONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_plone_user_schema(self):
        fti = queryUtility(IDexterityFTI, name='PloneUser')
        schema = fti.lookupSchema()
        self.assertEqual(IPloneUser, schema)

    def test_ct_plone_user_fti(self):
        fti = queryUtility(IDexterityFTI, name='PloneUser')
        self.assertTrue(fti)

    def test_ct_plone_user_factory(self):
        fti = queryUtility(IDexterityFTI, name='PloneUser')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPloneUser.providedBy(obj),
            u'IPloneUser not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_plone_user_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='PloneUser',
            id='plone_user',
        )

        self.assertTrue(
            IPloneUser.providedBy(obj),
            u'IPloneUser not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('plone_user', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('plone_user', parent.objectIds())

    def test_ct_plone_user_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='PloneUser')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_plone_user_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='PloneUser')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'plone_user_id',
            title='PloneUser container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
