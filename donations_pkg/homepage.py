def show_homepage():
    print("")
    print("        === DonateMe Homepage ===         ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register        |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations  |")
    print("------------------------------------------")
    print("|              5.    Exit                 |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation = f'{username} donated ${donation_amt}'
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for all_donations in donations:
            print(all_donations)
