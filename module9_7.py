def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            bool_ = False
        else:
            bool_ = True
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    bool_ = False
                    break

        if bool_:
            print('Число простое')
        else:
            print("Число составное")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 0, 0)
print(result)
