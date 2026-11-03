from datetime import date
from crm.models import Lead
from crm.database import conectar, criar_tabela, inserir_lead, listar_leads


def test_inserir_lead_devolve_id():
    conexao = conectar(":memory:")
    criar_tabela(conexao)
    lead = Lead("Teste", "Americana", "19999999999")
    # TODO: chame inserir_lead e afirme que id devolvido é 1
    id_novo = inserir_lead(conexao, lead)
    assert id_novo == 1


def test_listar_inserido():
    conexao = conectar(":memory:")
    criar_tabela(conexao)
    lead = Lead("Teste", "Americana", "19999999999")
    inserir_lead(conexao, lead)
    resultado = listar_leads(conexao)
    assert len(resultado) == 1
    assert resultado[0].empresa == "Teste"


def test_data_volta_como_date():
    #nome começa com test pra que o pytest encontre o teste
    conexao = conectar(":memory:") #cria um banco temporario
    criar_tabela(conexao) #cria uma tabela leads no banco novo, sem esse nao da pra usar o inserir_lead
    lead = Lead("Teste", "Americana", "19999999999", proximo_contato=date(2026, 11, 20)) #aqui estamos definindo uma data pro lead pra usar no teste
    inserir_lead(conexao, lead) # grava o lead no banco de dados temporario que criamos
    resultado = listar_leads(conexao) # le o banco de dados e devolve o texto da data e o listar leads converte de novo pra date
    assert resultado[0].proximo_contato == date(2026, 11, 20)


def test_data_sem_volta():
    conexao = conectar(":memory:")
    criar_tabela(conexao)
    lead = Lead("Teste", "Americana", "19999999999", proximo_contato=None) 
    inserir_lead(conexao, lead)
    resultado = listar_leads(conexao)
    assert resultado[0].proximo_contato is None