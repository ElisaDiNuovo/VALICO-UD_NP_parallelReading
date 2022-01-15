# Author = Elisa Di Nuovo
# I want to thank Dr. Mirko Lai and Davide Colla for their help. All the mess is mine.

from collections import Counter


def diff_LS(list1, list2):
    return list((Counter(list1) - Counter(list2)).elements())


def diff_TH(list1, list2):
    return list((Counter(list2) - Counter(list1)).elements())

# all 36 texts
fLS = open("it_valico-ud-test.conllu")
fTH = open("it_thvalico-ud-test.conllu")

# only DE L1 texts
# fLS = open("L1wise_data/ls_1st-release_DE.conllu")
# fTH = open("L1wise_data/th_1st-release_DE.conllu")

# only EN L1 texts
# fLS = open("L1wise_data/ls_1st-release_EN.conllu")
# fTH = open("L1wise_data/th_1st-release_EN.conllu")

# only ES L1 texts
# fLS = open("L1wise_data/ls_1st-release_ES.conllu")
# fTH = open("L1wise_data/th_1st-release_ES.conllu")

# only FR L1 texts
# fLS = open("L1wise_data/ls_1st-release_FR.conllu")
# fTH = open("L1wise_data/th_1st-release_FR.conllu")

lineLS = None
lineTH = None

singola_fraseLS = []
singola_fraseTH = []

noun_LS_morph = []
det_LS_morph = []
adj_LS_morph = []

det_adj_noun_LS_morph = []
det_adj_noun_TH_morph = []

noun_TH_morph = []
det_TH_morph = []
adj_TH_morph = []

det_dx_LS = 0
det_sx_LS = 0
adj_dx_LS = 0
adj_sx_LS = 0
det_dx_TH = 0
det_sx_TH = 0
adj_dx_TH = 0
adj_sx_TH = 0

det_dx_LS_tot = 0
det_sx_LS_tot = 0
adj_dx_LS_tot = 0
adj_sx_LS_tot = 0
det_dx_TH_tot = 0
det_sx_TH_tot = 0
adj_dx_TH_tot = 0
adj_sx_TH_tot = 0

# calcolata sulla totalità di adj det e noun
diff_lessic_LSeTH = 0
diff_lessic_in_piu_in_LS = 0
diff_lessic_in_piu_in_TH = 0

diff_form_LSeTH = 0
coppia_form_diversa = []
form_diversa = []

end = False

while not end:
    # ciclo sulle frasi
    nomeFraseLS = None
    nomeFraseTH = None

    # nuova frase LS
    while lineLS != '\n':
        lineLS = fLS.readline()
        if not lineLS:
            end = True
            break
        if lineLS.startswith('# sent_id ='):
            nomeFraseLS = lineLS.strip().split('# sent_id =')[1]
            singola_fraseLS = []
            noun_LS_morph_frase = []
            noun_LS_morph_frase.append(nomeFraseLS.strip())
            det_LS_morph_frase = []
            adj_LS_morph_frase = []
            continue
        elif lineLS.startswith("# text ="):
            continue
        elif lineLS.startswith("# err ="):
            continue
        elif lineLS != '\n':
            singola_fraseLS.append(lineLS)
            continue
        else:
            continue

    # nuova frase TH
    while lineTH != '\n':
        lineTH = fTH.readline()
        if not lineTH:
            end = True
            break
        if lineTH.startswith('# sent_id ='):
            nomeFraseTH = lineTH.strip().split('# sent_id =')[1]
            singola_fraseTH = []
            noun_TH_morph_frase = []
            noun_TH_morph_frase.append(nomeFraseTH.strip())
            det_TH_morph_frase = []
            adj_TH_morph_frase = []
            continue
        elif lineTH.startswith("# text ="):
            continue
        elif lineTH.startswith("# err ="):
            continue
        elif lineTH != '\n':
            singola_fraseTH.append(lineTH)
            continue

    ############################################################
    ################ posso confrontare la frasi ################
    ############################################################

    if lineLS == '\n' and lineTH == '\n':

        # print(singola_fraseLS,singola_fraseTH)

        # controllo che l'id della frase LS sia uguale a quello della frase TH
        # if nomeFraseLS != nomeFraseTH:
        #     print(nomeFraseLS,nomeFraseTH)

        # creo le liste per i nomi, det e adj per frase
        nomi_in_LS = []
        adj_in_LS = []
        det_in_LS = []

        det_adj_noun_LS = []
        det_adj_noun_LS_form = []
        det_adj_noun_LS_morph_frase = []

        # azzero le variabili che conto per frase
        errore_lessicale_per_frase = 0
        detLS_in_piu = 0
        det_dx_LS = 0
        det_sx_LS = 0
        adj_dx_LS = 0
        adj_sx_LS = 0
        indice_nomeLS = None
        genere_nomeLS = None
        numero_nomeLS = None
        lemma_nomeLS = None
        nomeLS = None

        for tokenLS in singola_fraseLS:
            indice_nomeLS = None
            genere_nomeLS = None
            numero_nomeLS = None
            lemma_nomeLS = None
            nomeLS = None
            noun_LS_singolo = []
            det_LS_singolo = []
            adj_LS_singolo = []

            singola_colonnaLS = tokenLS.strip().split('\t')

            if singola_colonnaLS[3] == 'NOUN':  # verifichiamo se il token è un nome NOUN
                # print(singola_colonnaLS, nomeFraseLS)
                nomi_in_LS.append(singola_colonnaLS[2])
                det_adj_noun_LS.append(singola_colonnaLS[2])
                det_adj_noun_LS_form.append(singola_colonnaLS[1])
                nomeLS = singola_colonnaLS[1]
                lemma_nomeLS = singola_colonnaLS[2]
                indice_nomeLS = singola_colonnaLS[0]

                # in caso il nome o l'aggettivo non abbia il genere o il numero rimane None

                # trovo genere e numero nome
                for morfologia in singola_colonnaLS[5].split('|'):
                    if morfologia.startswith('Gender'):
                        genere_nomeLS = morfologia
                    if morfologia.startswith('Number'):
                        numero_nomeLS = morfologia

                # creo la lista del nome singolo
                noun_LS_singolo.append(lemma_nomeLS)
                noun_LS_singolo.append(indice_nomeLS)
                noun_LS_singolo.append(genere_nomeLS)
                noun_LS_singolo.append(numero_nomeLS)

                # cerco la presenza di dipendenti DET or ADJ del nome
                for token in singola_fraseLS:
                    if det_LS_singolo:
                        det_LS_morph_frase.append(det_LS_singolo)
                    det_LS_singolo = []

                    detLS = None
                    indice_detLS = None
                    genere_detLS = None
                    numero_detLS = None
                    head_detLS = None
                    if token.split('\t')[6] == indice_nomeLS:

                        # vedo se è un DET e mi salvo le info
                        if 'DET' in token.split('\t')[3] and 'DE' not in token.split('\t')[4]:
                            # se il nome non ha dipendenti non lo aggiungo alla lista
                            # con i nomi della frase, se tra i dipendenti ha un DET lo aggiungo

                            if noun_LS_singolo not in noun_LS_morph_frase:
                                noun_LS_morph_frase.append(noun_LS_singolo)

                            det_in_LS.append(token.split('\t')[2])
                            det_adj_noun_LS.append(token.split('\t')[2])
                            det_adj_noun_LS_form.append(token.split('\t')[1])
                            detLS = token.split('\t')[2]
                            singolo_detLS = token
                            indice_detLS = token.split('\t')[0]
                            head_detLS = token.split('\t')[6]
                            det_LS_singolo.append(detLS)
                            det_LS_singolo.append(head_detLS)
                            for morfologia in token.split('\t')[5].split('|'):
                                if morfologia.startswith('Gender'):
                                    genere_detLS = morfologia
                                    det_LS_singolo.append(morfologia)
                                if morfologia.startswith('Number'):
                                    numero_detLS = morfologia
                                    det_LS_singolo.append(morfologia)
                            det_LS_singolo.append(token.split('\t')[4])

                            if genere_detLS is None:
                                det_LS_singolo = []
                                det_LS_singolo.append(detLS)
                                det_LS_singolo.append(head_detLS)
                                det_LS_singolo.append('Gender=None')
                                det_LS_singolo.append(numero_detLS)
                                det_LS_singolo.append(token.split('\t')[4])

                    # controllo se i det sono prima o dopo il nome e li conto
                    if indice_detLS is not None:
                        if int(indice_detLS) > int(head_detLS):
                            det_dx_LS += 1
                        if int(indice_detLS) < int(head_detLS):
                            det_sx_LS += 1

                # cerco gli ADJ che dipendono da NOUN

                for token in singola_fraseLS:
                    if adj_LS_singolo:
                        adj_LS_morph_frase.append(adj_LS_singolo)
                    adj_LS_singolo = []

                    # in caso non ci sia un ADJ dipendente da NOUN
                    adjLS = None
                    genere_adjLS = None
                    numero_adjLS = None
                    lemma_adjLS = None
                    indice_adjLS = None
                    head_adjLS = None
                    if token.split('\t')[6] == indice_nomeLS:
                        # vedo se è un ADJ e mi salvo le info
                        if 'ADJ' in token.split('\t')[3] and token.split('\t')[7] != 'conj':
                            # se il nome da cui dipende l'adj non è già in lista lo aggiungo
                            if noun_LS_singolo not in noun_LS_morph_frase:
                                noun_LS_morph_frase.append(noun_LS_singolo)
                            # print(token)
                            adj_in_LS.append(token.split('\t')[2])
                            det_adj_noun_LS.append(token.split('\t')[2])
                            det_adj_noun_LS_form.append(token.split('\t')[1])
                            adjLS = token.split('\t')[2]
                            singolo_adjLS = token
                            indice_adjLS = token.split('\t')[0]
                            head_adjLS = token.split('\t')[6]
                            adj_LS_singolo.append(adjLS)
                            adj_LS_singolo.append(head_adjLS)
                            for morfologia in token.split('\t')[5].split('|'):
                                if morfologia.startswith('Gender'):
                                    genere_adjLS = morfologia
                                    adj_LS_singolo.append(morfologia)
                                if morfologia.startswith('Number'):
                                    numero_adjLS = morfologia
                                    adj_LS_singolo.append(morfologia)

                            if genere_adjLS is None:
                                adj_LS_singolo = []
                                adj_LS_singolo.append(adjLS)
                                adj_LS_singolo.append(head_adjLS)
                                adj_LS_singolo.append('Gender=None')
                                adj_LS_singolo.append(numero_adjLS)
                            # print(adjLS, indice_adjLS, genere_adjLS, numero_adjLS)

                    # controllo se gli adj sono prima o dopo il nome e li conto
                    if indice_adjLS is not None:
                        if int(indice_adjLS) > int(head_adjLS):
                            adj_dx_LS += 1
                        if int(indice_adjLS) < int(head_adjLS):
                            adj_sx_LS += 1

        # creo una lista di liste contenente tutti i nomi, gli aggettivi e i determinanti separatamente e una insieme
        noun_LS_morph.append(noun_LS_morph_frase)
        det_LS_morph.append(det_LS_morph_frase)
        adj_LS_morph.append(adj_LS_morph_frase)

        det_adj_noun_LS_morph_frase.append(noun_LS_morph_frase)
        det_adj_noun_LS_morph_frase.append(det_LS_morph_frase)
        det_adj_noun_LS_morph_frase.append(adj_LS_morph_frase)

        # print(det_adj_noun_LS_morph_frase)
        det_adj_noun_LS_morph.append(det_adj_noun_LS_morph_frase)

        ##################################################
        ##############       PARTE TH        #############
        ##################################################

        # creo le liste per i nomi, det e adj per frase
        nomi_in_TH = []
        adj_in_TH = []
        det_in_TH = []

        det_adj_noun_TH = []
        det_adj_noun_TH_form = []
        det_adj_noun_TH_morph_frase = []

        # azzero le variabili che conto per frase
        errore_lessicale_per_frase = 0
        detTH_in_piu = 0
        det_dx_TH = 0
        det_sx_TH = 0
        adj_dx_TH = 0
        adj_sx_TH = 0
        indice_nomeTH = None
        genere_nomeTH = None
        numero_nomeTH = None
        lemma_nomeTH = None
        nomeTH = None

        for tokenTH in singola_fraseTH:
            indice_nomeTH = None
            genere_nomeTH = None
            numero_nomeTH = None
            lemma_nomeTH = None
            nomeTH = None
            noun_TH_singolo = []
            det_TH_singolo = []
            adj_TH_singolo = []

            singola_colonnaTH = tokenTH.strip().split('\t')

            if singola_colonnaTH[3] == 'NOUN':  # verifichiamo se il token è un nome NOUN
                # print(singola_colonnaTH, nomeFraseTH)
                nomi_in_TH.append(singola_colonnaTH[2])
                det_adj_noun_TH.append(singola_colonnaTH[2])
                det_adj_noun_TH_form.append(singola_colonnaTH[1])
                nomeTH = singola_colonnaTH[1]
                lemma_nomeTH = singola_colonnaTH[2]
                indice_nomeTH = singola_colonnaTH[0]

                # in caso il nome o l'aggettivo non abbia il genere o il numero rimane None

                # trovo genere e numero nome
                for morfologia in singola_colonnaTH[5].split('|'):
                    if morfologia.startswith('Gender'):
                        genere_nomeTH = morfologia
                    if morfologia.startswith('Number'):
                        numero_nomeTH = morfologia

                # creo la lista del nome singolo
                noun_TH_singolo.append(lemma_nomeTH)
                noun_TH_singolo.append(indice_nomeTH)
                noun_TH_singolo.append(genere_nomeTH)
                noun_TH_singolo.append(numero_nomeTH)

                # cerco la presenza di dipendenti DET or ADJ del nome
                for token in singola_fraseTH:
                    if det_TH_singolo:
                        det_TH_morph_frase.append(det_TH_singolo)
                    det_TH_singolo = []

                    detTH = None
                    indice_detTH = None
                    genere_detTH = None
                    numero_detTH = None
                    head_detTH = None
                    if token.split('\t')[6] == indice_nomeTH:

                        # vedo se è un DET e mi salvo le info
                        if 'DET' in token.split('\t')[3] and 'DE' not in token.split('\t')[4]:
                            # se il nome non ha dipendenti non lo aggiungo alla lista
                            # con i nomi della frase, se tra i dipendenti ha un DET lo aggiungo
                            if noun_TH_singolo not in noun_TH_morph_frase:
                                noun_TH_morph_frase.append(noun_TH_singolo)

                            det_in_TH.append(token.split('\t')[2])
                            det_adj_noun_TH.append(token.split('\t')[2])
                            det_adj_noun_TH_form.append(token.split('\t')[1])
                            detTH = token.split('\t')[2]
                            singolo_detTH = token
                            indice_detTH = token.split('\t')[0]
                            head_detTH = token.split('\t')[6]
                            det_TH_singolo.append(detTH)
                            det_TH_singolo.append(head_detTH)
                            for morfologia in token.split('\t')[5].split('|'):
                                if morfologia.startswith('Gender'):
                                    genere_detTH = morfologia
                                    det_TH_singolo.append(morfologia)
                                if morfologia.startswith('Number'):
                                    numero_detTH = morfologia
                                    det_TH_singolo.append(morfologia)
                            det_TH_singolo.append(token.split('\t')[4])

                            if genere_detTH is None:
                                det_TH_singolo = []
                                det_TH_singolo.append(detTH)
                                det_TH_singolo.append(head_detTH)
                                det_TH_singolo.append('Gender=None')
                                det_TH_singolo.append(numero_detTH)
                                det_TH_singolo.append(token.split('\t')[4])

                            # print('qvi')
                            # print(det_TH_singolo)
                    # print(detTH, indice_detTH, genere_detTH, numero_detTH)

                    # controllo se i det sono prima o dopo il nome e li conto
                    if indice_detTH is not None:
                        if int(indice_detTH) > int(head_detTH):
                            det_dx_TH += 1
                        if int(indice_detTH) < int(head_detTH):
                            det_sx_TH += 1

                # cerco gli ADJ che dipendono da NOUN

                for token in singola_fraseTH:
                    if adj_TH_singolo:
                        adj_TH_morph_frase.append(adj_TH_singolo)
                    adj_TH_singolo = []

                    # in caso non ci sia un ADJ dipendente da NOUN
                    adjTH = None
                    genere_adjTH = None
                    numero_adjTH = None
                    lemma_adjTH = None
                    indice_adjTH = None
                    head_adjTH = None
                    if token.split('\t')[6] == indice_nomeTH:
                        # vedo se è un ADJ e mi salvo le info
                        if 'ADJ' in token.split('\t')[3] and token.split('\t')[7] != 'conj':
                            # se il nome da cui dipende l'adj non è già in lista lo aggiungo
                            if noun_TH_singolo not in noun_TH_morph_frase:
                                noun_TH_morph_frase.append(noun_TH_singolo)
                            # print(token)
                            adj_in_TH.append(token.split('\t')[2])
                            det_adj_noun_TH.append(token.split('\t')[2])
                            det_adj_noun_TH_form.append(token.split('\t')[1])
                            adjTH = token.split('\t')[2]
                            singolo_adjTH = token
                            indice_adjTH = token.split('\t')[0]
                            head_adjTH = token.split('\t')[6]
                            adj_TH_singolo.append(adjTH)
                            adj_TH_singolo.append(head_adjTH)
                            for morfologia in token.split('\t')[5].split('|'):
                                if morfologia.startswith('Gender'):
                                    genere_adjTH = morfologia
                                    adj_TH_singolo.append(morfologia)
                                if morfologia.startswith('Number'):
                                    numero_adjTH = morfologia
                                    adj_TH_singolo.append(morfologia)
                            if genere_adjTH is None:
                                adj_TH_singolo = []
                                adj_TH_singolo.append(adjTH)
                                adj_TH_singolo.append(head_adjTH)
                                adj_TH_singolo.append('Gender=None')
                                adj_TH_singolo.append(numero_adjTH)
                            # print(adjTH, indice_adjTH, genere_adjTH, numero_adjTH)

                    # controllo se gli adj sono prima o dopo il nome e li conto
                    if indice_adjTH is not None:
                        if int(indice_adjTH) > int(head_adjTH):
                            adj_dx_TH += 1
                        if int(indice_adjTH) < int(head_adjTH):
                            adj_sx_TH += 1

        # creo una lista di liste
        noun_TH_morph.append(noun_TH_morph_frase)
        det_TH_morph.append(det_TH_morph_frase)
        adj_TH_morph.append(adj_TH_morph_frase)

        det_adj_noun_TH_morph_frase.append(noun_TH_morph_frase)
        det_adj_noun_TH_morph_frase.append(det_TH_morph_frase)
        det_adj_noun_TH_morph_frase.append(adj_TH_morph_frase)

        # print(det_adj_noun_TH_morph_frase)
        det_adj_noun_TH_morph.append(det_adj_noun_TH_morph_frase)

        ################################################################
        ##### Controllo se ci sono differenze di token tra LS e TH #####
        ################################################################

        if diff_LS(det_adj_noun_LS, det_adj_noun_TH):
            print('in più in LS', diff_LS(det_adj_noun_LS, det_adj_noun_TH), nomeFraseLS)
            diff_lessic_LSeTH += len(diff_LS(det_adj_noun_LS, det_adj_noun_TH))
            diff_lessic_in_piu_in_LS += len(diff_LS(det_adj_noun_LS, det_adj_noun_TH))

        if diff_TH(det_adj_noun_LS, det_adj_noun_TH):
            print('in più in TH', diff_TH(det_adj_noun_LS, det_adj_noun_TH), nomeFraseLS)
            diff_lessic_LSeTH += len(diff_TH(det_adj_noun_LS, det_adj_noun_TH))
            diff_lessic_in_piu_in_TH += len(diff_TH(det_adj_noun_LS, det_adj_noun_TH))

        ################################################################
        ######## Controllo anche errori ortografici tra LS e TH ########
        ################################################################
        # todo: sistemare lista form_diversa

        if coppia_form_diversa and coppia_form_diversa not in form_diversa:
            form_diversa.append(coppia_form_diversa)

        if diff_LS(det_adj_noun_LS_form, det_adj_noun_TH_form):
            print('diverso in LS', diff_LS(det_adj_noun_LS_form, det_adj_noun_TH_form), nomeFraseLS)
            coppia_form_diversa.append(diff_LS(det_adj_noun_LS_form, det_adj_noun_TH_form))
            diff_form_LSeTH += len(diff_LS(det_adj_noun_LS_form, det_adj_noun_TH_form))

        if diff_TH(det_adj_noun_LS_form, det_adj_noun_TH_form):
            print('diverso in TH', diff_TH(det_adj_noun_LS_form, det_adj_noun_TH_form), nomeFraseLS)
            coppia_form_diversa.append(diff_TH(det_adj_noun_LS_form, det_adj_noun_TH_form))
            diff_form_LSeTH += len(diff_TH(det_adj_noun_LS_form, det_adj_noun_TH_form))

        #########################################################
        # stampo le informatizioni sui DET (a dx o sx del NOUN) #
        #########################################################
        # todo: tenere traccia delle diverse XPOS
        # ho aggiunto in posizione det[4] la XPOS

        if det_dx_LS != 0:
            print('det_dx_LS', det_dx_LS, nomeFraseLS)
            det_dx_LS_tot += det_dx_LS
        if det_sx_LS != 0:
            print('det_sx_LS', det_sx_LS, nomeFraseLS)
            det_sx_LS_tot += det_sx_LS

        if det_dx_TH != 0:
            print('det_dx_TH', det_dx_TH, nomeFraseLS)
            det_dx_TH_tot += det_dx_TH
        if det_sx_TH != 0:
            print('det_sx_TH', det_sx_TH, nomeFraseLS)
            det_sx_TH_tot += det_sx_TH

        ###########################################################
        # stampo le informatizioni sugli ADJ (a dx o sx del NOUN) #
        ###########################################################

        if adj_dx_LS != 0:
            print('adj_dx_LS', adj_dx_LS, nomeFraseLS)
            adj_dx_LS_tot += adj_dx_LS
        if adj_sx_LS != 0:
            print('adj_sx_LS', adj_sx_LS, nomeFraseLS)
            adj_sx_LS_tot += adj_sx_LS

        if adj_dx_TH != 0:
            print('adj_dx_TH', adj_dx_TH, nomeFraseLS)
            adj_dx_TH_tot += adj_dx_TH
        if adj_sx_TH != 0:
            print('adj_sx_TH', adj_sx_TH, nomeFraseLS)
            adj_sx_TH_tot += adj_sx_TH

    lineTH = None
    lineLS = None

##########################################
############### FINE CICLO ###############
##########################################

print('det dx e sx LS tot:', det_dx_LS_tot, det_sx_LS_tot)
print('det dx e sx TH tot:', det_dx_TH_tot, det_sx_TH_tot)

print('adj dx e sx LS tot:', adj_dx_LS_tot, adj_sx_LS_tot)
print('adj dx e sx TH tot:', adj_dx_TH_tot, adj_sx_TH_tot)

print('=====================================================')

print('diff_lessic_LSeTH', diff_lessic_LSeTH)
print('diff_lessic_in_piu_in_LS', diff_lessic_in_piu_in_LS)
print('diff_lessic_in_piu_in_TH', diff_lessic_in_piu_in_TH)

print('diff_form_LSeTH', int((diff_form_LSeTH)))

# uncomment to print all the form differences
# print('form_diversa', form_diversa)

######################################################################
############ Controllo se ci sono errori di accordo ##################
######################################################################
# todo: aggiungere i contatori
# ho aggiunto genere e numero nelle liste separate di adj det e noun, una lista per frase
# pos_LS_morph --> lemma, index, gender and number
# le liste di liste hanno la stessa lunghezza e sono allineate
# print(len(noun_LS_morph),len(det_LS_morph), len(adj_LS_morph))
# for noun, det, adj in zip(noun_LS_morph,det_LS_morph,adj_LS_morph):
#     print(noun,det,adj)

print('=====================================================================')
print('=============================PARTE LS================================')
print('=====================================================================')
for x, y, z in zip(noun_LS_morph, det_LS_morph, adj_LS_morph):
    for noun in x:
        if isinstance(noun, list):
            for det in y:
                if noun[1] in det:
                    if not z:
                        # if len(det) < 4:
                        #     print(det, nomeFrase)
                        # pos[2] --> gender; pos[3] --> number
                        ##### CONTROLLO GENERE E NUMERO #####
                        if noun[2] == det[2] and noun[3] == det[3] or noun[2] is None or det[2] == 'Gender=None':
                            print(nomeFrase, 'det noun: accordo di genere e numero interno LS corretto', noun, det)
                        elif noun[2] is None or det[2] == 'Gender=None':
                            print(nomeFrase, 'det o noun genere inviariabile', noun, det)
                        else:
                            if noun[2] != det[2] and noun[3] != det[3] and (
                                    det[2] != 'Gender=None' or noun[2] is not None):
                                print(nomeFrase, 'det noun: accordo di genere e numero interno LS NON corretto', noun,
                                      det)

                            ########## CONTROLLO GENERE ##########
                            if noun[2] == det[2] or det[2] == 'Gender=None' or noun[2] is None:
                                print(nomeFrase, 'det noun: accordo di genere interno LS corretto', noun, det)
                            if noun[2] != det[2] and (det[2] != 'Gender=None' or noun[2] is not None):
                                print(nomeFrase, 'det noun: accordo di genere interno LS NON corretto', noun, det)

                            ########## CONTROLLO NUMERO ##########
                            if noun[3] == det[3]:
                                print(nomeFrase, 'det noun: accordo di numero interno LS corretto', noun, det)
                            if noun[3] != det[3]:
                                print(nomeFrase, 'det noun: accordo di genere interno LS NON corretto', noun, det)

                    else:
                        for adj in z:
                            if noun[1] in adj:

                                ##### CONTROLLO GENERE E NUMERO #####
                                if noun[2] == det[2] and noun[2] == adj[2] and noun[3] == det[3] and noun[3] == adj[
                                    3] or det[2] == 'Gender=None' or adj[2] == 'Gender=None' or noun[2] is None:
                                    print(nomeFrase, 'det adj noun: accordo di genere e numero interno LS corretto',
                                          noun, det, adj)
                                elif det[2] == 'Gender=None' or adj[2] == 'Gender=None' or noun[2] is None:
                                    print(nomeFrase, 'det, adj o noun genere inviariabile', noun, det, adj)
                                else:
                                    if noun[2] != det[2] and noun[2] != adj[2] and noun[3] != det[3] and noun[3] != adj[
                                        3] and (
                                            det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
                                        print(nomeFrase,
                                              'det adj noun: accordo di genere e numero interno LS NON corretto', noun,
                                              det, adj)

                                    ########## CONTROLLO GENERE ##########
                                    if noun[2] == det[2] and noun[2] == adj[2] or det[2] == 'Gender=None' or adj[
                                        2] == 'Gender=None' or noun[2] is None:
                                        print(nomeFrase, 'det adj noun: accordo di genere interno LS corretto', noun,
                                              det, adj)
                                    if noun[2] != det[2] and noun[2] != adj[2] and (
                                            det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
                                        print(nomeFrase, 'det adj noun: accordo di genere interno LS NON corretto',
                                              noun, det, adj)
                                    if noun[2] == det[2] and noun[2] != adj[2] and (
                                            det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
                                        print(nomeFrase,
                                              'det adj noun: accordo di genere interno LS det noun corretto, noun adj NON corretto',
                                              noun, det, adj)
                                    if noun[2] != det[2] and noun[2] == adj[2] and (
                                            det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
                                        print(nomeFrase,
                                              'det adj noun: accordo di genere interno LS det noun NON corretto, noun adj corretto',
                                              noun, det, adj)

                                    ########## CONTROLLO NUMERO ##########
                                    if noun[3] == det[3] and noun[3] == adj[3]:
                                        print(nomeFrase, 'det adj noun: accordo di numero interno LS corretto', noun,
                                              det, adj)
                                    if noun[3] != det[3] and noun[3] != adj[3]:
                                        print(nomeFrase, 'det adj noun: accordo di numero interno LS NON corretto',
                                              noun, det, adj)
                                    if noun[3] == det[3] and noun[3] != adj[3]:
                                        print(nomeFrase,
                                              'det adj noun: accordo di numero interno LS det noun corretto, noun adj NON corretto',
                                              noun, det, adj)
                                    if noun[3] != det[3] and noun[3] == adj[3]:
                                        print(nomeFrase,
                                              'det adj noun: accordo di numero interno LS det noun NON corretto, noun adj corretto',
                                              noun, det, adj)

        else:
            nomeFrase = noun

# print('=====================================================================')
# print('=============================PARTE TH================================')
# print('=====================================================================')
# for x, y, z in zip(noun_TH_morph, det_TH_morph, adj_TH_morph):
#     for noun in x:
#         if isinstance(noun, list):
#             for det in y:
#                 if noun[1] in det:
#                     if not z:
#                         # if len(det) < 4:
#                         #     print(det, nomeFrase)
#                         ##### CONTROLLO GENERE E NUMERO #####
#                         if noun[2] == det[2] and noun[3] == det[3] or (noun[2] != det[2] and noun[2] is None) or (noun[2] != det[2] and det[2] == 'Gender=None'):
#                             print(nomeFrase, 'det noun: accordo di genere e numero interno TH corretto')
#                             if noun[2] is None or det[2] == 'Gender=None':
#                                 print(noun, det)
#                         if noun[2] != det[2] and noun[3] != det[3] and (det[2] != 'Gender=None' or noun[2] is not None):
#                             print(nomeFrase, 'det noun: accordo di genere e numero interno TH NON corretto')
#                             print(noun, det)
#
#                         ########## CONTROLLO GENERE ##########
#                         if noun[2] == det[2] or (noun[2] != det[2] and noun[2] is None) or (
#                                 noun[2] != det[2] and det[2] == 'Gender=None'):
#                             print(nomeFrase, 'det noun: accordo di genere interno TH corretto')
#                             if det[2] == 'Gender=None' or noun[2] is None:
#                                 print(noun, det)
#                         elif (noun[2] != det[2] and det[2] != 'Gender=None') or (
#                                 noun[2] != det[2] and noun[2] is not None):
#                             print(nomeFrase, 'det noun: accordo di genere interno TH NON corretto')
#                             print(noun, det)
#
#                         ########## CONTROLLO NUMERO ##########
#                         elif noun[3] == det[3]:
#                             print(nomeFrase, 'det noun: accordo di numero interno TH corretto')
#                         elif noun[3] != det[3]:
#                             print(nomeFrase, 'det noun: accordo di genere interno TH NON corretto')
#                             print(noun, det)
#
#                     else:
#                         for adj in z:
#                             if noun[1] in adj:
#                                 ##### CONTROLLO GENERE E NUMERO #####
#                                 if noun[2] == det[2] and noun[2] == adj[2] and noun[3] == det[3] and noun[3] == adj[3] or det[2] == 'Gender=None' or adj[2] == 'Gender=None' or noun[2] is None:
#                                     print(nomeFrase, 'det adj noun: accordo di genere e numero interno TH corretto')
#                                     print(noun, det, adj)
#                                 if noun[2] != det[2] and noun[2] != adj[2] and noun[3] != det[3] and noun[3] != adj[
#                                     3] and (det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
#                                     print(nomeFrase, 'det adj noun: accordo di genere e numero interno TH NON corretto')
#
#                                 ########## CONTROLLO GENERE ##########
#                                 if noun[2] == det[2] and noun[2] == adj[2] or det[2] == 'Gender=None' or adj[
#                                     2] == 'Gender=None' or noun[2] is None:
#                                     print(nomeFrase, 'det adj noun: accordo di genere interno TH corretto')
#                                     if det[2] == 'Gender=None' or adj[2] == 'Gender=None' or noun[2] is None:
#                                         print(noun, det, adj)
#                                 elif noun[2] != det[2] and noun[2] != adj[2] and (
#                                         det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
#                                     print(nomeFrase, 'det adj noun: accordo di genere interno TH NON corretto')
#                                 elif noun[2] == det[2] and noun[2] != adj[2] and (
#                                         det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
#                                     print(nomeFrase,
#                                           'det adj noun: accordo di genere interno TH det noun corretto, noun adj NON corretto')
#                                 elif noun[2] != det[2] and noun[2] == adj[2] and (
#                                         det[2] != 'Gender=None' or adj[2] != 'Gender=None' or noun[2] is not None):
#                                     print(nomeFrase,
#                                           'det adj noun: accordo di genere interno TH det noun NON corretto, noun adj corretto')
#
#                                 ########## CONTROLLO NUMERO ##########
#                                 elif noun[3] == det[3] and noun[3] == adj[3]:
#                                     print(nomeFrase, 'det adj noun: accordo di numero interno TH corretto')
#                                 elif noun[3] != det[3] and noun[3] != adj[3]:
#                                     print(nomeFrase, 'det adj noun: accordo di numero interno TH NON corretto')
#                                 elif noun[3] == det[3] and noun[3] != adj[3]:
#                                     print(nomeFrase,
#                                           'det adj noun: accordo di numero interno TH det noun corretto, noun adj NON corretto')
#                                 elif noun[3] != det[3] and noun[3] == adj[3]:
#                                     print(nomeFrase,
#                                           'det adj noun: accordo di numero interno TH det noun NON corretto, noun adj corretto')
#
#         else:
#             nomeFrase = noun

print("""=====================================================================
=========================CONFRONTO LS e TH===========================
=====================================================================""")
# todo: inserire i contatori
err_gender_noun = 0
err_gender_det = 0
err_number_noun = 0
err_number_det = 0

err_gender_noun_3 = 0
err_gender_det_3 = 0
err_gender_adj_3 = 0
err_number_noun_3 = 0
err_number_det_3 = 0
err_number_adj_3 = 0

# usare lista di liste det_adj_noun_[(LS)|(TH)]_morph per controllare
# [Gender, Number]noun, [Gender, Number]det, [Gender, Number]adj
nome_adj_det_LS = []
nome_adj_det_TH = []
nome_adj_det_LS_singolo = []
nome_adj_det_TH_singolo = []

nome_det_LS = []
nome_det_TH = []
nome_det_LS_singolo = []
nome_det_TH_singolo = []

i = 0
TH = det_adj_noun_TH_morph
for LS in det_adj_noun_LS_morph:

    nome_adj_det_LS_singolo = []
    nome_adj_det_TH_singolo = []
    if (LS[1] != [] and TH[i][1] != []) or (LS[2] != [] and TH[i][2] != []):
        for nomeLS in LS[0]:
            if nome_adj_det_LS_singolo:
                nome_adj_det_LS.append(nome_adj_det_LS_singolo)

            if nome_adj_det_TH_singolo:
                nome_adj_det_TH.append(nome_adj_det_TH_singolo)

            nome_adj_det_TH_singolo = []
            nome_adj_det_LS_singolo = []
            indice_nomeLS = None
            indice_nomeTH = None
            if isinstance(nomeLS, list):
                for nomeTH in TH[i][0]:
                    if nomeLS[0] == nomeTH[0]:
                        nome_adj_det_LS_singolo.append(nomeLS)
                        nome_adj_det_TH_singolo.append(nomeTH)

                        indice_nomeLS = nomeLS[1]
                        indice_nomeTH = nomeTH[1]
                        for detLS in LS[1]:
                            if detLS[1] == indice_nomeLS:
                                nome_adj_det_LS_singolo.append(detLS)

                        for detTH in TH[i][1]:
                            if detTH[1] == indice_nomeTH:
                                nome_adj_det_TH_singolo.append(detTH)

                        for adjLS in LS[2]:
                            if adjLS[1] == indice_nomeLS:
                                nome_adj_det_LS_singolo.append(adjLS)

                        for adjTH in TH[i][2]:
                            if adjTH[1] == indice_nomeTH:
                                nome_adj_det_TH_singolo.append(adjTH)
            else:
                nome_adj_det_LS_singolo.append(nomeLS)
                nome_adj_det_TH_singolo.append(nomeLS)

            # print('primo ',nome_adj_det_LS_singolo)
            # print('primo ',nome_adj_det_TH_singolo)

    if (LS[1] != [] and TH[i][1] != []) and (LS[2] == [] and TH[i][2] != []):
        for nomeLS, nomeTH in zip(LS[0], TH[i][0]):
            if not isinstance(nomeLS, list) and not isinstance(nomeTH, list):
                nome = nomeLS
                nome_adj_det_LS_singolo.append(nome)
                nome_adj_det_TH_singolo.append(nome)
                nome_adj_det_LS_singolo.append('ADJ in TH not in LS')
                nome_adj_det_TH_singolo.append('ADJ in TH not in LS')

                if nome_adj_det_LS_singolo:
                    nome_adj_det_LS.append(nome_adj_det_LS_singolo)
                if nome_adj_det_TH_singolo:
                    nome_adj_det_TH.append(nome_adj_det_TH_singolo)
                nome_adj_det_TH_singolo = []
                nome_adj_det_LS_singolo = []
            # print('secondo ',nome_adj_det_LS_singolo)
            # print('secondo ',nome_adj_det_TH_singolo)

    if (LS[1] != [] and TH[i][1] != []) and (LS[2] != [] and TH[i][2] == []):
        for nomeLS, nomeTH in zip(LS[0], TH[i][0]):
            if not isinstance(nomeLS, list) and not isinstance(nomeTH, list):
                nome = nomeLS
                nome_adj_det_LS_singolo.append(nome)
                nome_adj_det_TH_singolo.append(nome)
                nome_adj_det_LS_singolo.append('ADJ in LS not in TH')
                nome_adj_det_TH_singolo.append('ADJ in LS not in TH')

                if nome_adj_det_LS_singolo:
                    nome_adj_det_LS.append(nome_adj_det_LS_singolo)
                if nome_adj_det_TH_singolo:
                    nome_adj_det_TH.append(nome_adj_det_TH_singolo)
                nome_adj_det_TH_singolo = []
                nome_adj_det_LS_singolo = []
            # print('terzo ',nome_adj_det_LS_singolo)
            # print('terzo ',nome_adj_det_TH_singolo)

    i += 1
prova=0
listaProva=[]
for x, y in zip(nome_det_LS, nome_det_TH):
    # print("nome-detLS e nome-detTH", x, y)
    if len(x) == 1:
        nomeFrase = x[0]
    else:
        prova += 1
        listaProva.append(x)
        listaProva.append(y)
        if x[0][2] != y[0][2]:
            print("nome-det: NOUN GENDER -->", nomeFrase, x, y)
            err_gender_noun += 1
        elif x[1][2] != y[1][2]:
            print("nome-det: DET GENDER -->", nomeFrase, x, y)
            err_gender_det += 1
        elif x[0][3] != y[0][3]:
            print("nome-det: NOUN NUMBER -->", nomeFrase, x, y)
            err_number_noun += 1
        elif x[1][3] != y[1][3]:
            print("nome-det: DET NUMBER -->", nomeFrase, x, y)
            err_number_det += 1

for x, y in zip(nome_adj_det_LS, nome_adj_det_TH):
    # print("nome-det-adjLS e nome-det-adjTH", x, y)
    if len(x) != len(y):
        print('lunghezza lista TH diversa da LS', nomeFrase, x, y)
    else:
        if len(x) == 1:
            nomeFrase = x[0]
        else:
            if len(x) == 2:
                prova += 1
                listaProva.append(x)
                listaProva.append(y)
                if x[0][2] != y[0][2]:
                    print("nome-det: NOUN GENDER -->", nomeFrase, x, y)
                    err_gender_noun += 1
                elif x[1][2] != y[1][2]:
                    print("nome-det: DET GENDER -->", nomeFrase, x, y)
                    err_gender_det += 1
                elif x[0][3] != y[0][3]:
                    print("nome-det: NOUN NUMBER -->", nomeFrase, x, y)
                    err_number_noun += 1
                elif x[1][3] != y[1][3]:
                    print("nome-det: DET NUMBER -->", nomeFrase, x, y)
                    err_number_det += 1

            if len(x) == 3:
                prova += 1
                listaProva.append(x)
                listaProva.append(y)
                if x[0][2] != y[0][2]:
                    print("nome-det-adj: NOUN GENDER -->", nomeFrase, x, y)
                    err_gender_noun_3 += 1
                elif x[1][2] != y[1][2]:
                    print("nome-det-adj: DET GENDER -->", nomeFrase, x, y)
                    err_gender_det_3 += 1
                elif x[2][2] != y[2][2]:
                    print("nome-det-adj: ADJ GENDER -->", nomeFrase, x, y)
                    err_gender_adj_3 += 1
                elif x[0][3] != y[0][3]:
                    print("nome-det-adj: NOUN NUMBER -->", nomeFrase, x, y)
                    err_number_noun_3 += 1
                elif x[1][3] != y[1][3]:
                    print("nome-det-adj: DET NUMBER -->", nomeFrase, x, y)
                    err_number_det_3 += 1
                elif x[2][3] != y[2][3]:
                    print("nome-det-adj: ADJ NUMBER -->", nomeFrase, x, y)
                    err_number_adj_3 += 1

print('err_gender_noun in coppia noun-det', err_gender_noun)
print('err_gender_det in coppia noun-det', err_gender_det)
print('err_number_noun in coppia noun-det', err_number_noun)
print('err_number_det in coppia noun-det', err_number_det)

print('err_gender_noun in noun-det-adj', err_gender_noun_3)
print('err_gender_det in noun-det-adj', err_gender_det_3)
print('err_gender_adj in noun-det-adj', err_gender_adj_3)
print('err_number_noun in noun-det-adj', err_number_noun_3)
print('err_number_det in noun-det-adj', err_number_det_3)
print('err_number_adj in noun-det-adj', err_number_adj_3)

# print('lista di sintagmi', listaProva)
# print('numero di sintagmi', prova)


