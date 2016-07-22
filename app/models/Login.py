""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Login(Model):
    def __init__(self):
        super(Login, self).__init__()

    def create(self, info):
        query = "INSERT INTO login_registration (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
        hash_pw = self.bcrypt.generate_password_hash(info['password'])
        data = {
            'first_name' : info['first_name'],
            'last_name' : info['last_name'],
            'email' : info['email'],
            'password' : hash_pw,
        }
        return self.db.query_db(query, data)

    def get_login_registration(self):
        return self.db.query_db("SELECT * FROM login_registration")

    def get_user_by_id(self, id):
        query = "SELECT * FROM login_registration WHERE id = :id"
        data = {'id' : id}
        return self.db.query_db(query,data)

    def login(self, login_data):
        email = login_data['email']
        password = login_data['password']
        user_query = 'SELECT * FROM login_registration WHERE email = :email LIMIT 1'
        query_value = { 'email': email}
        user = self.db.query_db(user_query, query_value)
        if self.bcrypt.check_password_hash(user[0]['password'],password):
            return user[0]
        else:
            return False



    # def destroy(self, id):
    #     query = "DELETE FROM login_registration WHERE id = :id"
    #     data = {'id' : id}
    #     return self.db.query_db(query, data)


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """