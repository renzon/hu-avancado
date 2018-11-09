"""
>>> executar('/')
404
>>> @rota('/')
... def raiz():
...     return 'Raiz'
...
>>> executar('/')
'Raiz'
>>> @rota('/nome')
... def ola(nome):
...     return f'Olá {nome}'
...
>>> executar('/nome', 'Renzo')
'Olá Renzo'
>>> executar('/nome', nome='Tre')
'Olá Tre'
"""