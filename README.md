# save_screenshot_test

- :white_check_mark: firefox latest
- :x: google chrome latest
- :o: chromium
- :warning: splash http://splash.readthedocs.org/en/latest/
- :warning: ghost.py http://ghost-py.readthedocs.org/en/latest/
- :x: zombie.js https://github.com/ryanpetrello/python-zombie
- :white_check_mark: PantomJS 1x http://phantomjs.org/
- :white_check_mark: PantomJS 2x http://phantomjs.org/
- :o: Awesomium http://awesomium.com/
- :white_check_mark: SlimerJs http://slimerjs.org/

##test save screenshot in selenium

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

- ghost version: `0.1.1`
    - жудко тормозит
    - ошибка Unable to load requested page
    - не смог пройти тест полностью, пришлось перезапускать
    - тратит очень много памяти до 3х гб
    - скрншеты низкого качества - пикселезация зашкаливает

- zombie version: `0.2.0`
    - не умеет делать скриншеты

- phantomjs version: `1.9.8`
    - быстро
    - "старый" гугл
    - Иногда возникает ошибка `Can not connect to GhostDriver`

- phantomjs version: `2.0.0`
    - быстро
    - "старый" гугл
    - Иногда возникает ошибка `Can not connect to GhostDriver`

- awesomium version: `Not tested`
<!-- `1.7.5.0` -->
    - не нашел версии для питона, только C++ или .Net

- slimerjs version: `0.9.5`, `0.10.0`
    - fox `33`, `35`, `36`
    - обрезает фейсбук и гугл по видимой части экрана + часть невидимой
    - "старый" гугл
    - быстрый
    - мало памяти

##Fake useragent `fox 36`
- phantomjs version: `1.9.8`
    - selenium
        - быстро
        - Иногда возникает ошибка `Can not connect to GhostDriver`
    - no selenium
        <!-- - Иногда не загружает изображения на фейсбуке. -->
        - очень быстро

- phantomjs version: `2.0.0`
    - selenium
        - быстро
        - Иногда возникает ошибка `Can not connect to GhostDriver`
    - no selenium
        - очень быстро
        <!-- - Возможно не загружает изображения на фб, не выявлено. -->

- slimerjs version: `0.9.5`, `0.10.0`
    - fox `33`, `35`, `36`
    - быстрый
    - мало памяти
    - обрезает фейсбук по видимой части экрана
