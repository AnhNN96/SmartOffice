from model.containers import Containers
from model.connect_db import DatabaseDriver

class Users:

    @staticmethod
    def confirm_account(email, password):
        query = 'select * from m_user join s_user on m_user.id = s_user.user_id and m_user.last_update_date = s_user.last_update_date where m_user.email = ? and s_user.password = ?'
        args = [email, password]
        result = DatabaseDriver().query_db(query, args, one = True)
        return (result is not None) and (len(result) != 0)

    @staticmethod
    def get_users():
        '''get info user and statistic container'''
        pass

    @staticmethod
    def get_user(user_id):
        ''''''

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

