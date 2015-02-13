# -*- coding: utf-8 -*-
# try something like
def general():
    if not (is_admin(auth.user.email)):
        exception('Not authorized')
    rows = db(db.my_order.id > 0).select()
    totalCostUSD = float(0)
    totalCostCNY = float(0)
    totalPoints = float(0)
    totalShippingCost =float(0)
    totalReceiveCNY = float(0)
    earning = float(0)
    for row in rows:
        costUSD = row.rrp * float(row.quantity) * (1 + row.tax_rate/100.0) + row.ship_rate
        earning += row.price/row.exchange_rate  - costUSD
        totalCostUSD += costUSD
        totalCostCNY += costUSD * row.exchange_rate
        totalPoints += row.rrp * row.reward.ratio * float(row.quantity)
        totalShippingCost += row.ship_rate
        totalReceiveCNY += row.price
    otherCost = float(0)
    rows = db(db.other_cost.id > 0).select()
    for row  in rows:
        otherCost += row.cost_amount
    return "Cost:" + str(round(totalCostUSD+otherCost,2))+"<br>Earning:"+ str(round(earning-otherCost,2))
