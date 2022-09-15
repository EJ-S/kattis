stocks_held = 0
avg_cost = 0

while True:
    command = input().split()
    command[1] = int(command[1])
    if command[0] == 'die':
        profit = command[1] - avg_cost
        #print(avg_cost, stocks_held, profit)
        if profit >= 0:
            print(float(stocks_held * (command[1] - (command[1] - avg_cost)*0.3)))
        else:
            print(float(stocks_held * command[1]))
        break
    elif command[0] == 'buy':
        avg_cost = ((avg_cost * stocks_held) + (command[1] * int(command[2]))) / (stocks_held + command[1])
        stocks_held += command[1]
    elif command[0] == 'sell':
        stocks_held -= command[1]
    elif command[0] == 'split':
        stocks_held *= command[1]
        avg_cost /= command[1]
    else:
        stocks_held = stocks_held // command[1]
        avg_cost = avg_cost * command[1]
    #print("AVG COST:", avg_cost)
    #print("STOCKS HELD:", stocks_held)
