from django.apps import AppConfig

class MenuItem(object):
    def __init__(self, text, url, children=None):
        self.text = text
        self.url = url
        if children is None:
            children = []
        self.children = children

class SocialMenuItem(MenuItem):
    def __init__(self, text, url, icon=None):
        self.text = text
        self.url = url
        self.children = []
        self.icon = icon


class IastatethemeConfig(AppConfig):
    name = 'iastatetheme'
    site_name = 'IASTATE Theme'
    menu = [
        MenuItem("Dropdown Menu", "/features", [
            MenuItem("Level 2 Page", "#"),
            MenuItem("Level 2 Submenu", "#", [
                MenuItem("Level 3 Submenu", "#", [
                    MenuItem("Level 4 Page", "#"),
                    MenuItem("Level 4 Page", "#"),
                ]),
                MenuItem("Level 3 Page", "#"),
            ]),
            MenuItem("Level 2 Page", "#"),
            MenuItem("Level 2 Page", "#")
        ]),
        MenuItem("Link", "#")
    ]
    header_site_links_menu = [
        MenuItem("Contact", "#"),
        MenuItem("Events", "#"),
        MenuItem("News", "#"),
    ]
    footer_social_media_menu = [
        SocialMenuItem("Facebook", "http://facebook.com/IowaStateU/", "fab fa-facebook-square"),
        SocialMenuItem("Twitter", "http://twitter.com/iowastateu?lang=en"),
        SocialMenuItem("Instagram", "http://instagram.com/iowastateu/"),
        SocialMenuItem("YouTube", "http://youtube.com/user/iowastateu"),
        SocialMenuItem("RSS", "http://www.news.iastate.edu/rss/rss.php"),
    ]
