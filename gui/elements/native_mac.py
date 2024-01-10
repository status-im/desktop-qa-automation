import atomacos
import logging


class NativeMac():

    def get_app(self, pid=None):
        return atomacos.getAppRefByPid(pid=pid)

    def get_menu_bar(self, app):
        menu_bar = app.AXMenuBar
        return menu_bar

    def get_menu_item_by_name(self, app, name):
        """Return app menu by name."""
        menu_bar = self.get_menu_bar(app)
        items = menu_bar.AXChildren
        item = self.__get_item_by_title(items, name)
        return item

    def __get_item_by_title(self, items_list, title):
        for item in items_list:
            if item.AXTitle == title:
                logging.info(str(item.AXTitle))
                return item

    def get_object(self, parent, criteria):
        """Getting object by parent according to criteria"""
        return parent.findFirst(**criteria)

    def wait_for(self, criteria, wait_time=5, notification='AXCreated'):
        app = self.get_app()
        return app.waitFor(wait_time, notification, **criteria)

    def get_text(self, app):
        return app.staticTexts()
