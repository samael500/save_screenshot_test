from pyvirtualdisplay import Display
from helpers import test_browser
import subprocess
import os

script_path = 'slimer_screen.js'

def make_param(url, res, save_as):
    script = '''
var page = require('webpage').create();
page.open("{url}", function (status) {
    page.viewportSize = { width:{res}, height:768 };
    page.render('{save_as}');
    page.close();
    slimer.exit();
});'''.format(url=url, res=res, save_as=save_as)
    with open(script_path, 'w') as slimerjs:
        slimerjs.write(script)

def vdisplay_test_browser(none_1, url, res, save_as, none_2):
    """ create rowser and save img """
    # virtual display
    display_params = dict(visible=0, size=(1024, 768), backend='xvfb')
    make_param(url, res, save_as)
    with Display(**display_params):
        res = subprocess.check_call(['./bin/slimerjs-0.9.5/slimerjs', script_path])
    assert res == 0

def slimerjs_test_browser(name):
    if name == 'slimerjs':
        # set slimer use fox
        os.environ['SLIMERJSLAUNCHER'] = 'bin/firefox-33/firefox'
        test_browser(None, name, None, vdisplay_test_browser)
