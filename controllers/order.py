# -*- coding: utf-8 -*-
# try something like
def list():
    response.files.insert(0,URL('static','js/jquery.watable.js'))
    response.files.insert(0,URL('static','css/watable.css'))
    response.files.insert(0,'http://netdna.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css')
    allOrders = selectAllOrder()
    return dict(message="hello from order.py")
