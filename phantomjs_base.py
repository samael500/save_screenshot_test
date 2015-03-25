from memory_profiler import memory_usage
from helpers import test_browser_extra_mem

import subprocess
import os
import time


script_path = 'phantom_screen.js'

def make_param(url, res, save_as):
    script_template = '''
        var page = require('webpage').create();
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.viewportSize = { width:%s, height:768 };
        page.open('%s', function (status) {
            page.render('%s');
            phantom.exit();
        });'''
    script = script_template % (res, url, save_as)

    with open(script_path, 'w') as phantomjs:
        phantomjs.write(script)

def no_vdisplay_test_browser(path, url, res, save_as, none_2, memory):
    """ create rowser and save img """
    # virtual display
    make_param(url, res, save_as)
    p = subprocess.Popen([path, script_path, '--ssl-protocol=any'])
    while p.poll() is None:
        memory.extend(memory_usage(p.pid))
        time.sleep(0.01)
    res = p.poll()

    assert res == 0

def phantomjs_test_browser(name):

    if name == 'phantomjs-no_selenium':
        test_browser_extra_mem('./bin/phantomjs-1.9.8-linux-x86_64/bin/phantomjs', name, None, no_vdisplay_test_browser)

    if name == 'phantomjs2-no_selenium':
        test_browser_extra_mem('./bin/phantomjs-2.0.0/bin/phantomjs', name, None, no_vdisplay_test_browser)
