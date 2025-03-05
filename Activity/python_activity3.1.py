# User Input
nm = str (input(" Enter Name: "))
wght = float (input(" Enter Weight: "))

stps_wlk = int (input("Enter How Many Steps Walked: "))
yrs_exr = int (input(" Years Started Exercising: "))
yr_exer = 2025 - yrs_exr
est_wght_nxt_yr = wght - .2

# Displaying the User's Input
print(f" Name: {nm}")
print(f" Weight: {wght}")
print(f" Steps Walked: {stps_wlk}")
print(f" Years Exercising: {yr_exer}")
print(f" Estimated Weght Next Month: {est_wght_nxt_yr}")