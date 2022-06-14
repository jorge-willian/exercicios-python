def voto(ano_nasc):
    from datetime import date
        
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        situacao = 'NEGADO'

    elif 16 <= idade < 18 or idade > 65:
        situacao = 'OPCIONAL'
        
    else:
        situacao = 'OBRIGATÓRIO'
    
    return idade, situacao
        

print(f'''{"=" * 50}
{"EX101 - Funções para votação":^50}
{"=" * 50}''')

ano_nasc = int(input('Digite o ano de nascimento: '))
print(f'Com {voto(ano_nasc)[0]} anos: VOTO {voto(ano_nasc)[1]} ')


   