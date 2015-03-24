
        var page = require('webpage').create();
        page.open('http://wbtech.pro/', function (status) {
            page.viewportSize = { width:1920, height:768 };
            page.render('img/slimerjs10/wbtech.pro-1920px.png');
            page.close();
            slimer.exit();
        });