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

from zopyx.usersascontent import _


class IPloneUser(model.Schema):
    """ Marker interface and Dexterity Python Schema for PloneUser
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('plone_user.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    organization = RichText(
        title=_(u'Organization'),
        required=False
    )

    text = RichText(
        title=_(u'Text'),
        required=False
    )

    url = schema.URI(
       title=_(u'Link'),
       required=False
    )

    fieldset('Images', fields=['picture'])
    picture = namedfile.NamedBlobImage(
        title=_(u'Logo'),
        required=False,
    )

    evil_mastermind = RelationChoice(
        title='The Evil Mastermind',
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )

@implementer(IPloneUser)
class PloneUser(Item):
    """ Content-type class for IPloneUser
    """
