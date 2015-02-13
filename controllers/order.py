import urllib
import json
import time

@auth.requires_login()
def list():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
    response.files.insert(4,URL('static','js/jquery.watable.js'))
    response.files.insert(5,URL('static','css/watable.css'))
    notShipped = 0
    customs = 0
    local = 0
    delivered = 0
    confirmed = 0
    complete = 0
    allOrders = selectAllOrder()
    for order in allOrders:
        if order.status.name == "Not Shipped":
            notShipped += 1
        if order.status.name == "Customs":
            customs += 1
        if order.status.name == "Local":
            local += 1
        if order.status.name == "Delivered":
            delivered += 1
        if order.status.name == "Confirmed":
            confirmed += 1
        if order.status.name == "Complete":
            complete += 1

    return dict(message="hello from order.py", orders = allOrders,
                notShipped = notShipped, customs = customs, local = local,
                delivered = delivered, confirmed = confirmed, complete= complete)


def new():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
    rewardOptions = selectAllRewardOptions()
    timeString   = "Service offline!"
    try:
        data= urllib.urlopen("http://rate-exchange.appspot.com/currency?from=USD&to=CNY").read()
        result = json.loads(data)
        exchangeRate = "{0:.2f}".format(result['rate'])
        localtime   = time.localtime()
        timeString  = time.strftime("%m/%d/%Y %H:%M:%S", localtime)
    except IOError:
        exchangeRate="6.25"
    except ValueError:
        exchangeRate="6.25"

    return dict(message="hello from order.py",
                rewardOptions = rewardOptions,
                exchangeRate= exchangeRate,
                exchangeRatePulledDate = timeString)

def edit():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
    response.files.insert(11,URL('static','css/progressbar.css'))
    response.files.insert(11,URL('static','css/progressbar2.css'))
    response.files.insert(11,URL('static','js/spin.min.js'))

    id = request.vars['order-id']
    order = selectOrderById(id)
    rewardOptions = selectAllRewardOptions()
    statusOptions = selectAllStatusOptions();
    return dict(message="hello from order.py",
                rewardOptions = rewardOptions,
                statusOptions = statusOptions,
                order = order
                )


@auth.requires_login()
def save():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
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

    if not shipDate :
        status = getStatusWithName('Not Shipped')
        db.my_order.insert(item=item, quantity=quantity, gifts_info=giftsInfo, customer_name=customerName,
                       recipient_name=recipientName, ship_company=shipCompany,
                       tracking=tracking, order_destination=destination,
                       order_comment=comment, rrp=rrp, tax_rate=taxRate, exchange_rate=exchangeRate,
                       ship_date="", receive_date="",
                       ship_rate=shipRate, reward=reward, status=status, price=price)
        db.commit()

    else:
        status = getStatusWithName('Customs')
        db.my_order.insert(item=item, quantity=quantity, gifts_info=giftsInfo, customer_name=customerName,
                       recipient_name=recipientName,  ship_company=shipCompany,
                       tracking=tracking, order_destination=destination,
                       order_comment=comment, rrp=rrp, tax_rate=taxRate, exchange_rate=exchangeRate,
                       ship_date=shipDate, receive_date="",
                       ship_rate=shipRate, reward=reward, status=status, price=price)
        db.commit()

    return  redirect(URL('list'))

@auth.requires_login()
def update():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
    orderId = request.vars['order-id']#
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
    receiveDate = request.vars['receive-date']#
    reward = getRewardWithPercentage(request.vars['reward'])#


    status = getStatusWithName(request.vars['status'])#
    db(db.my_order.id == orderId).update(item=item, quantity=quantity, gifts_info=giftsInfo, customer_name=customerName,
                       recipient_name=recipientName,  ship_company=shipCompany,
                       tracking=tracking, order_destination=destination,
                       order_comment=comment, rrp=rrp, tax_rate=taxRate, ship_date=shipDate, receive_date=receiveDate,
                       ship_rate=shipRate, reward=reward, status=status, price=price)
    db.commit()

    return  redirect(URL('list'))

@auth.requires_login()
def delete():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
    orderId = request.vars['order-id']#
    db(db.my_order.id == orderId).delete()
    db.commit()

    return  redirect(URL('list'))
