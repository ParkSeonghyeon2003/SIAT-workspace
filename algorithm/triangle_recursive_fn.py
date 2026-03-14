def print_trianle(width):
    if width == 0: return
    print_trianle(width - 1)
    return print("*" * width)

def solve_triangle():
    n = int(input())
    print_trianle(n)

if __name__ == "__main__":
    solve_triangle()