import random
import time

def run_tests():
    print("Running quality control tests...")
    time.sleep(1)
    print("Color Test Passed.")
    time.sleep(1)
    print("Consistency Test Passed.")
    time.sleep(1)
    print("Odor Test Passed.")
    time.sleep(.5)
    print("✔️  All quality control tests passed.")

def check_defects():
    defects = (["❌ Defects found! Manual inspection needed.",
    "✅ No defects found."])
    result = random.choice(defects)
    if result == "❌ Defects found! Manual inspection needed.":
        return "Failed"
    else:
        return "Passed"
    
def quality_check_pipeline():
    run_tests()
    print("Inspecting for defects...")
    time.sleep(1)
    clear = check_defects()  
    
    if clear == "Failed":
        print("❌ Defects found! Manual inspection needed.")
        print("Hold For Manual Review.")
        time.sleep(1)
        return "Hold"  
    else:
        print("✅ No defects found.")
        print("Cleared for Packaging.")
        return "OK"    

if __name__ == "__main__":
    quality_check_pipeline()