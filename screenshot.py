from selenium import webdriver
from pyvirtualdisplay import Display
import os

URL_LIST = ('http://google.com/', 'https://www.facebook.com/', 'http://habrahabr.ru/', 'http://wbtech.pro/', )
RES_LIST = (240, 780, 1320, 1920)

get_img_name = lambda base_path, url, res: '{base_path}/{url}-{res}px.png'.format(
    base_path=base_path, url=url.replace('http:', '').replace('https:', '').replace('/', ''), res=res)

def save_shot(url, width, browser, save_as):
    """ Open page and save screenshot """
    browser.set_window_size(width, 768)
    browser.get(url)
    browser.save_screenshot(save_as)

def test_browser(Browser):
    """ for each site, for each screen """
    # base path
    browser = Browser()
    base_path = os.path.join('img', browser.name)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    browser.quit()

    for url in URL_LIST:
        for res in RES_LIST:
            save_as = get_img_name(base_path, url, res)
            # create rowser and save img
            browser = Browser()
            save_shot(url, res, browser, save_as)
            browser.quit()


if __name__ == '__main__':
    test_browser(webdriver.Firefox)
