from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

now = dt.now()

possible_destinations = choice(['Brazil', 'Spain', 'UK', 'USA', 'Italy', 'Switzerland', 'Portugal'])

target_year = randint(now.year, now.year + 50)

base_cost = Decimal('280.30')

cost_multiplier = abs(now.year - target_year)

final_cost = Decimal(base_cost * cost_multiplier)

print(custom_module.generate_time_travel_message(target_year, possible_destinations, final_cost))