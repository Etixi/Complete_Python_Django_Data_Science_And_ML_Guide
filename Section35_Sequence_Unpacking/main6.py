print()
print("Practice - Unpacking a Dictionary into Keyword Arguments" + "\n" +
      "=======================================================")
print()

def setup_db_connection(hostname, port, username, password):
    print(hostname, port, username, password)
    return {'hostname': hostname, 'port': port, 'username': username, 'password': password}

data = {
    'hostname': 'localhost',
    'username': 'admin',
    'password': 'admin123',
    'port_value': 3674,
}


data['port'] = data['port_value']
del data['port']

setup_db_connection(*data)