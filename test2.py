# fruits = [
#         {'name':'apple','price':20},
#         {'name':'orange','price':10},
#     ]

# print(
#     {fruit['name']: fruit['price'] for fruit in fruits if fruit['price'] < 20}
# )

print(
    list(
        filter(lambda x: x > 1, {1,2,3,4})
        )
    )