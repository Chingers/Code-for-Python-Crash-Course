#8-12, Python Crash Course, Sandwiches

#Functions
def make_sandwich(*items):
    """Prints summary of the sandwich being made"""
    print("\nThe sandwhich being made has:")
    for item in items:
        print("- " + item)

make_sandwich('cheese', 'ham')
make_sandwich('cheese', 'ham', 'tomatoes')
make_sandwich('chicken')
