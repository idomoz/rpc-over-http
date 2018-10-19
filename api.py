def logout_user(address):
    pass


def register_user(username, password, age):
    pass


BANNES_ADDRESS = '1.1.1.1'


def login(username, password, request):
    if username == 'foo' and password == 'bar' and request.remote_addr != BANNES_ADDRESS:
        return 'logged in!'
    return 'forbidden'


def logout(request):
    logout_user(request.remote_addr)


def register(username, password, age=20, request=None):
    register_user(username, password, age)
