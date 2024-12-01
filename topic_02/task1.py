
def find_discriminator(a, b, c):
    return b ** 2 - 4 * a * c

def find_roots(a, b, c):
    d = find_discriminator(a, b, c)
    if d < 0:
        return None
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


a_str = input("Уведіть a: ")
b_str = input("Уведіть b: ")
c_str = input("Уведіть c: ")

answer = solve_kvadr_rivn(int(a_str), int(b_str), int(c_str))

<<<<<<< HEAD
=======
coeffs = input_call()
answer = find_roots(coeffs[0], coeffs[1], coeffs[2])

print()
>>>>>>> 77b9501 (add solution for topic_02 and topic_03)
if answer is None:
    print('Коренів не знайдено оскільки Дискримінант від\'ємний.')
else:
    print('Корені квадратного рівняння: ', answer)
