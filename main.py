from fns_and_dsa.arithmetic_operations import perform_operation


def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

# main.py

from book_class import Book
def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)
    print(repr(my_book))
    del my_book
if __name__ == "__main__":
    main()
