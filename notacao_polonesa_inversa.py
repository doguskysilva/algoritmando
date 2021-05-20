from collections import deque

def ordem_precedencia_eh_maior(simbolo_atual, simbolo_ultimo) -> bool:
    operacoes = { '+': 1, '-': 1, '*': 2, '/': 2, '^': 3 }
    return operacoes.get(simbolo_atual, -1) > operacoes.get(simbolo_ultimo, -1)

def organiza_expressao(expressao: str) -> str:
    expressao = expressao.replace(" ", "")
    expressao_organizada = ''
    for index, caractere in enumerate(expressao):
        if index == 0 and (caractere.isnumeric() or caractere.isalpha()):
            expressao_organizada += caractere
        elif not caractere.isnumeric() and not caractere.isalpha():
            if index == 0:
                expressao_organizada += caractere + " "
            elif expressao[index - 1].isnumeric() or expressao[index - 1].isalpha():
                expressao_organizada += " " + caractere + " "
            else:
                expressao_organizada += caractere + " "
        else:
            expressao_organizada += caractere
    return expressao_organizada

def notacao_polonesa_reversa(expressao) -> list:
    tokens = organiza_expressao(expressao).split(" ")
    Q = deque()
    rpn = []

    for token in tokens:
        if token.isalpha() or token.isnumeric():
            rpn.append(token)
        else:
            if not Q:
                Q.append(token)
            elif token == '(':
                Q.append(token)
            elif token == ')':
                while (len(Q) > 0 and Q[-1] != '('):
                    rpn.append(Q.pop())
                Q.pop()
            elif ordem_precedencia_eh_maior(token, Q[-1]):
                Q.append(token)
            else:
                while (len(Q) > 0 and ordem_precedencia_eh_maior(token, Q[-1]) == False):
                    rpn.append(Q.pop())
                Q.append(token)
    while Q:
        rpn.append(Q.pop())

    return rpn

def converte_expressao_em_notacao_polonesa_reversa(expressao) -> str:
    expressao_organizada = organiza_expressao(expressao)
    npr = " ".join(notacao_polonesa_reversa(expressao_organizada))

    return expressao_organizada + " <=> " + npr

# print(converte_expressao_em_notacao_polonesa_reversa('3*3'))
# print(converte_expressao_em_notacao_polonesa_reversa('3*10'))
# print(converte_expressao_em_notacao_polonesa_reversa('3 * 15'))
# print(converte_expressao_em_notacao_polonesa_reversa('2 - 3 * 5 + 4'))
# print(converte_expressao_em_notacao_polonesa_reversa('2 + 31 * 5 - 4'))
# print(converte_expressao_em_notacao_polonesa_reversa('A(1+2*3)/ 4'))
# print(converte_expressao_em_notacao_polonesa_reversa('a+b*(c^d-e)^(f+g*h)-i'))
# print(converte_expressao_em_notacao_polonesa_reversa('(4 + (7 * 4 )) + 12 / 3'))
print(converte_expressao_em_notacao_polonesa_reversa('(A+B) * (C-D)'))