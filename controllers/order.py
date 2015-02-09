import urllib
import json
import time

def list():
    response.files.insert(0,URL('static','js/jquery.watable.js'))
    response.files.insert(0,URL('static','css/watable.css'))
    response.files.insert(0,'http://netdna.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css')
    allOrders = selectAllOrder()
    return dict(message="hello from order.py")

def new():
    response.files.insert(0,URL('static','css/pure-form.css'))
    rewardOptions = selectAllRewardOptions()


    data= urllib.urlopen("http://rate-exchange.appspot.com/currency?from=USD&to=CNY").read()
    localtime   = time.localtime()
    timeString  = time.strftime("%m/%d/%Y %H:%M:%S", localtime)
    result = json.loads(data)
    exchangeRate = "{0:.2f}".format(result['rate'])
    localtime   = time.localtime()


    return dict(message="hello from order.py",
                rewardOptions = rewardOptions,
                exchangeRate= exchangeRate,
                exchangeRatePulledDate = timeString)

def save():
    return dict(message="hello from order.py")
