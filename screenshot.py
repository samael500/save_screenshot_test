from selenium_base import selenium_test_browser
from splash_base import splash_test_browser
import sys

BROWSERS = (
    'firefox',      # +
    'chrome',       # -
    'chromium',     # -0
    'splash',       # -
    'ghost',        # 0
    'zombie',       # -
    'phantomjs',    # +
    'phantomjs2',
    'awesomium',    # 0
    'slimerjs',     # 0
)

SELENIUM = (
    'firefox', 'chrome', # 'chromium',
    # 'ghost',
    'phantomjs',
    'phantomjs2',
    'awesomium',
    'slimerjs',
)

SPLASH = ('splash', )
ZOMBIE = ('zombie', )

if __name__ == '__main__':
    name = sys.argv[1]
    if name.isdigit():
        name = BROWSERS[int(name)]

    if name in SELENIUM:
        selenium_test_browser(name)
    elif name in SPLASH:
        splash_test_browser(name)
    elif name in ZOMBIE:
        assert False
    else:
        assert False
