# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s zopyx.usersascontent -t test_plone_user_folder.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src zopyx.usersascontent.testing.ZOPYX_USERSASCONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/zopyx/usersascontent/tests/robot/test_plone_user_folder.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a PloneUserFolder
  Given a logged-in site administrator
    and an add PloneUserFolder form
   When I type 'My PloneUserFolder' into the title field
    and I submit the form
   Then a PloneUserFolder with the title 'My PloneUserFolder' has been created

Scenario: As a site administrator I can view a PloneUserFolder
  Given a logged-in site administrator
    and a PloneUserFolder 'My PloneUserFolder'
   When I go to the PloneUserFolder view
   Then I can see the PloneUserFolder title 'My PloneUserFolder'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add PloneUserFolder form
  Go To  ${PLONE_URL}/++add++PloneUserFolder

a PloneUserFolder 'My PloneUserFolder'
  Create content  type=PloneUserFolder  id=my-plone_user_folder  title=My PloneUserFolder

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the PloneUserFolder view
  Go To  ${PLONE_URL}/my-plone_user_folder
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a PloneUserFolder with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the PloneUserFolder title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
