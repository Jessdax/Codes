import time
from datetime import datetime

#Packaging
from packaging.main_packaging import main_packaging

#Processing
from processing.main_processing import main_processing

#Quality Control
from quality_control.main_control import main_control

#Raw Materials
from raw_materials.main_material import main
from raw_materials.supplier import get_ingredients

# ====== NEW FEATURES ======

# Bottle counter
bottles_produced = 0

# Helper function to log with timestamp
def log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")


# ====== MENU ======
def main_menu():
    print("|" + "=" * 40,  "|")
    print("|🚀 Jessitol Production Line Automation   |")
    print("|1. Raw Materials Check                   |")
    print("|2. Process Formula                       |")
    print("|3. Quality Control                       |")
    print("|4. Packaging                             |")
    print("|5. Run Full Workflow                     |")
    print("|6. Exit                                  |")
    print("|" + "=" * 40,  "|")

# ====== WORKFLOW ======
def full_workflow():
    global bottles_produced

    time.sleep(1)
    log("Starting Raw Materials")
    print("Checking supplies")
    main()

    time.sleep(1)
    log("Starting Processing")
    print("Mixing ingredients")
    main_processing()

    time.sleep(1)
    log("Starting Quality Control")
    print("Inspecting samples")
    main_control()

    time.sleep(1)
    log("Starting Packaging")
    print("Sealing bottles")
    main_packaging()

    # Example: produce a random number of bottles per run
    produced_now = 50
    bottles_produced += produced_now
    log(f"✅ Jessitol Production Cycle Completed! Produced {produced_now} bottles this run.")
    log(f"📦 Total bottles produced so far: {bottles_produced}")

# ====== RUN ======
def run_production_line():
    while True:
        main_menu()
        choice = input("|Select an option (1-6): ").strip()
        match choice:
            case "1":
                log("Starting Raw Materials")
                print("Checking supplies...")
                main()

            case "2":
                log("Starting Processing")
                print("Mixing ingredients...")
                main_processing()

            case "3":
                log("Starting Quality Control")
                print("Inspecting samples...")
                main_control()

            case "4":
                log("Starting Packaging")
                print("Sealing bottles...")
                main_packaging()

            case "5":
                log("Starting Full Workflow")
                print("Working on Full Workflow...")
                full_workflow()

            case "6":
                log("👋 Exiting production line. Goodbye!")
                break

            case _:
                log("❌ Invalid choice. Try again.")  

if __name__ == "__main__":
    run_production_line()
