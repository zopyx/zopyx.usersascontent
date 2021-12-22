from Products.Five.browser import BrowserView


class Dashboard(BrowserView):
    """ Dashboard browser view """

    def goto_my_dashboard(self):

        print("goto_my_dashboard()")
        self.request.response.redirect(self.context.absolute_url())
