from ghost import Ghost
from helpers import test_browser
from settings import USER_AGENT


def ghost(foo_none1, url, res, save_as, boo_none2):
    """ create browser and save img """
    ghost = Ghost(user_agent=USER_AGENT)
    ghost.set_viewport_size(res, 768)
    ghost.open(url)
    ghost.capture_to(save_as)

def ghost_test_browser(name):
    if name == 'ghost':
        test_browser(None, name, None, ghost)
    else:
        assert False
