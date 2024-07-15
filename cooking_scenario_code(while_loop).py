import time

# Simulated function to check the cooking status of the rice
def check_rice_cooking_status():
    print("Checking the cooking status of the rice...")
    time.sleep(1)  # Simulating checking time

# Simulated function to determine if the rice is fully cooked
def rice_is_fully_cooked():
    print("Determining if the rice is fully cooked...")
    time.sleep(1)  # Simulating determination time
    return True  # Simulated result for demonstration

rice_status = "uncooked"
while rice_status == "uncooked":
    check_rice_cooking_status()
    if rice_is_fully_cooked():
        rice_status = "cooked"
    else:
        print("The rice is still cooking...")

print("The rice is fully cooked. Enjoy your meal!")

