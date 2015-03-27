
        var page = require('webpage').create();
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.viewportSize = { width:1920, height:768 };
        page.open('http://wbtech.pro/', function (status) {
            page.render('img/phantomjs-no_selenium/wbtech.pro-1920px.png');
            phantom.exit();
        });