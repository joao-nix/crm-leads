from datetime import date

STATUS_VALIDOS = [
        "novo",
        "contatado",
        "respondeu",
        "proposta_enviada",
        "fechado",
        "perdido",
]


class Lead:
    def __init__(self, empresa, cidade, contato, observacao="", status="novo", proximo_contato=None):
        self.empresa = empresa
        self.cidade = cidade
        self.contato = contato
        self.observacao = observacao
        self.status = status
        self.proximo_contato = proximo_contato


    def mudar_status(self, novo_status):
        if novo_status not in STATUS_VALIDOS:
            raise ValueError(f"Status invalido: {novo_status}. Use um de {STATUS_VALIDOS}")
        else:
            self.status = novo_status
        #aqui poderia deixar sem o else pois a função só chegaria no self caso o if fosse invalido.


    def precisa_retorno(self, hoje=None):
        if hoje is None:
            hoje = date.today()
            #aqui estamos falando "se hoje nao tem valor, troque hoje pela data de hoje"
        
        if self.proximo_contato is None:
            return False

        if self.proximo_contato > hoje:
            return False
        #se proximo contato for nos proximos dias retornara falso, pois queremos saber de hoje

        if self.status in ["fechado", "perdido"]:
            return False

        return True
        #se nao for nenhum dos outros retornara true

