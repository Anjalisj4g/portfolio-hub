
import time

# --------------------------------
# 1. PRODUCT CATALOG
# --------------------------------

products = [
    {"id": 101, "name": "Laptop", "category": "Electronics", "price": 55000},
    {"id": 102, "name": "Smartphone", "category": "Electronics", "price": 25000},
    {"id": 103, "name": "Headphones", "category": "Accessories", "price": 2000},
    {"id": 104, "name": "Keyboard", "category": "Accessories", "price": 1500},
    {"id": 105, "name": "Smart Watch", "category": "Electronics", "price": 5000},
    {"id": 106, "name": "Shoes", "category": "Fashion", "price": 3000},
    {"id": 107, "name": "Backpack", "category": "Fashion", "price": 1200},
    {"id": 108, "name": "Monitor", "category": "Electronics", "price": 12000},
    {"id": 109, "name": "Mouse", "category": "Accessories", "price": 800},
    {"id": 110, "name": "Tablet", "category": "Electronics", "price": 18000}
]


# --------------------------------
# 2. DISPLAY PRODUCTS
# --------------------------------

def display_products(product_list):

    print("\n--------- PRODUCT CATALOG ---------")

    print("ID\tName\t\tCategory\tPrice")

    for product in product_list:

        print(
            product["id"],
            "\t",
            product["name"],
            "\t",
            product["category"],
            "\t",
            product["price"]
        )


# --------------------------------
# 3. LINEAR SEARCH
# --------------------------------

def linear_search(product_list, target_id):

    for product in product_list:

        if product["id"] == target_id:
            return product

    return None


# --------------------------------
# 4. BINARY SEARCH
# --------------------------------

def binary_search(product_list, target_id):

    low = 0
    high = len(product_list) - 1

    while low <= high:

        mid = (low + high) // 2

        if product_list[mid]["id"] == target_id:

            return product_list[mid]

        elif product_list[mid]["id"] < target_id:

            low = mid + 1

        else:

            high = mid - 1

    return None


# --------------------------------
# 5. SELECTION SORT BY PRICE
# --------------------------------

def selection_sort(product_list):

    sorted_products = product_list.copy()

    n = len(sorted_products)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if sorted_products[j]["price"] < sorted_products[min_index]["price"]:

                min_index = j

        sorted_products[i], sorted_products[min_index] = (
            sorted_products[min_index],
            sorted_products[i]
        )

    return sorted_products


# --------------------------------
# 6. BUBBLE SORT BY NAME
# --------------------------------

def bubble_sort(product_list):

    sorted_products = product_list.copy()

    n = len(sorted_products)

    for i in range(n):

        for j in range(0, n - i - 1):

            if sorted_products[j]["name"] > sorted_products[j + 1]["name"]:

                sorted_products[j], sorted_products[j + 1] = (
                    sorted_products[j + 1],
                    sorted_products[j]
                )

    return sorted_products


# --------------------------------
# 7. SEARCH PERFORMANCE COMPARISON
# --------------------------------

def compare_search_performance():

    target_id = 110

    sorted_products = sorted(products, key=lambda p: p["id"])

    repetitions = 10000

    start = time.perf_counter()

    for i in range(repetitions):
        linear_search(products, target_id)

    linear_time = time.perf_counter() - start

    start = time.perf_counter()

    for i in range(repetitions):
        binary_search(sorted_products, target_id)

    binary_time = time.perf_counter() - start

    print("\n------ SEARCH PERFORMANCE ------")

    print("Linear Search Time:", linear_time)
    print("Binary Search Time:", binary_time)


# --------------------------------
# 8. SORTING PERFORMANCE COMPARISON
# --------------------------------

def compare_sorting_performance():

    repetitions = 10000

    start = time.perf_counter()

    for i in range(repetitions):
        selection_sort(products)

    selection_time = time.perf_counter() - start

    start = time.perf_counter()

    for i in range(repetitions):
        bubble_sort(products)

    bubble_time = time.perf_counter() - start

    print("\n------ SORTING PERFORMANCE ------")

    print("Selection Sort Time:", selection_time)
    print("Bubble Sort Time:", bubble_time)


# --------------------------------
# 9. MAIN MENU
# --------------------------------

while True:

    print("\n========== SHOPSEARCH ==========")

    print("1. Display All Products")
    print("2. Search Product Using Linear Search")
    print("3. Search Product Using Binary Search")
    print("4. Sort Products by Price")
    print("5. Sort Products by Name")
    print("6. Compare Searching Algorithms")
    print("7. Compare Sorting Algorithms")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        display_products(products)

    elif choice == "2":

        target = int(input("Enter Product ID: "))

        result = linear_search(products, target)

        if result:
            print("\nProduct Found:", result)
        else:
            print("\nProduct Not Found")

    elif choice == "3":

        target = int(input("Enter Product ID: "))

        sorted_products = sorted(products, key=lambda p: p["id"])

        result = binary_search(sorted_products, target)

        if result:
            print("\nProduct Found:", result)
        else:
            print("\nProduct Not Found")

    elif choice == "4":

        result = selection_sort(products)

        print("\nProducts Sorted by Price:")

        display_products(result)

    elif choice == "5":

        result = bubble_sort(products)

        print("\nProducts Sorted by Name:")

        display_products(result)

    elif choice == "6":

        compare_search_performance()

    elif choice == "7":

        compare_sorting_performance()

    elif choice == "0":

        print("Thank you for using ShopSearch!")

        break

    else:

        print("Invalid Choice. Please Try Again.")
