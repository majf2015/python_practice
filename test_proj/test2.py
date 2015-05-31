#profit = int(raw_input("please input your profit:"))

def Commision(profit):
    if profit <= 100000:
        commision = profit * 0.1
    elif profit <= 200000:
        commision = (profit - 100000) * 0.075 + Commision(100000)
    elif profit <= 400000:
        commision = (profit - 200000) * 0.05 + Commision(200000)
    elif profit <= 600000:
        commision = (profit - 400000) * 0.03 + Commision(400000)
    elif profit <= 1000000:
        commision = (profit - 600000) * 0.015 + Commision(600000)
    else:
        commision = (profit - 1000000) * 0.01 + Commision(1000000)
    return commision




def test_profit(input, output):
    Coutput = Commision(input)
    if Coutput != output:
        print input, output, Coutput

test_profit(100000, 10000)
test_profit(200000, 17500)
test_profit(400000, 27500)
test_profit(470002, 29600.06)
test_profit(600000, 33500)
test_profit(1000000, 39500)
test_profit(2000000, 49500)