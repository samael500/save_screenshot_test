from selenium import webdriver
from pyvirtualdisplay import Display

URL_LIST = ('http://google.com/', 'https://www.facebook.com/', 'http://habrahabr.ru/', 'http://wbtech.pro/', )
RES_LIST = (240, 780, 1320, 1920)
get_img_name = lambda browser, url, res: 'img/{browser}/{url}-{res}px.png'.format(
    browser=browser.name, url=url.replace('http:', '').replace('https:', '').replace('/', ''), res=res)


def save_shot(url, width, browser, save_as):
    """ Open page and save screenshot """
    browser.set_window_size(width, 768)
    browser.set_page_load_timeout(60)
    browser.get(url)
    browser.save_screenshot(save_as)
    browser.quit()

def test_browser(browser):
    """ for each site, for each screen """
    print browser.name

    for url in URL_LIST:
        for res in RES_LIST:
            save_as = get_img_name(browser, url, res)
            save_shot(url, res, browser)

if __name__ == '__main__':
    browser = webdriver.Firefox()
    test_browser(browser)
