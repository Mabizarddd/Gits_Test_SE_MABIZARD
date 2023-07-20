def is_balanced_brackets(b):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in b:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"

if __name__ == "__main__":
    try:
        input_str = input("Masukkan string yang berisi tanda kurung: ")
        result = is_balanced_brackets(input_str)
        print("Output:", result)
    except Exception as e:
        print("Terjadi kesalahan:", e)