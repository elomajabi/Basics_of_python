# A store wants to know how many times each product was bought.
# You are given:
# products = [
# "apple",
# "banana",
# "apple",
# "orange",
# "banana",
# "apple"
# ]
#
# count how many times each product appears.

products = [
"apple",
"banana",
"apple",
"orange",
"banana",
"apple"
]

count = {}

for product in products:
    if product not in count:
        count[product] = 1
    else:
        count[product] += 1

print(count)