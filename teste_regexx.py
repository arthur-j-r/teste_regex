import re

dados = {
    'emails': ['email@example.com', 'invalid-email', 'user@domain', 'another@example.com'],
    'telefones': ['(11) 98765-4321', '11 987654321', 'invalid-phone'],
    'cpfs': ['123.456.789-00', '123.456.789-01', 'invalid-cpf']
}


def verificador_de_email(email):
    if re.match(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$', email):
        print(f'{email} é um email válido.')
        return True
    else:
        print(f'{email} não é um email válido.')
        return False
def verificador_de_telefone(telefone): 
    if re.match(r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', telefone):
        print(f'{telefone} é um telefone válido.')
        return True
    else:
        print(f'{telefone} não é um telefone válido.')
        return False
def verificador_de_cpf(cpf):
    if re.match(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$', cpf):
        print(f'{cpf} é um CPF válido.')
        return True
    else:
        print(f'{cpf} não é um CPF válido.')
        return False

for email, telefone, cpf in zip(dados['emails'], dados['telefones'], dados['cpfs']):
    verificador_de_email(email)
    verificador_de_telefone(telefone)
    verificador_de_cpf(cpf)
