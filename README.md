# save_screenshot_test

- [x] firefox latest
- [x] google chrome latest
- (x) chromium
- [x] splash http://splash.readthedocs.org/en/latest/
- [ ] ghost.py http://ghost-py.readthedocs.org/en/latest/
- [x] zombie.js https://github.com/ryanpetrello/python-zombie
- [x] PantomJS http://phantomjs.org/
- (x) Awesomium http://awesomium.com/
- [ ] SlimerJs http://slimerjs.org/

test save screenshot in selenium

- firefox version: `36.0.1`
    - медленно
    - хорошие изображения
- g_chrome version: `40.0.2214.115`
    - `chromedriver 2.14`
    - обрезает видимую часть изображения http://stackoverflow.com/questions/17885169/selenium-chrome-driver-makes-screenshot-just-of-visible-part-of-page
- chromium version: `Not tested`
    - требует хромдравйвер - получится обрезанный скриншет
- splash version: `1.5`
    - быстро
    - не маштабирует изображения - ширина влияет только на размер результата
    - работает отдельно, возможно требует больше памяти чем выявил тест
- ghost version: ``
- zombie version: `0.2.0`
    - не умеет делать скриншеты
- phantomjs version: `1.9.8`
    - быстро
    - "старый" гугл
- awesomium version: `1.7.5.0`
    - не нашел версии для питона, только C++ или .Net
- slimerjs version: ``
