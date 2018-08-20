from modal.containers import Container


class Users:
    @staticmethod
    def get_user(user_id):
        pass

    @staticmethod
    def confirm_account(email, password):
        pass

    @staticmethod
    def get_users():
        # lay thong tin tat ca nguoi dung va so container
        pass

    @staticmethod
    def count():
        pass

    @staticmethod
    def create_user(user):
        pass


class User:
    def __init__(self, name, email, phone_number, note, duty):
        self.activated = None
        self.id = None
        pass

    def get_containers(self):
        if self.id is None:
            return None
        return Container.get_container_by_user(self.id)
