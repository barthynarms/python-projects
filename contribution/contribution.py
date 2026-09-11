
target = 500000
raised = 0
contributions = []  # stores (name, amount) pairs

def show_progress():
    remaining = target - raised
    percent = (raised / target) * 100
    
    bar_length = 30
    filled = int(bar_length * raised / target)
    bar = "█" * filled + "░" * (bar_length - filled) #Linux

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
        print(f"✅ Added ₦{amount:,.2f} from {name}")
        

    elif choice == "2":
        show_progress()

    elif choice == "3":
        show_list()

    elif choice == "4":
        print("Exiting... Final summary:")
        show_progress()
        break

    else:4
        print("Invalid option, please choose 1-4.")