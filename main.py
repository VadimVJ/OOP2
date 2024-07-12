class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._users_list = []

    def add_user(self, user):
        self._users_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен в систему.")

    def remove_user(self, user_id):
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"Пользователь с ID {user_id} удален из системы.")
                return
        print(f"Пользователя с ID {user_id} нет в системе.")


# Пример использования
user1 = User(1, "Иванов")
user2 = User(2, "Петров")
admin = Admin(100, "Администратор")

admin.add_user(user1)
admin.add_user(user2)

admin.remove_user(1)
admin.remove_user(3)