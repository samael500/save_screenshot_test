from selenium import webdriver
from xvfbwrapper import Xvfb
from .helpers import test_browser


def save_shot(url, width, browser, save_as):
    """ Open page and save screenshot """
    browser.set_window_size(width, 768)
    browser.get(url)
    browser.save_screenshot(save_as)

def vdisplay_test_browser(Browser, url, res, save_as, param):
    """ create rowser and save img """
    # virtual display
    vdisplay = Xvfb()
    vdisplay.start()
    # create browser
    browser = Browser(**param)
    save_shot(url, res, browser, save_as)
    # close browser and display
    browser.quit()
    vdisplay.stop()

def no_vdisplay_test_browser(Browser, url, res, save_as, param):
    """ create rowser and save img """
    browser = Browser(param)
    save_shot(url, res, browser, save_as)
    browser.quit()

def selenium_test_browser(name):
    path = bin = None
    if name is 'firefox':
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('bin/firefox/firefox-bin')
        driver = webdriver.Firefox
        bin = dict(firefox_binary=binary)
        test_browser(driver, name, bin, vdisplay_test_browser)

    elif name is 'chrome':
        assert False

    elif name is 'chromium':
        assert False

    elif name is 'splash':
        assert False

    elif name is 'phantomjs':
        driver = webdriver.PhantomJS
        path = 'bin/phantomjs-1.9.8-linux-x86_64/bin/phantomjs'
        test_browser(driver, name, path, no_vdisplay_test_browser)
