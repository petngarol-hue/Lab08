from database.distributore_DAO import DistributoreDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Model:
    def __init__(self):
        self._distributori = None
        self.load_distributori()

        self.__sequenza_ottima = []
        self.__costo_ottimo = -1

    def load_distributori(self):
        """ Carica tutti i distributori e li setta nella variabile self._distributori """
        self._distributori = DistributoreDAO.get_distributori()

    def get_prezzo_medio(self, mese:int):
        """
        Calcola, per ogni distributore, il prezzo medio al litro per il mese selezionato.
        :param mese: Mese selezionato (un intero da 1 a 12)
        :return: lista di tuple --> (nome del distributore, media), es. (Distributore A, 1.789)
        """
        # TODO

        self._lista_prezzi_filtrati=[]
        self._lista_average_distributore=[]
        for n in self._distributori:
            self._lista_prezzi_filtrati = []
            self.lista=n.get_prezzi()
            for l in self.lista:
                if mese == l.data.month:
                    self._lista_prezzi_filtrati.append(l)
            self.media=sum([o.prezzo_litro for o in self._lista_prezzi_filtrati ])/len([o.prezzo_litro for o in self._lista_prezzi_filtrati ])
            self._lista_average_distributore.append((n.nome,self.media))
        return self._lista_average_distributore





    def get_sequenza_ottima(self, mese:int):
        """
        Calcola la sequenza ottimale di rifornimenti nei primi 7 giorni
        :return: sequenza di nomi distributore ottimale
        :return: costo ottimale (cioè quello minimizzato dalla sequenza scelta)
        """
        self.__sequenza_ottima = []

        prezzi_settimana = self.__get_prezzi_prima_settimana_mese(mese)
        self.__costo_ottimo = sum(prezzi_settimana[1])*100
        self.__ricorsione([], 1, None, 0, prezzi_settimana)



        # Traduci gli ID in nomi
        id_to_nome = {distributore.id: distributore.nome for distributore in self._distributori}
        sequenza_nomi = [f"Giorno {giorno}: {id_to_nome[i]}" for giorno, i in enumerate(self.__sequenza_ottima, start=1)]
        return sequenza_nomi, round(self.__costo_ottimo, 2)

    def __ricorsione(self, sequenza_parziale, giorno, ultimo_distributore, costo_corrente, prezzi_settimana):
        """ Implementa la ricorsione """
        # Todo


        if giorno>7  :
            print(costo_corrente, self.__costo_ottimo)
            if self.__costo_ottimo>costo_corrente:
                self.__costo_ottimo = costo_corrente
                self.__sequenza_ottima = list(sequenza_parziale)




            return


        for i in prezzi_settimana:
            nuovo_prezzo=prezzi_settimana[i][giorno-1]*100+costo_corrente

            if i!=ultimo_distributore and  giorno!=1:
                nuovo_prezzo+=5
            sequenza_parziale.append(i)
            self.__ricorsione(sequenza_parziale, giorno + 1, i, nuovo_prezzo, prezzi_settimana)
            sequenza_parziale.pop()



    def __get_prezzi_prima_settimana_mese(self, mese: int):
        """
        Restituisce i prezzi dei primi 7 giorni del mese selezionato per ciascun distributore.
        :return: un dizionario: {id_distributore: [prezzo_giorno1, ..., prezzo_giorno7]}
        """
        # TODO
        self.dizionario = {}
        for n in self._distributori:
            self.dizionario[n.id]=[]
            for l in n.get_prezzi():
                if mese == l.data.month and 1 <= l.data.day <= 7:
                    self.dizionario[n.id].append(l.prezzo_litro)
                    print(self.dizionario)


        return self.dizionario


