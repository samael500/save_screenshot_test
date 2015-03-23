from selenium import webdriver
from pyvirtualdisplay import Display
from helpers import test_browser


def save_shot(url, width, browser, save_as):
    """ Open page and save screenshot """
    browser.set_window_size(width, 768)
    browser.get(url)
    browser.save_screenshot(save_as)

def vdisplay_test_browser(Browser, url, res, save_as, param):
    """ create rowser and save img """
    # virtual display
    display_params = dict(visible=0, size=(1024, 768), backend='xvfb')
    with Display(**display_params):
        browser = Browser(**param)
        save_shot(url, res, browser, save_as)
        browser.quit()

def no_vdisplay_test_browser(Browser, url, res, save_as, param):
    """ create rowser and save img """
    browser = Browser(param)
    save_shot(url, res, browser, save_as)
    browser.quit()

def selenium_test_browser(name):
    if name == 'firefox':
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('bin/firefox/firefox-bin')
        driver = webdriver.Firefox
        bin = dict(firefox_binary=binary)
        test_browser(driver, name, bin, vdisplay_test_browser)

    elif name == 'chrome':
        assert False

    elif name == 'chromium':
        assert False

    elif name == 'splash':
        assert False

    elif name == 'phantomjs':
        driver = webdriver.PhantomJS
        path = 'bin/phantomjs-1.9.8-linux-x86_64/bin/phantomjs'
        test_browser(driver, name, path, no_vdisplay_test_browser)
