from modal.containers import Containers


class Users:
    @staticmethod
    def confirm_account(email, password):
        pass

    @staticmethod
    def get_users():
        # lay thong tin tat ca nguoi dung va so container
        pass

    @staticmethod
    def get_user(user_id):
        pass

    @staticmethod
    def create_user(user):
        pass

    @staticmethod
    def edit_user(user):
        pass

    @staticmethod
    def del_user(user_id):
        pass

    @staticmethod
    def count():
        pass


class User:
    def __init__(self, name, email, phone_number, note, duty):
        self.id = None
        pass

    def get_containers(self):
        if self.id is None:
            return None
        return Containers.get_container_by_user(self.id)

