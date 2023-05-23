import logger

margem_seguranca = 150 * 1000000
quantidade_processos = 10
ids_anterior = []
ids_inicial = []
ids_saida = []
heartbeat = []
erro = False

for i in range(0, quantidade_processos):
    ids_anterior.append({"v1": -99})

for i in range(0, quantidade_processos):
    ids_saida.append({"id": -99,
                      "margem_de_seguranca": margem_seguranca,
                      "numero_erros_detector": 0,
                      "tempo_erro_detector_id": 0,
                      "tempo_total_do_id": 0,
                      "taxa_de_erros_id": 0.0,
                      "prob_acuracia": 0.0, })

for i in range(0, quantidade_processos):
    ids_inicial.append({"tempo_inicial": 0})


def le_arquivo():
    with open("trace.log", 'r') as trace2:
        for linha in trace2:
            global ids_anterior
            v = linha.split()
            objeto = {"v1": v[0], "v2": v[1], "v3": v[2], "v4": v[3], "v5": v[4]}
            if ids_anterior[int(objeto["v1"])]["v1"] == -99:
                ids_inicial[int(objeto["v1"])]["tempo_inicial"] = int(objeto["v3"])
                ids_anterior[int(objeto["v1"])] = objeto
            else:
                calcula_dif(objeto)


def calcula_dif(objeto):
    global ids_anterior
    global ids_saida
    global erro
    erro = False

    if int(objeto["v3"]) - int(ids_anterior[int(objeto["v1"])]["v3"]) > margem_seguranca:
        erro = True

    ids_saida[int(objeto["v1"])] = {"id": int(objeto["v1"]),
                                    "margem_de_seguranca": margem_seguranca,
                                    "numero_erros_detector": numero_erros_detector(objeto),
                                    "tempo_erro_detector_id": tempo_erro_detector_id(objeto),
                                    "tempo_total_do_id": tempo_total_do_id(objeto),
                                    "taxa_de_erros_id": taxa_de_erros_id(objeto),
                                    "prob_acuracia": prob_acuracia(objeto)}
    ids_anterior[int(objeto["v1"])] = objeto


def numero_erros_detector(obj):
    if erro is True:
        return ids_saida[int(obj["v1"])]["numero_erros_detector"] + 1
    else:
        return ids_saida[int(obj["v1"])]["numero_erros_detector"]


def tempo_erro_detector_id(obj):
    global ids_anterior
    if erro is True:
        return ids_saida[int(obj["v1"])]["tempo_erro_detector_id"] + (int(obj["v3"]) - int(ids_anterior[int(obj["v1"])]
                                                                                           ["v3"]))
    else:
        return ids_saida[int(obj["v1"])]["tempo_erro_detector_id"]


def tempo_total_do_id(obj):
    global ids_inicial
    return -(int(ids_inicial[int(obj["v1"])]["tempo_inicial"]) - int(obj["v3"]))


def taxa_de_erros_id(obj):
    global ids_saida
    if float(ids_saida[int(obj["v1"])]["tempo_total_do_id"]) != 0:
        return float(ids_saida[int(obj["v1"])]["numero_erros_detector"]) \
            / float(ids_saida[int(obj["v1"])]["tempo_total_do_id"]) \
            / 1000000000
    else:
        return 0.0


def prob_acuracia(obj):
    return 1
    # probabilidade de acurácia(pa0 do id = tempo de erro do id / tempo total do id (mostrar 1 - pa)


def printa_saida():
    global ids_saida
    for it in range(0, quantidade_processos):
        var_id = ids_saida[it]["id"]
        var_margem_de_seguranca = ids_saida[it]["margem_de_seguranca"]
        var_numero_erros_detector = ids_saida[it]["numero_erros_detector"]
        var_tempo_erro_detector_id = ids_saida[it]["tempo_erro_detector_id"]
        var_tempo_total_do_id = ids_saida[it]["tempo_total_do_id"]
        var_taxa_de_erros_id = ids_saida[it]["taxa_de_erros_id"]
        var_prob_acuracia = ids_saida[it]["prob_acuracia"]
        logger.loga_info(f"{var_id}-{var_margem_de_seguranca}-{var_numero_erros_detector}-{var_tempo_erro_detector_id}-"
                         f"{var_tempo_total_do_id}-{var_taxa_de_erros_id}-{var_prob_acuracia}")


le_arquivo()
printa_saida()
