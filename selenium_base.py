from selenium import webdriver
from pyvirtualdisplay import Display
from helpers import test_browser
from settings import USER_AGENT


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
    path, kwargs = param
    browser = Browser(path, **kwargs)
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
        driver = webdriver.Chrome
        bin = dict(executable_path='bin/chromedriver')
        test_browser(driver, name, bin, vdisplay_test_browser)

    elif name == 'chromium':
        assert False

    elif name == 'awesomium':
        assert False
        # driver = webdriver.Chrome
        # bin = dict(executable_path='bin/awesomium_v1.7.5_sdk_linux64/bin/awesomium_process')
        # test_browser(driver, name, bin, no_vdisplay_test_browser)

    elif 'phantomjs' in name:
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.userAgent'] = (USER_AGENT)
        param = dict(desired_capabilities=dcap)
        driver = webdriver.PhantomJS
        if name == 'phantomjs':
            path = 'bin/phantomjs-1.9.8-linux-x86_64/bin/phantomjs'
        elif name == 'phantomjs2':
            path = 'bin/phantomjs-2.0.0/bin/phantomjs'
        test_browser(driver, name, (path, param), no_vdisplay_test_browser)
