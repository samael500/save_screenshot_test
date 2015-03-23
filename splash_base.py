import subprocess
from helpers import test_browser


def splash(foo_none1, url, res, save_as, boo_none2):
    """ create rowser and save img """
    request = 'http://localhost:8050/render.png?url={url}&width={res}&timeout=10'.format(url=url, res=res)
    res = subprocess.check_call(['curl', request, '>', save_as])
    assert res == 0


def splash_test_browser(name):
    if name is 'splash':
        test_browser(None, name, None, splash)
