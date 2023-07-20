def A000124(n):
    result = []
    current_val = 1
    for i in range(0, n ):
        current_val += i
        result.append(str(current_val))
    return "-".join(result)

if __name__ == "__main__":
    try:
        input_number = int(input("Masukkan angka: "))
        if input_number <= 0:
            print("Masukkan angka positif lebih dari nol!")
        else:
            output = A000124(input_number)
            print(f"Output: {output}")
    except ValueError:
        print("Input yang salah! Pastikan Anda memasukkan angka dengan benar.")