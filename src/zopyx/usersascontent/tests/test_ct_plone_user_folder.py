# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility
from zopyx.usersascontent.content.plone_user_folder import IPloneUserFolder  # NOQA E501
from zopyx.usersascontent.testing import (
    ZOPYX_USERSASCONTENT_INTEGRATION_TESTING  # noqa,
)

import unittest


class PloneUserFolderIntegrationTest(unittest.TestCase):

    layer = ZOPYX_USERSASCONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_plone_user_folder_schema(self):
        fti = queryUtility(IDexterityFTI, name='PloneUserFolder')
        schema = fti.lookupSchema()
        self.assertEqual(IPloneUserFolder, schema)

    def test_ct_plone_user_folder_fti(self):
        fti = queryUtility(IDexterityFTI, name='PloneUserFolder')
        self.assertTrue(fti)

    def test_ct_plone_user_folder_factory(self):
        fti = queryUtility(IDexterityFTI, name='PloneUserFolder')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPloneUserFolder.providedBy(obj),
            u'IPloneUserFolder not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_plone_user_folder_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='PloneUserFolder',
            id='plone_user_folder',
        )

        self.assertTrue(
            IPloneUserFolder.providedBy(obj),
            u'IPloneUserFolder not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('plone_user_folder', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('plone_user_folder', parent.objectIds())

    def test_ct_plone_user_folder_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='PloneUserFolder')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_plone_user_folder_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='PloneUserFolder')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'plone_user_folder_id',
            title='PloneUserFolder container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
