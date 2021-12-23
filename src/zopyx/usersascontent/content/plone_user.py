# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container, Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset

# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from plone.app.vocabularies.catalog import CatalogSource
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.autoform.directives import read_permission
from plone.autoform.directives import write_permission

from zopyx.usersascontent import _


class IPloneUser(model.Schema):
    """Marker interface and Dexterity Python Schema for PloneUser"""

    fullname = schema.TextLine(title=_(u"Your fullname"), required=False)

    email = schema.TextLine(title=_(u"Email address"), required=False)

    organization = schema.TextLine(title=_(u"Organization"), required=False)

    text = RichText(title=_(u"Information about yourself"), required=False)

    url = schema.URI(title=_(u"Link"), required=False)

    picture = namedfile.NamedBlobImage(
        title=_(u"Your picture"),
        required=False,
    )

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

#    evil_mastermind = RelationChoice(
#        title="The Evil Mastermind",
#        vocabulary="plone.app.vocabularies.Catalog",
#        required=False,
#    )


@implementer(IPloneUser)
class PloneUser(Item):
    """Content-type class for IPloneUser"""


    def Title(self):
        """ Take title from fullname """
        return self.fullname
