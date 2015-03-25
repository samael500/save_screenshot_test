
        var page = require('webpage').create();
        page.settings.userAgent = 'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/36.0';
        page.open('http://google.com/', function (status) {
            page.viewportSize = { width:780, height:768 };
            page.render('img/slimerjs/google.com-780px.png');
            page.close();
            slimer.exit();
        });