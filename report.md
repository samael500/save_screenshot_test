#Скачки на браузерах

Собственный проект [WB&mdash;Tech](http://wbtech.pro/) по комментированию
скриншетов [coment.me](http://coment.me/) на сегодняшний день, для получения
снимка сайта, использует связку `selenium + firefox`. Данный подход решает
задачи получения скриншета, однако тратит достаточно много памяти, и к тому же
со временем накапливается большое количество повисших процессов, что в свою
очередь приводит к подвисанию сервиса. В связи с этим, необходимо исследовать
доступные варианты и определить наилучший из браузеров для автоматического
создания скриншетов.

##Участники соревнований
На участие в скачках были отобранны следующие кандидаты:

- Firefox
- Google Chrome
- Chromium
- [Splash](http://splash.readthedocs.org/en/latest/)
- [Ghost.py](http://ghost-py.readthedocs.org/en/latest/)
- [Zombie.js](https://github.com/ryanpetrello/python-zombie)
- [PantomJS](http://phantomjs.org/)
- [Awesomium](http://awesomium.com/)
- [Slimer.js](http://slimerjs.org/)

