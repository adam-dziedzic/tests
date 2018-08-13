tax_table = [(10000, 0.1), (20000, 0.2), (None, 0.3)]


def get_tax(init_salary, tax_table):
    tax = 0
    salary = init_salary
    previous_limit = 0
    for limit, ratio in tax_table:
        if limit is None or init_salary < limit:
            tax += salary * ratio
            return tax
        current_salary = limit - previous_limit
        tax += current_salary * ratio
        previous_limit = limit
        salary -= current_salary


if __name__ == "__main__":
    tax = get_tax(31000, tax_table)
    print("tax: ", tax)
    assert get_tax(500, tax_table) == 50
    assert get_tax(10000, tax_table) == 1000
    assert get_tax(10100, tax_table) == 1020
    assert get_tax(20000, tax_table) == 3000
    assert get_tax(20100, tax_table) == 3030
    assert get_tax(30000, tax_table) == 6000
    assert get_tax(36000, tax_table) == 7800


