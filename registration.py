import re


def is_valid_email(email):
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}", email) is not None


if __name__ == "__main__":
    email = input("Введите email: ")
    if is_valid_email(email):
        print("Email подходит для регистрации.")
    else:
        print("Некорректный email.")
