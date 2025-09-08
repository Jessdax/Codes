def main_processing():
    from processing.formula import process_formula
    from processing.inventory import store
    from processing.process import processing

    processing()
    print(process_formula(ingredients=["Jessitol Base", "Stabilizer"]))
    store()
    print("\n")