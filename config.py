from distutils.debug import DEBUG


class DevelopmentConfig():
    DEBUG =True
    MYSQL_HOST        = 'localhost'
    MYSQL_USER        = 'root'
    MYSQL_PASSWORD    = ''
    MYSQL_DB         = 'proyecto_jornada_almuerzo'

config ={
    'development': DevelopmentConfig
}