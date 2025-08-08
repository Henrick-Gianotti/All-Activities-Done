import os
import pprint

register = {}
serviços = {}

def banco_clientes(nome_cliente, idade_cliente, cpf_cliente, telefone, chassi, veiculo_placa, veiculo_ano):
    
    register[cpf_cliente] = {
        "info_cliente": {

            "Cliente": nome_cliente,
            "Idade": idade_cliente,
            "Telefone": telefone,
            "Placa do veículo": veiculo_placa,
            "Ano do veículo": veiculo_ano,
            "Chassi do veículo": chassi
            }
    }
    print(f"CPF: {cpf_cliente}")
    print("Informações do Cliente:",f"\nCPF: {cpf_cliente}")
    for key, value in register[cpf_cliente]["info_cliente"].items():
        print(f"  {key.capitalize()}: {value}")


def banco_service(cpf_cliente, service, peça, orçamento):

    if cpf_cliente in register:
        if "serviços" in register[cpf_cliente]:
            if "contador_serviços" in register[cpf_cliente]:
                contador_serviços = register[cpf_cliente]["contador_serviços"] + 1
            else:
                contador_serviços = 1
            register[cpf_cliente]["serviços"].append({

                f"serviço {contador_serviços}": {
                    "serviço": service,
                    "peça": peça,
                    "orçamento": orçamento
                }
            })
            register[cpf_cliente]["contador_serviços"] = contador_serviços
        else:
            register[cpf_cliente]["serviços"] = [{
                "serviço 1": {
                "serviço": service,
                "peça": peça,
                "orçamento": orçamento
                }
            }]
            register[cpf_cliente]["contador_serviços"] = 1
    else:
        print("---CPF não existe!---")
        print("Não é possível cadastrar serviço sem um CPF cadastrado.")

    return register

