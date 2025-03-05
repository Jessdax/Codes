products = {
    "Biogesic" : 10,
    "Paracetamol" : 5,
    "Neozep" : 15,
    "Cobra" : 25
}
products["Sting"] = 25

print("Updated Dictionary\n")
for products, price in products.items():
    print(f"{products}: P{price:.2f}")