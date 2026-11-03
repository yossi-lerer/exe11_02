VAT_RATE = 0.17

def add_vat(amount):
    return (amount * VAT_RATE) + amount

def apply_discount(amount, percent):
    return amount * (1 - (percent / 100))

if __name__ == "__main__":
    print(apply_discount(200, 10))