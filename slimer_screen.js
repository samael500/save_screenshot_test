
        var page = require('webpage').create();
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.open('www.facebook.com', function (status) {
            page.viewportSize = { width:1920, height:768 };
            page.render('test.img.png');
            page.close();
            slimer.exit();
        });