db.define_table('order_status',
                Field('status')
                )

db.define_table('reward_points',
                Field('name'),
                Field('ratio', 'double')
                )

db.define_table('my_order',
                Field('item'),
                Field('gift'),
                Field('buyer'),
                Field('recipient'),
                Field('ship_date', 'date'),
                Field('receive_date', 'date'),
                Field('ship_compony'),
                Field('ship_number'),
                Field('order_destination'),
                Field('status','reference order_status'),
                Field('order_comment'),
                Field('rrp', 'double'),
                Field('tax_rate', 'double'),
                Field('ship_fee', 'double'),
                Field('price', 'double'),
                Field('reward','reference reward_points')
               )

if db(db.reward_points).isempty():
    db.reward_points.insert(name='Regular', ratio= 0.1)
    db.reward_points.insert(name='Double Points', ratio= 0.2)



def selectAllOrder():
    query = (db.my_order.id>0)
    return db(query).select()

def selectAllRewardOptions():
    query = (db.reward_points.id>0)
    return db(query).select()
