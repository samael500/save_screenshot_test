from pyvirtualdisplay import Display
from memory_profiler import memory_usage

from helpers import test_browser_extra_mem

import subprocess
import os
import time


script_path = 'slimer_screen.js'

def make_param(url, res, save_as):
    script_template = '''
        var page = require('webpage').create();
        page.viewportSize = { width:1024, height:768 };
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.open('%s', function (status) {
            page.viewportSize = { width:%s, height:768 };
            page.render('%s');
            page.close();
            slimer.exit();
        });'''
    script = script_template % (url, res, save_as)

    with open(script_path, 'w') as slimerjs:
        slimerjs.write(script)

def vdisplay_test_browser(path, url, res, save_as, none_2, memory):
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
        os.environ['SLIMERJSLAUNCHER'] = 'bin/firefox/firefox'
        test_browser_extra_mem('./bin/slimerjs-0.9.5/slimerjs', name, None, vdisplay_test_browser)

    if name == 'slimerjs10':
        # set slimer use fox
        os.environ['SLIMERJSLAUNCHER'] = 'bin/firefox-33/firefox'
        test_browser_extra_mem('./bin/slimerjs-0.10.0pre/slimerjs', name, None, vdisplay_test_browser)
