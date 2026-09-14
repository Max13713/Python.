def fatorial(num=0, show=False):
    """
    -> calcula o fatorial de um numero.
    :param num: o numero a ser calculado.
    :param show: (OPCIONAL) mostra ou nao a conta
    :return: o valorr do fatorial de um numero num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c

        if show:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
    return f
print(fatorial(5, True))
    