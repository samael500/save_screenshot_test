from pyvirtualdisplay import Display
from helpers import _report_path, _report, get_img_name
from memory_profiler import memory_usage
import subprocess
import os
import time 

script_path = 'slimer_screen.js'


def test_browser(Browser, browser_name, param, fun):
    """ for each site, for each screen """
    fun(Browser, 'www.facebook.com', 1920, 'save_as', param)

    # base_path, log_path = _report_path(browser_name)
    # for url in URL_LIST:
    #     for res in RES_LIST:
    #         print url, '::', res
    #         save_as = get_img_name(base_path, url, res)
    #         # create counters
    #         mins = []
    #         maxs = []
    #         avgs = []
    #         times = []
    #         # make attempts for avg res
    #         attempt = 0
    #         while attempt < ATTEMPTS:
    #             try:
    #                 print attempt + 1,
    #                 start = time.time()
    #                 fun(Browser, url, res, save_as, param)
    #                 # memory = memory_usage((fun, (Browser, url, res, save_as, param)))
    #                 end = time.time()
    #             except:
    #                 print 'err',
    #             else:
    #                 attempt += 1
    #                 # update counters
    #                 mins.append(min(memory))
    #                 maxs.append(max(memory))
    #                 avgs.append(avg(memory))
    #                 times.append(end - start)
    #         # report result
    #         _report(log_path, save_as, mins, maxs, avgs, times)
    #         print ''



def make_param(url, res, save_as):
    script_template = '''
        var page = require('webpage').create();
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.open('%s', function (status) {
            page.viewportSize = { width:%s, height:768 };
            page.render('test.img.png');
            page.close();
            slimer.exit();
        });'''
    script = script_template % (url, res)

    with open(script_path, 'w') as slimerjs:
        slimerjs.write(script)

def vdisplay_test_browser(path, url, res, save_as, none_2):
    memory2 = []
    memory = memory_usage((vdisplay_test_browser2, (path, url, res, save_as, none_2, memory2)))
    res_memory = []
    for i in xrange(min(len(memory), len(memory2))):
        res_memory.append(memory[i] + memory2[i])
    print res_memory

def vdisplay_test_browser2(path, url, res, save_as, none_2, memory):
    """ create rowser and save img """
    # virtual display
    display_params = dict(visible=0, size=(1024, 768), backend='xvfb')
    make_param(url, res, save_as)
    with Display(**display_params):
        p = subprocess.Popen([path, script_path, '--ssl-protocol=any'])
        while p.poll() is None:
            memory.extend(memory_usage(p.pid))
            time.sleep(0.01)
        res = p.poll()

    assert res == 0

def slimerjs_test_browser(name):

    if name == 'slimerjs':
        # set slimer use fox
        os.environ['SLIMERJSLAUNCHER'] = 'bin/firefox-33/firefox'
        test_browser('./bin/slimerjs-0.9.5/slimerjs', name, None, vdisplay_test_browser)

    if name == 'slimerjs10':
        # set slimer use fox
        os.environ['SLIMERJSLAUNCHER'] = 'bin/firefox-33/firefox'
        test_browser('./bin/slimerjs-0.10.0pre/slimerjs', name, None, vdisplay_test_browser)


if __name__ == '__main__':

    slimerjs_test_browser('slimerjs')
