from time import strftime


def logadora(fcn):
    def envoltoria(*args, **kwargs):
        print(strftime('%Y/%M/%d %H:%m:%S'))
        return fcn(*args, **kwargs)

    return envoltoria


def hello():
    return 'Olá'


@logadora
def ola(nome):
    return f'Olá P{nome}'


# Transformações para logar o tempo
hello = logadora(hello)

####

print(hello())
print(hello())
# 2018/11/09 22:00:00
# Olá

print(ola('Renzo'))
# 2018/11/09 22:00:01
# Olá Renzo
