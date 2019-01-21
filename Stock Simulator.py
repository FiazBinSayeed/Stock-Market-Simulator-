import random
import time
import sys
import keyboard 

original_cash = random.randint(100,10000) #produces virtual coins for the user to invest 
number_of_stocks_owned = 0
money_in_stocks = 0
original_stock_price = random.randint(5,100) #randomizes company stock price

time.sleep(1)
print("You have $",original_cash, "available to invest")
time.sleep(1) 
print("The stock price of this company is $",original_stock_price)
time.sleep(1)
max_to_buy = int(original_cash/original_stock_price) #notifies user of how many shares can be bought with the given capital
print("You can buy a max of", max_to_buy, "shares in this company")
time.sleep(2)  

initial_buy = int(input("How many shares do you wish to purcahse? "))
if initial_buy>max_to_buy: #tests to make sure that the desired amount of shares can be purchased with the initial capital
    print("You don't have enough cash to buy that many shares yet. Please try again")
    sys.exit() 

number_of_stocks_owned = number_of_stocks_owned + initial_buy
money_in_stocks = money_in_stocks + initial_buy * original_stock_price
cash = original_cash - initial_buy * original_stock_price

time.sleep(1.5) 
print("Congratulations! You now own", number_of_stocks_owned, "shares in the company")
time.sleep(1.5)
print("You invested $",money_in_stocks)
time.sleep(1.5) 
print("")

def volatility(stock_price): #function which randomly changes the price of the stock
    r = random.randint(1,2)
    x = random.randint(6,10) #you can increase volatility in the market by lowering the first bound i.e by changing 6 to 4. 
    if r ==1:
        stock_price = stock_price + 1/x * stock_price 
    if r ==2:
        stock_price = stock_price - 1/x * stock_price
    time.sleep(.10)
    return stock_price

time.sleep(2)
print("The market seems to be extremely volatile today")
time.sleep(2) 
print("Press S when you want to sell your stocks.")
time.sleep(2)
print("Good Luck!") 
print("")

while True: #creates a loop
    new_price = int(volatility(original_stock_price))
    print("The current price of the stock is $",new_price)
    if keyboard.is_pressed('s'): #when s is pressed, the following lines are executed 
        print("") 
        time.sleep(1) 
        profit = number_of_stocks_owned * new_price - number_of_stocks_owned * original_stock_price
        new_money_in_stocks = money_in_stocks + profit
        print("You had bought", initial_buy, "stocks at $",original_stock_price, "a share for a total of $",money_in_stocks)
        time.sleep(1)
        print("You sold", initial_buy, "stocks at $",new_price, "a share for a total of $",new_money_in_stocks)
        time.sleep(1) 
        if profit<0:
            print ("Oops. You lost $",abs(profit),". Better luck next time!")
        else:
            print ("Congrats! You made $",profit, "in profit")
        return_from_investing = int((new_money_in_stocks - money_in_stocks)/money_in_stocks * 100)
        print("Your total return was", return_from_investing,"%")
        time.sleep(1)
        new_cash = cash + new_money_in_stocks
        print("You now have $",new_cash, "in cash to invest")
        time.sleep(1) 
        break #stops executing the program if "s" is pressed once
    else:
        pass #allows the program to keep running until the user chooses to sell their stocks.
        

        


