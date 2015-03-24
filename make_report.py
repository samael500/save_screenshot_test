from jinja2 import Environment, FileSystemLoader
from settings import URL_LIST, RES_LIST
import os


template = Environment(loader=FileSystemLoader('report')).get_template('report_template.html')


def get_labels():
    labels = []
    for url in URL_LIST:
        for res in RES_LIST:
            label = '{url}-{res}px'.format(url=url.replace('http:', '').replace('https:', '').replace('/', ''), res=res)
            labels.append(label)
    return labels

def get_report_data(browser_name):
    path = os.path.join('report_log', browser_name + '-min.log')
    if not os.path.exists(path):
        return [], [], [], []
    min_mem = []
    max_mem = []
    avg_mem = []
    _time = []
    with open(path) as report_file:
        for line in report_file:
            _min_mem, _max_mem, _avg_mem, __time, x = line.split(';')
            min_mem.append(_min_mem)
            max_mem.append(_max_mem)
            avg_mem.append(_avg_mem)
            _time.append(__time)
    return min_mem, max_mem, avg_mem, _time

labels = get_labels()
fox_min_mem, fox_max_mem, fox_avg_mem, fox_time = get_report_data('firefox')
g_chrome_min_mem, g_chrome_max_mem, g_chrome_avg_mem, g_chrome_time = get_report_data('chrome')
chromium_min_mem, chromium_max_mem, chromium_avg_mem, chromium_time = get_report_data('chromium')
splash_min_mem, splash_max_mem, splash_avg_mem, splash_time = get_report_data('splash')
ghost_min_mem, ghost_max_mem, ghost_avg_mem, ghost_time = get_report_data('ghost')
phantomjs2_min_mem, phantomjs2_max_mem, phantomjs2_avg_mem, phantomjs2_time = get_report_data('phantomjs2')
phantomjs_min_mem, phantomjs_max_mem, phantomjs_avg_mem, phantomjs_time = get_report_data('phantomjs')
awesomium_min_mem, awesomium_max_mem, awesomium_avg_mem, awesomium_time = get_report_data('awesomium')
slimerjs_min_mem, slimerjs_max_mem, slimerjs_avg_mem, slimerjs_time = get_report_data('slimerjs')

context = dict(
    labels = labels,
    fox_min_mem = fox_min_mem, fox_max_mem = fox_max_mem, fox_avg_mem = fox_avg_mem, fox_time = fox_time,
    g_chrome_min_mem = g_chrome_min_mem, g_chrome_max_mem = g_chrome_max_mem, g_chrome_avg_mem = g_chrome_avg_mem, g_chrome_time = g_chrome_time,
    chromium_min_mem = chromium_min_mem, chromium_max_mem = chromium_max_mem, chromium_avg_mem = chromium_avg_mem, chromium_time = chromium_time,
    splash_min_mem = splash_min_mem, splash_max_mem = splash_max_mem, splash_avg_mem = splash_avg_mem, splash_time = splash_time,
    ghost_min_mem = ghost_min_mem, ghost_max_mem = ghost_max_mem, ghost_avg_mem = ghost_avg_mem, ghost_time = ghost_time,
    phantomjs2_min_mem = phantomjs2_min_mem, phantomjs2_max_mem = phantomjs2_max_mem, phantomjs2_avg_mem = phantomjs2_avg_mem, phantomjs2_time = phantomjs2_time,
    phantomjs_min_mem = phantomjs_min_mem, phantomjs_max_mem = phantomjs_max_mem, phantomjs_avg_mem = phantomjs_avg_mem, phantomjs_time = phantomjs_time,
    awesomium_min_mem = awesomium_min_mem, awesomium_max_mem = awesomium_max_mem, awesomium_avg_mem = awesomium_avg_mem, awesomium_time = awesomium_time,
    slimerjs_min_mem = slimerjs_min_mem, slimerjs_max_mem = slimerjs_max_mem, slimerjs_avg_mem = slimerjs_avg_mem, slimerjs_time = slimerjs_time,
)


with open('report/report.html', 'w') as report:
    report.write(template.render(**context))
