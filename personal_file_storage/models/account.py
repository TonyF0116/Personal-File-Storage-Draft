from ..db import db_execute


# Create user in the database with the input username and password_hash, set as non-administrator by default
def sign_up(username, password_hash):
    sql = '''INSERT INTO users(UserName, Password, Administrator) VALUES ('{}', '{}', 0);'''
    db_execute(sql.format(username, password_hash))


# Create user in the database with the input username, password_hash, and administrator
def create_user(username, password_hash, administrator):
    sql = '''INSERT INTO users(UserName, Password, Administrator) VALUES ('{}', '{}', {});'''
    db_execute(sql.format(username, password_hash, administrator))


# Return the number of the given username in the database
def check_username(username):
    sql = '''SELECT * FROM users WHERE UserName = '{}';'''
    return len(db_execute(sql.format(username)))


# Return the user info in the database with the given username and password_hash
def check_password(username, password_hash):
    sql = "SELECT * FROM users WHERE UserName = '{}' AND Password = '{}'"
    return db_execute(sql.format(username, password_hash))
