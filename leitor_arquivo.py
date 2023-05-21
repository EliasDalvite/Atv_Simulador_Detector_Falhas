margem_seguranca = 150
quantidade_processos = 10
ids_anterior = []
ids_saida = []

for i in range(0, quantidade_processos):
    ids_anterior.append({"v1": -99})

for i in range(0, quantidade_processos):
    ids_saida.append({})


def le_arquivo():
    cont = 0
    with open("trace2.log", 'r') as trace2:
        for linha in trace2:
            global ids_anterior
            v = linha.split()
            objeto = {"v1": v[0], "v2": v[1], "v3": v[2], "v4": v[3], "v5": v[4]}
            if ids_anterior[int(objeto["v1"])]["v1"] == -99:
                ids_anterior[int(objeto["v1"])] = objeto
            else:
                calcula_dif(objeto)
            cont += 1
            if cont > 1000:
                return


def calcula_dif(objeto):
    global ids_anterior
    global ids_saida

    ids_saida[int(objeto["v1"])] = {"id": int(objeto["v1"]),
                                    "margem_de_seguranca": margem_seguranca,
                                    "numero_erros_detector": numero_erros_detector(objeto),
                                    "tempo_erro_detector_id": tempo_erro_detector_id(objeto),
                                    "tempo_total_do_id": tempo_total_do_id(objeto),
                                    "taxa_de_erros_id": taxa_de_erros_id(objeto),
                                    "prob_acuracia": prob_acuracia(objeto)}


def numero_erros_detector(obj):
    return


def tempo_erro_detector_id(obj):
    return


def tempo_total_do_id(obj):
    return


def taxa_de_erros_id(obj):
    return


def prob_acuracia(obj):
    return


    # global ids_anterior
    #
    # anterior = ids_anterior[int(tempo["v1"])]["v2"]
    # novo = tempo["v2"]
    # for indice, objeto in dados.iterrows():


le_arquivo()
# printa_saida(saida)
