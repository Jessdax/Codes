# Collecting of User's Income
wk_i = int(input(" What is your weekly income: "))
no_of_dys_sv = int (input(" Number of days they want to save: "))
est_dly_ex = int (input(" What is your estimated daily expenses: "))
ttl_wk_ex = int ( est_dly_ex * 7)
rm_mny = int ( wk_i - ttl_wk_ex )
dly_sng_5_dy = rm_mny / no_of_dys_sv 

# Budget Planner
print("Budget Planner\n")
print(f" Weekly Income: {wk_i}")
print(f" Daily Expenses: {est_dly_ex}")
print(f" Total Weekly Expenses: {ttl_wk_ex}")
print(f" Remaining Money: {rm_mny}")
print(f" Daily Savings Over {no_of_dys_sv} Days: {dly_sng_5_dy}")