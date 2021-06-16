def div_por_7_no_por_5(num_1, num_2):
    for i in range(num_1,num_2+1):
        if i % 7 == 0:
            if i % 5 == 0:
                pass
            else:
                print(f' {i} es divisible por 7, pero no por 5.')
    return

div_por_7_no_por_5(0,42)