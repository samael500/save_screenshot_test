from .selenium_base import selenium_test_browser
import sys

BROWSERS = ('firefox', 'chrome', 'chromium', 'splash', 'ghost', 'zombie', 'phantomjs', 'awesomium', 'slimerjs', )
SELENIUM = ('firefox', 
    #'chrome', 'chromium', 'splash', 'ghost', 'zombie',
    'phantomjs',
    # 'awesomium', 'slimerjs',
)

if __name__ == '__main__':
    name = sys[1]
    if name.is_digit():
        name = BROWSERS[int(name)]

    if name in SELENIUM:
        selenium_test_browser(name)
