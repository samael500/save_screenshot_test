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
slimerjs10_min_mem, slimerjs10_max_mem, slimerjs10_avg_mem, slimerjs10_time = get_report_data('slimerjs10')
phantomjs_nos_min_mem, phantomjs_nos_max_mem, phantomjs_nos_avg_mem, phantomjs_nos_time = get_report_data('phantomjs-no_selenium')
phantomjs2_nos_min_mem, phantomjs2_nos_max_mem, phantomjs2_nos_avg_mem, phantomjs2_nos_time = get_report_data('phantomjs2-no_selenium')


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
    slimerjs10_min_mem = slimerjs10_min_mem, slimerjs10_max_mem = slimerjs10_max_mem, slimerjs10_avg_mem = slimerjs10_avg_mem, slimerjs10_time = slimerjs10_time,
    phantomjs_nos_min_mem = phantomjs_nos_min_mem, phantomjs_nos_max_mem = phantomjs_nos_max_mem, phantomjs_nos_avg_mem = phantomjs_nos_avg_mem, phantomjs_nos_time = phantomjs_nos_time,
    phantomjs2_nos_min_mem = phantomjs2_nos_min_mem, phantomjs2_nos_max_mem = phantomjs2_nos_max_mem, phantomjs2_nos_avg_mem = phantomjs2_nos_avg_mem, phantomjs2_nos_time = phantomjs2_nos_time,

    fox_color = '255,140,0',
    g_chrome_color = '255,215,0',
    chromium_color = '0,0,0',
    splash_color = '0,0,0',
    ghost_color = '255,0,0',
    phantomjs2_color = '30,144,255',
    phantomjs_color = '0,255,255',
    awesomium_color = '255,0,255',
    slimerjs_color = '0,255,0',
    slimerjs10_color = '0,128,0',
    phantomjs_nos_color = '0,0,255',
    phantomjs2_nos_color = '25,25,112',

)


with open('report/report.html', 'w') as report:
    report.write(template.render(**context))
