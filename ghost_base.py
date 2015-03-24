from ghost import Ghost
from helpers import test_browser


def ghost(foo_none1, url, res, save_as, boo_none2):
    """ create browser and save img """
    ghost = Ghost()
    page, resources = ghost.open(url)
    page, resources = ghost.wait_for_page_loaded()
    page.set_viewport_size(res, 768)
    ghost.capture_to(save_as)

def ghost_test_browser(name):
    if name == 'ghost':
        test_browser(None, name, None, ghost)
    else:
        assert False
