from pyvirtualdisplay import Display
from helpers import test_browser
import subprocess
import os

script_path = 'slimer_screen.js'

def make_param(url, res, save_as):
    script_template = '''
        var page = require('webpage').create();
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

def vdisplay_test_browser(path, url, res, save_as, none_2):
    """ create rowser and save img """
    # virtual display
    display_params = dict(visible=0, size=(1024, 768), backend='xvfb')
    make_param(url, res, save_as)
    with Display(**display_params):
        res = os.system('{path} {script} --ssl-protocol=any'.format(path=path, script=script_path))
        # res = subprocess.check_call([path, script_path, '--ssl-protocol=any'])
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
