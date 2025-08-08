import os
cadastro_client = {}

def cadastro_banco(nome_cliente,idade_cliente,cpf_cliente, telefone,veiculo_cadastro,veiculo_defeito):
    
    cadastro_client[cpf_cliente] = {
        
        'Cliente': nome_cliente,
        'Idade': idade_cliente,
        'Telefone': telefone,
        'Veiculo': veiculo_cadastro,
        'Defeito': veiculo_defeito
    }
    
    return f"Cliente: {nome_cliente}\nIdade: {idade_cliente}\nTelefone: {telefone}\nVeiculo: {veiculo_cadastro}\nDefeito: {veiculo_defeito}\n\n"
    
def cadastro_f_orçamento():
    pass
# def cadastro_orçamento():
#     cadastro_client[cpf_cliente][] = {

#         "Valor_serviço": service
#     }

