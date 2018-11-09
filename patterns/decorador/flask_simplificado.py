"""
>>> app=FlaskSimplificado()
>>> app.executar('/')
404
>>> @app.rota('/')
... def raiz():
...     return 'Raiz'
...
>>> app.executar('/')
'Raiz'
>>> @app.rota('/nome')
... def ola(nome):
...     return f'Olá {nome}'
...
>>> app.executar('/nome', 'Renzo')
'Olá Renzo'
>>> app.executar('/nome', nome='Tre')
'Olá Tre'
"""