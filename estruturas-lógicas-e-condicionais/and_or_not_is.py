"""Exemplos de And, Or, Not, Is"""

ativo = True
logado = True

# exemplo de if e else
if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Cheque seu e-mail')

# exemplo do uso de not
if not ativo:
    print('Você precisa ativar sua conta')
else:
    print('Seja bem-vindo')

print(not False)

#exemplo de is
if ativo is True:
    print('Você precisa ativar sua conta')
else:
    print('Bem-vindo usuário')

# ou: ativo é verdadeiro???
print(ativo is True)
