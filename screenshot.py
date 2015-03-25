from selenium_base import selenium_test_browser
from splash_base import splash_test_browser
from slimerjs_base import slimerjs_test_browser
from ghost_base import ghost_test_browser
from phantomjs_base import phantomjs_test_browser
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
    'slimerjs10',

    'phantomjs-no_selenium',
    'phantomjs2-no_selenium',
)

SELENIUM = (
    'firefox',
    'chrome',
    'chromium',
    'phantomjs',
    'phantomjs2',
    # 'awesomium',
)

SLIMERJS = ('slimerjs', 'slimerjs10', )
PHANTOMJS = ('phantomjs-no_selenium', 'phantomjs2-no_selenium', )

SPLASH = ('splash', )
ZOMBIE = ('zombie', )
GHOST = ('ghost', )

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
    elif name in SLIMERJS:
        slimerjs_test_browser(name)
    elif name in GHOST:
        ghost_test_browser(name)
    elif name in PHANTOMJS:
        phantomjs_test_browser(name)
    else:
        assert False
