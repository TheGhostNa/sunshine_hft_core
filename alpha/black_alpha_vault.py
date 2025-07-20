vault_balance = 0.0


def inject(amount):
    global vault_balance
    vault_balance += amount
    print(f"⚫ Black Alpha Vault +${amount:.2f} | Total = ${vault_balance:.2f}")


def get_balance():
    return vault_balance
