
class config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aymen:aymen1234@localhost/cs50'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_PERMANENT= False
    SESSION_TYPE= "filesystem"
    SESSION_TYPE = 'sqlalchemy'