def lin(est, tam):
    print(f'{est}' * tam)
def maior(* int):
    lin('-=', 20)
    print('analisando valores informados...')
    for v in int:
        print(v, end=' ')
    print(f'Foram informados {len(int)} valores ao todo')
    print(f'O maior valor informado foi {max(int)}.')
    print()
maior(1, 3, 4, 6, 7, 8)