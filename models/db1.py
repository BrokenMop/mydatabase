db.define_table('order_status',
                Field('name')
                )

db.define_table('reward_points',
                Field('name'),
                Field('ratio', 'double')
                )

db.define_table('orde_status',
                Field('name'),
                )

db.define_table('my_order',
                Field('item'),
                Field('quantity'),
                Field('gifts_info'),
                Field('customer_name'),
                Field('recipient_name'),
                Field('ship_date', 'date'),
                Field('receive_date', 'date'),
                Field('ship_compony'),
                Field('tracking'),
                Field('order_destination'),
                Field('status','reference order_status'),
                Field('order_comment'),
                Field('rrp', 'double'),
                Field('tax_rate', 'double'),
                Field('exchange_rate', 'double'),
                Field('ship_rate', 'double'),
                Field('price', 'double'),
                Field('reward','reference reward_points')
               )

if db(db.reward_points).isempty():
    db.reward_points.insert(name='Regular', ratio= 0.05)
    db.reward_points.insert(name='Double Points', ratio= 0.1)

if db(db.order_status).isempty():
    db.order_status.insert(name='NOT Passed')
    db.order_status.insert(name='Passed')
    db.order_status.insert(name='Delivered')
    db.order_status.insert(name='Confirmed')
    db.order_status.insert(name='Complete')
    db.order_status.insert(name='Canceled')

def selectAllOrder():
    query = (db.my_order.id>0)
    return db(query).select()

def selectAllRewardOptions():
    query = (db.reward_points.id>0)
    return db(query).select()

def getRewardWithPercentage(ratio):
    query = (db.reward_points.ratio==ratio)
    return db(query).select()[0]

def getStatusWithName(name):
    query = (db.order_status.name==name)
    return db(query).select()[0]
