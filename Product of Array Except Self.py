'Product of Array Except Self'
def product_arry(arr):

    n = len(arr)
    left_products = [1] * n
    right_products = [1]* n

    left_product = 1
    for i in range(n):
        left_products[i] = left_product
        left_product *= arr[i]

    right_product =1
    for i in range(n-1,-1,-1):
        right_products[i] = right_product
        right_product *= arr[i]
    output =[]
    for i in range(n):
        output.append(left_products[i] * right_products[i])

    # output = [left_products[i] * right_products[i] for i in range(n)]

    return output

print(product_arry([1, 2, 3, 4]))

