# David Wylie
# CIS150AB Spring 2025
# Computer Purchase Calculator (computer_purchase.py)

MESA_TAX_RATE = 0.083


def calculate_purchase(a_units, a_cost, b_units, b_cost):
    """
    Calculate and display the total cost of a computer purchase order.

    This function calculates the total cost for purchasing two
    different types of computers.
    It calculate pre-tax total, applies the Mesa sales tax rate,
    and displays a formatted receipt showing the itemized costs.

    Parameters:
        a_units (int): Number of units of computer "A" version
        a_cost (float): Cost per unit of computer "A" version
        b_units (int): Number of units of computer "B" version
        b_cost (float): Cost per unit of computer "B" version

    Returns:
        None:
        The function prints the receipt to the console

    Example:
        Two (2) units of Computer A at $3,150.00 per unit
        Five (5) units of Computer B at $1350.55 per unit
        calculate_purchase(2, 3150, 5, 1350.55)
    """

    total_pretax = (a_units * a_cost) + (b_units * b_cost)
    total_tax = total_pretax * MESA_TAX_RATE
    total_cost = total_pretax + total_tax
    print(f"""
-----------COMPUTER PURCHASE CALCULATOR-----------
Computer        Units       Price       Line Total
Version A         {a_units}       ${a_cost:,.2f}     ${a_units * a_cost:,.2f}
Version B         {b_units}       ${b_cost:,.2f}     ${b_units * b_cost:,.2f}
--------------------------------------------------
  Pre-Tax Cost: ${total_pretax:>9,.2f}
Sales Tax Rate: {MESA_TAX_RATE * 100:>9.1f}%
           Tax: ${total_tax:>9,.2f}
    Total Cost: ${total_cost:>9,.2f}
          """)


calculate_purchase(2, 3150, 5, 1350.55)
