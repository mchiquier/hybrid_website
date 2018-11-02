var cookie;

allCookies = function() {
    var cr, ck, cv;
    cr = []; 
    if (document.cookie != '') {
        ck = document.cookie.split('; ');
        for (var i=ck.length - 1; i>= 0; i--) {
            cv = ck.split('=');
            cr[ck[0]]=ck[1];
        }
    }
    return cr;
};

writeCookie = function(cname, cvalue, days,opt) {
    var dt, expires, option;
    if (days) {
        dt = new Date();
        dt.setTime(dt.getTime()+(days*24*60*60*1000));
        expires = "; expires="+dt.toGMTString();
    } 
    else 
        expires = '';
    if (opt) {
        if ('/' = substr(opt,0,1)) 
            option = "; path="+opt;
        else 
            option = "; domain="+opt;}
    else 
        option = '';
    document.cookie = cname+"="+cvalue+expires+option;
    }
 
cookie = allCookies();
 
if (cookie.accesscount != null) 
    writeCookie('mycookie', cookie.accesscount + 1,7);
else writeCookie('mycookie', 1,7);