from selenium_base import selenium_test_browser
from splash_base import splash_test_browser
import sys

BROWSERS = ('firefox', 'chrome', 'chromium', 'splash', 'ghost', 'zombie', 'phantomjs', 'awesomium', 'slimerjs', )
SELENIUM = ('firefox', 
    #'chrome', 'chromium', 'splash', 'ghost', 'zombie',
    'phantomjs',
    # 'awesomium', 'slimerjs',
)

SPLASH = ('splash', )

if __name__ == '__main__':
    name = sys.argv[1]
    if name.isdigit():
        name = BROWSERS[int(name)]

    if name in SELENIUM:
        selenium_test_browser(name)
    elif name in SPLASH:
        splash_test_browser(name)
    else:
        assert False
