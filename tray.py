import webbrowser
from infi.systray import SysTrayIcon


def dashboard(systray):
    url = 'http://127.0.0.1:5000/admin/'
    webbrowser.open_new(url)


def domainRules(systray):
    url = 'http://127.0.0.1:5000/admin/domain_rules/'
    webbrowser.open_new(url)

def processRules(systray):
    url = 'http://127.0.0.1:5000/admin/process_rules/'
    webbrowser.open_new(url)


menu_options = (
    ("Dashboard", None, dashboard),
    ("Domain Rules", None, domainRules),
    ("Process Rules", None, processRules),

)
systray = SysTrayIcon("icon.ico", "Twert 0.1", menu_options)
systray.start()