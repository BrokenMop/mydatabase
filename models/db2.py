db.define_table('other_cost',
                Field('name'),
                Field('cost_amount', 'double'),
                Field('cost_date', 'date'),
                Field('cost_comment')
                )
if db(db.other_cost).isempty():
    db.other_cost.insert(name='Initial', cost_amount=float(436), cost_date="2015-02-11")
