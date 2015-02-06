# -*- coding: utf-8 -*-
db.define_table('my_order',
                Field('item'),
                Field('buyer'),
                Field('recipient'),
                Field('ship_date', 'date'),
                Field('if_pass_customs','boolean'),
                Field('receive_date', 'date'),
                Field('if_confirmed','boolean'),
                Field('ship_number'),
                Field('order_destination'),
                Field('order_comment'),
                Field('rrp', 'double'),
                Field('tax_rate', 'double'),
                Field('ship_fee', 'double'),
                Field('if_double_point','boolean')
               )


def selectAllOrder():
    query = (db.my_order.id>0)
    return db(query).select()
