import itertools

if __name__ == "__main__":
    try:
        # Creating an infinite generator of numbers
        counter = itertools.count(start=1, step=1)
        print("First 5 numbers from the infinite generator:")
        for _ in range(5):
            print(next(counter), end=' ')
        print()

        # Applying a function to each element in an iterator
        numbers = [(2, 5), (3, 2), (10, 3)]
        squares = itertools.starmap(pow, numbers)
        # squares = map(lambda x: x ** 2, numbers)
        print("Squares of the numbers:", list(squares))

        # Combining several iterators into one
        iterator1 = range(3)
        iterator2 = range(3, 6)
        combined = itertools.chain(iterator1, iterator2)
        print("Combined iterators:", list(combined))

    except Exception as e:
        print("An error occurred:", e)
