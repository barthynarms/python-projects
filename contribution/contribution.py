import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "contributions.json")
target = 500000

def load_data():
    """Load saved contributions from file, if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []  # no file yet, start empty

def save_data(contributions):
    """Save the current contributions list to file."""
    with open(DATA_FILE, "w") as f:
        json.dump(contributions, f, indent=2)

contributions = load_data()
raised = sum(amount for name, amount in contributions)

def show_progress():
    remaining = target - raised
    percent = (raised / target) * 100
    bar_length = 30
    filled = int(bar_length * raised / target)
    bar = "\u2588" * filled + "\u2591" * (bar_length - filled)

    print("\n" + "=" * 45)
    print("       CONTRIBUTION PROGRESS TRACKER")
    print("=" * 45)
    print(f"Target Amount      : ₦{target:,.2f}")
    print(f"Amount Raised      : ₦{raised:,.2f}")
    print(f"Remaining          : ₦{remaining:,.2f}")
    print(f"Total Members      : {len(contributions)}")
    if contributions:
        avg = raised / len(contributions)
        print(f"Average/Member     : ₦{avg:,.2f}")
    print(f"Progress           : {percent:.1f}%")
    print(f"[{bar}] {percent:.0f}%")
    print("=" * 45)

def show_list():
    print("\n--- Contribution List ---")
    if not contributions:
        print("No contributions yet.")
    for i, (name, amt) in enumerate(contributions, start=1):
        print(f"{i}. {name} - ₦{amt:,.2f}")
    print("-" * 26)

while True:
    print("\n1. Add contribution")
    print("2. Show progress")
    print("3. Show contributor list")
    print("4. Exit")
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        name = input("Contributor name: ").strip()
        try:
            amount = float(input("Amount contributed: ₦").strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        raised += amount
        contributions.append((name, amount))
        save_data(contributions)
        print(f"✅ Added ₦{amount:,.2f} from {name}")

    elif choice == "2":
        show_progress()

    elif choice == "3":
        show_list()

    elif choice == "4":
        print("Exiting... Final summary:")
        show_progress()
        break

    else:
        print("Invalid option, please choose 1-4.")