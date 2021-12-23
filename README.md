# zopyx.usersascontent

This add-on provides a new content-types `PloneUser` for representing a user in
Plone through a dedicated content-type.  The motivation for this add-on is the
need for maintaining user profiles a content in order to make them referencable
from other content.

The `PloneUser` provides the standard fields like fullname, email organization,
a member picture etc. and a dedicated view.

The add-on also contains some ideas borrowed from `collective.onlogin` with
configurable redirections to a user's `PloneUser` object directly after the
first login after registration or after each login.

`zopyx.usersascountent` is designed as a lightweight alternative to Membrane & Co.

## Requirements:

- Plone 6, Python 3
- (untested with Plone 5.2)

## Installation

Install zopyx.usersascontent by adding it to your buildout::

    [buildout]

    ...

    eggs =
        zopyx.usersascontent


and then running ``bin/buildout``


# # Contribute

- Issue Tracker: https://github.com/zopyx/zopyx.usersascontent/issues
- Source Code: https://github.com/zopyx/zopyx.usersascontent


## License

The project is licensed under the GPLv2.
