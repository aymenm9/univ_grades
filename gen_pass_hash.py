from werkzeug.security import generate_password_hash
import csv

with open("admin.csv", 'a') as f:
    filednames = ['username', 'password', 'hash']
    writer = csv.DictWriter(f,fieldnames=filednames)
    password = 'admin'
    pwhash = generate_password_hash(password)
    user = {}
    user['username'] = 'admin'
    user['password'] = password
    user['hash'] = pwhash
    writer.writerow(user)