n = int(input(""))
n_arr = list(map(int, input().split()))
arr_dupli = list(set(n_arr))
arr_dupli.sort(reverse=True)
print(arr_dupli[1])