from datetime import date
import pytest
from crm.models import Lead


def test_lead_novo_comeca_com_status_novo():
    lead = Lead("Teste", "Americana", "19999999999")
    assert lead.status == "novo"


def test_mudar_status_para_valor_valido():
    lead = Lead("Teste", "Americana", "19999999999")
    lead.mudar_status("contatado")
    assert lead.status == "contatado"


def test_mudar_status_para_valor_invalido():
    lead = Lead("Teste", "Americana", "19999999999")
    with pytest.raises(ValueError):
        lead.mudar_status("banana")


def test_precia_retorno():
    lead = Lead("Teste", "Americana", "19999999999", proximo_contato=date(2026, 11, 1))
    resultado = lead.precisa_retorno(hoje=date(2026, 11, 5))
    assert resultado is True
    #aqui diz para criar um lead com retorno marcado para 01/11, e hoje é 5/11 ou seja, a data ja passou, entao tem que precisar de retorno


def test_proximo_contato():
    lead = Lead("Teste", "Americana", "19999999999", proximo_contato=date(2026, 12, 1))
    resultado = lead.precisa_retorno(hoje=date(2026, 10, 1))
    assert resultado is False
    #aqui é praticamene o contrario do anterior, estamos testando que a data de retorno ainda nao chegou, entao tem que dar false


def test_sem_data():
    lead = Lead("Teste", "Americana", "19999999999", proximo_contato=None)
    resultado = lead.precisa_retorno(hoje=date(2026, 11, 5))
    assert resultado is False
    #aqui nao temos data de retorno, entao tem que retornar falso, pois nao existe data


def test_status_fechado():
    lead = Lead("Teste", "Americana", "19999999999", status="fechado", proximo_contato=date(2026, 11, 19))
    resultado = lead.precisa_retorno(hoje=date(2026, 11, 23))
    assert resultado is False
    #aqui o resultafdo tem que ser falso pois ja fechamos a venda antes da data de retorno, ou seja, se fechamos nao precisa retornar, pois ja vendemos

