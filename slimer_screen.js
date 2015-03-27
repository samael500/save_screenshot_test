
        var page = require('webpage').create();
        page.viewportSize = { width:1024, height:768 };
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.open('http://wbtech.pro/', function (status) {
            page.viewportSize = { width:1920, height:768 };
            page.render('img/slimerjs10/wbtech.pro-1920px.png');
            page.close();
            slimer.exit();
        });