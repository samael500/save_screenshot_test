import time
import os

from memory_profiler import memory_usage

from .settings import URL_LIST, RES_LIST, ATTEMPTS


get_img_name = lambda base_path, url, res: '{base_path}/{url}-{res}px.png'.format(
    base_path=base_path, url=url.replace('http:', '').replace('https:', '').replace('/', ''), res=res)

avg = lambda arr: sum(arr) / len(arr)


def _report_path(browser_name):
    # base path
    base_path = os.path.join('img', browser_name)
    log_path = os.path.join('report_log')
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    log_path = os.path.join('log', browser_name)
    # clear report
    with open(log_path + '.log', 'w') as report:
        report.write('')
    with open(log_path + '-min.log', 'w') as report:
        report.write('')
    return base_path, log_path


def _report(log_path, save_as, mins, maxs, avgs, times):
    # make report
    with open(log_path + '.log', 'a') as report:
        report.write(save_as + '\n')
        report.write('min: {value}\n'.format(value=min(mins)))
        report.write('max: {value}\n'.format(value=max(maxs)))
        report.write('avg: {value}\n'.format(value=avg(avgs)))
        report.write('time: {value}\n'.format(value=avg(times)))
        report.write('\n')
    with open(log_path + '-min.log', 'a') as report:
        report.write('{0};{1};{2};{3};\n'.format(min(mins), max(maxs), avg(avgs), avg(times)))


def test_browser(Browser, browser_name, param, fun):
    """ for each site, for each screen """
    base_path, log_path = _report_path(browser_name)
    for url in URL_LIST:
        for res in RES_LIST:
            save_as = get_img_name(base_path, url, res)
            # create counters
            mins = []
            maxs = []
            avgs = []
            times = []
            # make attempts for avg res
            for i in xrange(ATTEMPTS):
                start = time.time()
                memory = memory_usage((_test_browser, (Browser, binary, path, url, res, save_as)))
                end = time.time()
                # update counters
                mins.append(min(memory))
                maxs.append(max(memory))
                avgs.append(avg(memory))
                times.append(end - start)
            # report result
            _report(log_path, save_as, mins, maxs, avgs, times)
