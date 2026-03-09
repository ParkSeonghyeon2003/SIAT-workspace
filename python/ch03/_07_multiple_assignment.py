a = 10
b = 20
print(a, b)

a, b = 10, 20
print(a, b)

x, y, z = 1, 2, 3
print(x, y, z)

"""
    int first = 10;
    int second = 20;
    int tmp = first;
    first = second;
    second = tmp;
    printf("%d %d", first, second);
"""
first, second = 10, 20
first, second = second, first
print(first, second)

"""
    다중 변수 할당을 사용할 때에는
    당연하지만, 변수의 수와 할당할 값의 수를
    맞춰줘야 한다.
"""