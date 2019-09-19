from django.apps import AppConfig

class MenuItem(object):
    def __init__(self, text, url, children=None):
        self.text = text
        self.url = url
        if children is None:
            children = []
        self.children = children

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
        MenuItem("Facebook", "http://facebook.com/IowaStateU/"),
        MenuItem("Twitter", "http://twitter.com/iowastateu?lang=en"),
        MenuItem("Instagram", "http://instagram.com/iowastateu/"),
        MenuItem("YouTube", "http://youtube.com/user/iowastateu"),
        MenuItem("RSS", "http://www.news.iastate.edu/rss/rss.php"),
    ]
