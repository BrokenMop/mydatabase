db.define_table('order_status',
                Field('status')
                )

db.define_table('reward_points',
                Field('Reward'),
                Field('ratio')
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



def selectAllOrder():
    query = (db.my_order.id>0)
    return db(query).select()
