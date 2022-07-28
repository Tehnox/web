import os


def create_file(file_path: str):
    if not os.path.isfile(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        f = open(file_path, 'x')
        f.close()


bind = '0.0.0.0:8080'
workers = 1
daemon = True

accesslog = './logs/hello_module_access.log'
create_file(accesslog)

errorlog = './logs/hello_module_error.log'
create_file(errorlog)
