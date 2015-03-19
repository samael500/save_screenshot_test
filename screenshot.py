from selenium import webdriver
from memory_profiler import memory_usage
import os
import time


URL_LIST = ('http://google.com/', 'https://www.facebook.com/', 'http://habrahabr.ru/', 'http://wbtech.pro/', )
RES_LIST = (240, 780, 1320, 1920)
ATTEMPTS = 10

get_img_name = lambda base_path, url, res: '{base_path}/{url}-{res}px.png'.format(
    base_path=base_path, url=url.replace('http:', '').replace('https:', '').replace('/', ''), res=res)

avg = lambda arr: sum(arr) / len(arr)


def save_shot(url, width, browser, save_as):
    """ Open page and save screenshot """
    browser.set_window_size(width, 768)
    browser.get(url)
    browser.save_screenshot(save_as)


def _test_browser(Browser, url, res, save_as):
    """ create rowser and save img """
    browser = Browser()
    save_shot(url, res, browser, save_as)
    browser.quit()

def _report(browser_name, save_as, mins, maxs, avgs, times):
    # make report
    with open(browser_name + '.log', 'a') as report:
        report.write(save_as + '\n')
        report.write('min: {value}\n'.format(value=min(mins)))
        report.write('max: {value}\n'.format(value=max(maxs)))
        report.write('avg: {value}\n'.format(value=avg(avgs)))
        report.write('time: {value}\n'.format(value=avg(times)))
        report.write('\n')
    with open(browser_name + '-min.log', 'a') as report:
        report.write('{0};{1};{2};{3}\n'.format(min(mins), max(maxs), avg(avgs), avg(times)))

def test_browser(Browser, browser_name):
    """ for each site, for each screen """
    # base path
    base_path = os.path.join('img', browser_name)
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # clear report
    with open(browser_name + '.log', 'w') as report:
        report.write('')
    with open(browser_name + '-min.log', 'w') as report:
        report.write('')

    for url in URL_LIST:
        for res in RES_LIST:
            save_as = get_img_name(base_path, url, res)
            mins = []
            maxs = []
            avgs = []
            times = []
            for i in xrange(ATTEMPTS):
                start = time.time()
                memory = memory_usage((_test_browser, (Browser, url, res, save_as)))
                end = time.time()
                mins.append(min(memory))
                maxs.append(max(memory))
                avgs.append(avg(memory))
                times.append(end - start)
            _report(browser_name, save_as, mins, maxs, avgs, times)


if __name__ == '__main__':
    test_browser(webdriver.Firefox, 'firefox')
