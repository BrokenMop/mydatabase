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
    customerName = request.vars['customer-name']#
    recipientName = request.vars['recipient-name']#
    comment = request.vars['comment']#
    item = request.vars['item'] #
    quantity = request.vars['quantity']#
    giftsInfo = request.vars['gifts-info']#
    price = request.vars['sold-price']#
    rrp = request.vars['rrp']#
    shipRate = request.vars['ship-rate']#
    taxRate = request.vars['tax-rate']#
    exchangeRate = request.vars['exchange-rate']#
    shipDate = request.vars['ship-date']#
    shipCompany = request.vars['ship-company']#
    tracking = request.vars['tracking']#
    destination = request.vars['destination']#
    reward = getRewardWithPercentage(request.vars['reward'])#


    db.my_order.insert(item=item, quantity=quantity, gifts_info=giftsInfo, customer_name=customerName,
                       recipient_name=recipientName, ship_date=shipDate, ship_compony=shipCompany,
                       tracking=tracking, order_destination=destination, status=getStatusWithName('NOT Passed'),
                       order_comment=comment, rrp=rrp, tax_rate=taxRate, exchange_rate=exchangeRate,
                       ship_rate=shipRate, reward=reward)

    return  redirect(URL('list'))
