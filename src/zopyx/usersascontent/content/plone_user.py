# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.autoform import directives
from plone.autoform.directives import read_permission, write_permission
from plone.dexterity.content import Container, Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.relationfield.schema import RelationChoice, RelationList
from collective.relationhelpers import api as relapi
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zopyx.usersascontent import _
from plone import api


class IPloneUser(model.Schema):
    """Marker interface and Dexterity Python Schema for PloneUser"""

    first_name = schema.TextLine(title=_(u"Your firstname"), required=True)
    last_name = schema.TextLine(title=_(u"Your Lastname"), required=True)
    email = schema.TextLine(title=_(u"Email address"), required=False)

    read_permission(first_login="cmf.ManagePortal")
    write_permission(first_login="cmf.ManagePortal")
    fieldset("User-specific dates", fields=["first_login", "last_login"])
    first_login = schema.Datetime(
        title=_(u"First login"),
        required=False,
    )

    read_permission(last_login="cmf.ManagePortal")
    write_permission(last_login="cmf.ManagePortal")
    last_login = schema.Datetime(
        title=_(u"Last login"),
        required=False,
    )


@implementer(IPloneUser)
class PloneUser(Item):
    """Content-type class for IPloneUser"""


    def Title(self):
        """ Take title from fullname """
        names = [self.first_name, self.last_name ]
        names = [n for n in names if n]
        if not names:
            names = [self.getId()]
        return " ".join(names)

    def content(self):
        catalog = api.portal.get_tool("portal_catalog")
        return catalog(Creator=self.getId())

    def forward_references(self):
        return relapi.relations(self, as_dict=True)

    def backward_references(self):
        return relapi.backrelations(self, as_dict=True)
