# 내 풀이
def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        num1 = phone_book[i - 1]
        num2 = phone_book[i]

        if len(num1) < len(num2):
            if num1 == num2[: len(num1)]:
                return False
        else:
            if num2 == num1[: len(num2)]:
                return False
    return True


# 베스트 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
