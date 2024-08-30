import sys
import math

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12
    if annual_rate == 0:
        return principal / num_payments
    return principal * monthly_rate / (1 - math.pow(1 + monthly_rate, -num_payments))

def generate_amortization_table(principal, annual_rate, years):
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    balance = principal
    num_payments = years * 12

    print(f"{'Month':<8}{'Payment':<15}{'Interest':<15}{'Principal':<15}{'Remaining Principal'}")
    print("=" * 60)

    for month in range(1, num_payments + 1):
        interest = balance * (annual_rate / 12 / 100)
        principal_payment = monthly_payment - interest
        balance -= principal_payment
        print(f"{month:<8}{monthly_payment:<15.2f}{interest:<15.2f}{principal_payment:<15.2f}{balance:.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python loan_table.py <years> <principal> <annual_rate>")
    else:
        years = int(sys.argv[1])
        principal = float(sys.argv[2])
        annual_rate = float(sys.argv[3])

        generate_amortization_table(principal, annual_rate, years)
