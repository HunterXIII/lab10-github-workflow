import re


def is_valid_email(email):
    # Точка разделяет части имени. Дефис допустим внутри части домена.
    name = r"[A-Za-z0-9_%+-]+"
    domain = r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}"
    return re.fullmatch(name + "@" + domain, email) is not None


if __name__ == "__main__":
    email = input("Введите email: ")
    if is_valid_email(email):
        print("Email подходит для регистрации.")
    else:
        print("Некорректный email.")
