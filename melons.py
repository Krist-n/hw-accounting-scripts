melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

melon_flesh_color = {
}

melon_weight = {
}

melon_rind_color = {
}

melons = dict(melon_names.items() + melon_prices.items() + melon_seedlessness.items()\
     + melon_flesh_color.items() +  melon_weight.items() + melon_rind_color.items())
print(melons)