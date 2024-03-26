import Simulator
import Generator
import datetime
import pandas as pd
import random


if __name__ == '__main__':

    stats = pd.DataFrame()

    for i in range(2):
        amount_transactions = random.randint(300,500) # Amount of DVP transactions per day, x2 transactions/day
        amount_participants = random.randint(4,10)
        amount_securities = random.randint(3,7)
        min_balance_value = 1000000
        max_balance_value = 10000000000

         #Initializations:
        opening_time = datetime.time(1,30,0)
        closing_time = datetime.time(19,30,00) #19u30 base
        recycling = True
        credit_limit_percentage = 1.0

        # Freeze participant
        freeze = False
        freeze_part = '41'
        freeze_time = datetime.time(14,00,00)

        start_time = datetime.datetime.now()
        print("Start Time:", start_time.strftime('%Y-%m-%d %H:%M:%S'))

        Generator.generate_data(amount_transactions, amount_participants, amount_securities, min_balance_value, max_balance_value)

        max_credit, final_settlement_efficiency = Simulator.simulator(opening_time, closing_time, recycling, credit_limit_percentage, freeze, freeze_part, freeze_time)

        end_time = datetime.datetime.now()
        print("End Time:", end_time.strftime('%Y-%m-%d %H:%M:%S'))
        duration = end_time - start_time
        print("Execution Duration:", duration)

        new_row = pd.DataFrame({"transactions DVP": [amount_transactions],"participants": [amount_participants],"securities": [amount_securities],"min bal": [min_balance_value],"max bal": [max_balance_value],"efficiency": [final_settlement_efficiency],"max total credit": [max_credit]}, index=[0])
        stats = pd.concat([stats, new_row], ignore_index=True)
    
    stats.to_csv('RunSummary.csv', index=False, sep = ';')