import sqlite3
from datetime import date


from crm.models import Lead


def conectar(caminho="data/leads.db"):
    return sqlite3.connect(caminho)


def criar_tabela(conexao):
    conexao.execute(
        """
        Create Table if not exists leads(
            id integer primary key autoincrement,
            empresa text not null,
            cidade text,
            contato text,
            observacao text,
            status text not null,
            proximo_contato text
        )
        """
    )
    conexao.commit()


def inserir_lead(conexao, lead):
    # TODO: insert na tabela leads com os campos do lead, uadno "?".
    # converter proximo_contato para texto (ou None) e dar commit.
    # devolva o id do novo registro (cursor.lastrowid).
    data = lead.proximo_contato.isoformat() if lead.proximo_contato else None
    cursor = conexao.execute(
        "INSERT INTO Leads (empresa, cidade, contato, observacao, status, proximo_contato) VALUES (?, ?, ?, ?, ?, ?)",
        (lead.empresa, lead.cidade, lead.contato, lead.observacao, lead.status, data),
    )
    conexao.commit()
    return cursor.lastrowid


def listar_leads(conexao):
    # TODO: select dos leads, tranforamr cada linha em um objeto Lead
    # e devolver uma lista. Lembre de converter o texto de volta para date.
    linhas = conexao.execute(
        "SELECT empresa, cidade, contato, observacao, status, proximo_contato FROM Leads"
    ).fetchall()

    Leads = []
    for empresa, cidade,contato, observacao, status, data in linhas:
        proximo_contato = date.fromisoformat(data) if data else None
        Leads.append(Lead(empresa, cidade, contato, observacao, status, proximo_contato))
    return Leads

