budget = int(input(" Total Budget for Snacks: $"))
no_friends = int(input(" Number of Friends Joining: "))
price_per_snacks = int(input(" Price per Snacks: $"))
packs_wanted = int(input(" Packs Wanted: "))

snack_cost = packs_wanted * price_per_snacks
total_servings = packs_wanted * no_friends

t_budget25 = budget * 0.25
t_budget50 = budget * 0.50
t_budget75 = budget * 0.75
discounted_cost = snack_cost + t_budget25
discount_price = snack_cost * .05
dis_price = snack_cost - discount_price


print(f" Your Total Budget is: {snack_cost}")

if snack_cost > budget:
    print(f" Over Budget! Snack cost: ${snack_cost:.2f}")

elif snack_cost <= t_budget25 :
    print(f" Small Snack Haul! Discounted Cost: $ {dis_price:.2f}\n ")

elif snack_cost > t_budget25 and snack_cost <= t_budget50 and no_friends >= 3:
    print(f" Group Snack Deal! Cost: ${snack_cost:.2f}")

elif snack_cost > t_budget25 and snack_cost <= t_budget50 and no_friends <= 3:
    print(f" Wala kang Friend? Cost: ${snack_cost:.2f}")
    
elif snack_cost > t_budget50 and snack_cost <= t_budget75:
    print(f" Medium Snack Plan!: ${snack_cost:.2f}")

elif snack_cost > t_budget75 and snack_cost <= budget:
    print(f" Big Snack Night!: #{snack_cost:.2f}")

else:
    print(" No Plan is Recorded ")

if total_servings < 5:
    print(" WARNING!: Might not have enough snacks!")

