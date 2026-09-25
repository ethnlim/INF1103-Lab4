def get_valid_input():
    """Prompt for a delivery quantity. Returns (quantity, is_valid, is_quit)."""
    user_input = input("Number of items: ").strip()

    if user_input.lower() == 'quit':
        return None, False, True

    # Checks for negative integers and rejects them
    if user_input.startswith("-") and user_input[1:].isdigit():
        print(f"Error: '{user_input}' is negative. Negative stock is not allowed.\n")
        return None, False, False

    if not user_input.isdigit():
        # Not a whole number at all (letters, symbols, decimals, empty, etc.)
        print(f"Error: '{user_input}' is not a valid number. Please enter a whole number.\n")
        return None, False, False

    return int(user_input), True, False


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("=== Delivery Audit Report ===")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")

def load_inventory(filename="inventory.txt"):
    #Load saved total and transaction history. Returns (total, history).
    try:
        with open(filename, "r") as f:
            print("File opened successfully!!")
    except FileNotFoundError:
        print("File not found, starting fresh.")
        return 0, []

def main():
    load_inventory()  # test call
    total_inventory = 0
    failed_entries = 0

    print("Enter the number of items in inventory: or type 'quit' to exit")

    while True:
        quantity, is_valid, is_quit = get_valid_input()

        if is_quit:
            print("Exiting the auditor.")
            break

        if not is_valid:
            failed_entries += 1
            continue

        total_inventory = process_delivery(total_inventory, quantity)
        tax = calculate_tax(quantity)
        print(f"Added {quantity} items to inventory. Tax for this delivery: {tax:.2f}")
        print(f"Total inventory is now: {total_inventory}\n")

        # Trigger Overstock Alert if total inventory exceeds 500 units
        if total_inventory > 500:
            print(f"OVERSTOCK ALERT! Total inventory ({total_inventory}) exceeds the 500 unit limit.")
            print("Halting entry process immediately.\n")
            break
        elif total_inventory == 500:
            print("Notice: Inventory is exactly at the 500 unit capacity limit.\n")

    generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()
