import classbody
def main():
    user = classbody.Authorization(
        name=input("Введите имя: "),
        surname=input("Введите фамилию: "),
        login=input("Введите логин: "),
        password=input("Введите пароль: "),
        hash_algorithm=input("Алгоритм хеширования(sha256, md5): "))
    print(user.hashing_pass())
    print(user.info())
    print(user.is_employee())

if __name__ == "__main__":
    main()
