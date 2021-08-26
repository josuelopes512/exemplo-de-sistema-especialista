def consulta(categoria, lancamento, origem):
    categoria = categoria if categoria in ['Ação', 'Comedia', 'Romance', 'Terror', 'Ficção cientifica', 'Aventura','Novela', 'Fantasia'] else 'Nulo'
    origem = origem if origem in ['nacional', 'internacional'] else 'Nulo'
    lancamento = lancamento if type(lancamento) == int and (lancamento < 2012 or lancamento > 2012) else 'Nulo'

    if categoria == 'Nulo' or origem == 'Nulo' or lancamento == 'Nulo':
        return 'Erro'

    if(categoria=="Ação"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Acerto de Contas'
            if origem == 'internacional':
                return 'The flash'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'Cidade dos Homens'
            if origem == 'internacional':
                return 'Smallville'


    if(categoria=="Comedia"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Politicamente incorreto'
            if origem == 'internacional':
                return 'Orange is the new black'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'Grande Familia'
            if origem == 'internacional':
                return 'The Big Bang Theory'

    if(categoria=="Romance"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Amor Verissimo'
            if origem == 'internacional':
                return 'Billy e billie'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'Capitu'
            if origem == 'internacional':
                return 'Mad Love'

    if(categoria=="Terror"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Contos de Edgar'
            if origem == 'internacional':
                return 'Z Nation'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'N/A'
            if origem == 'internacional':
                return 'The walking Dead'
    
    if(categoria=="Ficção cientifica"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'A mulher invisível'
            if origem == 'internacional':
                return 'Under the Done'
        if lancamento < 2012:
            if origem == 'nacional':
                return '3 por cento'
            if origem == 'internacional':
                return 'Falling Skies'

    if(categoria=="Aventura"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Xingu'
            if origem == 'internacional':
                return 'Sherlock'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'Rondon-O grande chefe'
            if origem == 'internacional':
                return 'Vikings'
    
    if(categoria=="Novela"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Dez mandamentos'
            if origem == 'internacional':
                return 'Dallas'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'Avenida Brasil'
            if origem == 'internacional':
                return 'The Royals'

    if(categoria=="Fantasia"):
        if lancamento > 2012:
            if origem == 'nacional':
                return 'Como aproveitar o fim do mundo'
            if origem == 'internacional':
                return 'Arrow'
        if lancamento < 2012:
            if origem == 'nacional':
                return 'Sitio do Pica-Pau Amarelo'
            if origem == 'internacional':
                return 'Game of Thrones'
        

print(consulta('Aventura', int('2018') , 'internacional')) # categoria: str , lancamento: int, origem: str
