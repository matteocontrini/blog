---
title: "Il digitale secondo Trentino Trasporti (parte 3)"
date: 2025-11-12T13:30:00+01:00
lastmod: 2025-11-12T13:30:00+01:00
slug: trentino-trasporti-digitale-3
summary: "Fa parte di un servizio digitale anche la comunicazione: diamo un'occhiata alla pagina \"FAQ risposte in un clic\" del sito Trentino Trasporti."
---

<style>
    @media (min-width: 600px) {
        .post-content img {
            width: 60%;
            margin-left: 0;
            border: 1px solid #eee;
            border-radius: 8px;
        }
    }
</style>

Fa parte di un servizio digitale (qua la [parte 1](/it/trentino-trasporti-digitale/) e qua la [parte 2](/it/trentino-trasporti-digitale-2/)) anche la **comunicazione**, specialmente nella pubblica amministrazione dove c'è l'abitudine a usare un linguaggio burocratico anche nelle comunicazioni al pubblico, spesso dimenticandosi che si sta parlando con delle persone.

Questa volta diamo quindi un'occhiata alla pagina [FAQ risposte in un clic](https://www.trentinotrasporti.it/it/servizio-clienti/faq) ([archivio](https://gist.github.com/matteocontrini/cd67215f17daecd99578cb4e28f539f9)) di Trentino Trasporti, una buona idea purtroppo realizzata in modo mediocre. I testi sono pieni di errori (ho contato almeno 9 errori di battitura e molti altri di sintassi) e sono scritti male, cioè di difficile comprensione.

Lo stile è troppo distante dalle indicazioni del [Manuale operativo di design](https://docs.italia.it/italia/designers-italia/manuale-operativo-design-docs/it/versione-corrente/doc/progettazione-dei-contenuti/scrittura-e-linguaggio.html#le-regole-per-un-linguaggio-semplice) dei servizi pubblici digitali, dai [fondamenti di linguaggio](https://designers.italia.it/design-system/fondamenti/linguaggio/) e dalla [Guida al linguaggio della Pubblica Amministrazione](https://docs.italia.it/italia/designers-italia/writing-toolkit/it/bozza/index.html), che sono i riferimenti ufficiali a livello nazionale.

Come riassume bene il manuale, l'obiettivo dovrebbe essere "scrivere per le persone" e "parlare la lingua delle persone per servizi più utili e accessibili".

Vediamo qualche esempio di **cosa non è la lingua delle persone**.

## Bici 🚲

{{< fig src="faq-bici.png" alt="Posso viaggiare con la bici elettrica o monopattino elettrico? Si ma solo sui treni della linea ferroviaria Trento-Malè-Mezzana e Trento Bassano del Grappa  e sulla Funivia Trento Sardagna in quanto sussiste una rastrelliera dedicata alle biciclette. Sul tasporto urbano ed extraurbano effettuato con autobus non sono ammesse." >}}

Chiaro. Ieri sono andato al supermercato e purtroppo non ho potuto parcheggiare la bici in quanto non sussisteva una rastrelliera dedicata alle biciclette. Se suona ridicola, non è la lingua delle persone.

Come doveva essere:

>**Posso viaggiare con la bici elettrica o con il monopattino elettrico?**
>
>🚂 **Treni e funivia**: sì, su tutti i treni della ferrovia [...] ci sono le rastrelliere per appoggiare le bici e puoi quindi portare con te la bici elettrica o il monopattino elettrico.
>
>🚌 **Autobus**: no, sugli autobus, sia urbani che extraurbani, **non puoi** portare con te la bici elettrica o il monopattino elettrico.

(Non ho capito perché le bici elettriche hanno regole diverse da quelle normali, ma non importa.)

---

{{< fig src="faq-bici2.png" alt="Quanto costa il biglietto per il trasporto bicicletta? Per tutti i servizi di trasporto pubblico di Trentino Trasporti (escluso il servizio urbano) il pagamento della tariffa ordinaria bicicletta è  pari a € 2,00." >}}

Scopriamo che "il pagamento della tariffa ordinaria bicicletta è pari a € 2,00". Suppongo volesse dire che la tariffa è di 2 €. Esiste una tariffa non ordinaria? Boh. I 2 € sono in aggiunta al costo del biglietto passeggero? Boh (presumo di sì, ma non c'è scritto da nessuna parte).

In italiano si direbbe così:

>**Quanto costa trasportare la mia bicicletta?**
>
>Il trasporto della bicicletta costa 2 € (per bici), da pagare in aggiunta al costo del biglietto/abbonamento passeggero, ma se sei un turista è spesso gratis. [Verifica qui] i dettagli.
>
>**Attenzione:** il trasporto delle bici non è sempre ammesso e dipende dallo spazio disponibile. [Leggi qui] per i dettagli.

## Orari 🕑

{{< fig src="faq-orari.png" alt="Quando escono i nuovi orari? Gli orari si suddividono in orari estivi e orari invernali. Orari estivi: sono attivi indicativamente il giorno successivo al termine dell'anno scolastico; nel periodo precedente al cambio, circa 15 giorni, vengono sempre esposti entrambi. Orari invernali: sono attivi indicativamente il primo giorno di scuola del nuovo anno scolastico; nel periodo precedente al cambio, circa 15 giorni, vengono sempre esposti entrambi." >}}

A prima vista sembra accettabile, ma non lasciamoci confondere. Gli orari "escono"? Si "suddividono"? Perché mi fai risolvere un rebus anziché dirmi le date? Come dovrei riuscire ad applicare una regola con dentro "indicativamente"? "Vengono sempre esposti entrambi"... dove? E perché una frase è ripetuta due volte?

Questa FAQ sarebbe utile se fosse scritta così:

>**Quando avverrà il passaggio da orario invernale a estivo?**
>
>❄️ L'**orario invernale** terminerà mercoledì 10 giugno 2026, l'ultimo giorno di scuola.
>
>☀️ L'**orario estivo** inizierà il giorno dopo, giovedì 11 giugno, e terminerà con l'inizio della scuola (la data non è ancora stata decisa).
>
>Nelle due settimane prima del cambio orario troverai affissi alle fermate sia l'orario estivo che invernale.

Aggiornare la risposta due volte all'anno non credo sia uno sforzo eccessivo.

---

{{< fig src="faq-orari2.png" alt="Come capire se ci sono deviazioni? Per verificare se la corsa di proprio interesse è soggetta a deviazione di percorso per ordinanza del Comune o dell'ente gestore della strada per vari motivi (cantieri, eventi sportivi) sul nostro sito internet in corrispondenza della linea, viene riportata una nota di servizio, facilmente visibile in quanto viene evidenziata da un punto escamativo ! Cliccando sul punto esclamativo si apre il comunicato. Le comunicazioni inerenti alle deviazioni di percorso vengono affisse con largo anticipo presso tutte le fermate della linea che ha subito la deviazione di percorso per informare anche gli utenti che non possono accedere all'informazione digitale." >}}

Qui non saprei da dove cominciare per commentare, quindi passiamo direttamente alla versione per le persone:

>**Come posso sapere se ci sono deviazioni delle linee degli autobus?**
>
>In presenza di cantieri, eventi sportivi, mercatini di Natale, ecc. alcune linee degli autobus potrebbero essere deviate e saltare delle fermate.
>
>Verifica se ci sono deviazioni:
>
>🚏 **Alle fermate**: presso tutte le fermate della linea deviata troverai affisso un cartello con le informazioni sulla deviazione.
>
>🛜 **Sul nostro sito**: [in questa pagina] trovi la lista delle deviazioni di autobus attualmente attive.
>
>📱 **Nell'app**: installa l'app Muoversi in Trentino per accedere rapidamente alla lista delle deviazioni per la linea o la fermata di cui hai bisogno.

## Biglietti 🎟️

{{< fig src="faq-biglietti.png" alt="Posso acquistare il biglietto a bordo? Il biglietto può essere acquistato a bordo dal personale viaggiante pagando solamente in contanti (con banconota del taglio immediatamente superiore a quello dell’ammontare del prezzo del biglietto): - biglietto extraurbano (pullman/treno) a tariffa chilometrica; si precisa che dal 11/07/2022 nel caso che biglietto sia acquistato direttamente a bordo viene applicata la tariffa biglietto a bordo (il sovrapprezzo di 2,00 è stato abolito). - biglietto di corsa semplice urbana: 2 euro (valido per singola corsa); per la vendita del biglietto a bordo, il cliente è invitato a utilizzare banconote di taglio minimo, o quello equivalente di pari importo o quello immediatamente superiore al valore del (o dei) biglietto(i) emesso(i); (es.: da 1 a 2 biglietti utilizzare 1 banconota da 5€; da 3 a 4 biglietti utilizzare 1 banconota da 10€ etc.) - Servizio urbano Alto Garda e su tutte le linee del Servizio Urbano Pergine: sulle linee 3 (Nago-S.Tomaso-Bolognano) e 869 (Riva-Deva-Pranzo-Campi) del Servizio urbano Alto Garda e su tutte le linee del Servizio Urbano Pergine per i biglietti venduti a bordo si applica la tariffa extraurbana." >}}

Questa è incredibile. Perché usare perifrasi come "il personale viaggiante"? Poi, si può pagare solo con le banconote o anche con le monete? Perché mi parli dell'abolizione del sovrapprezzo, visto che il sovrapprezzo in realtà c'è?

Rivoluzioniamo:

>**Posso acquistare il biglietto a bordo degli autobus?**
>
>Sì, puoi acquistare il biglietto a bordo degli autobus urbani ed extraurbani rivolgendoti all'autista e pagando in contanti con monete o banconote.
>
>**Attenzione:** i biglietti acquistati a bordo costano di più. Per risparmiare, usa [le app], [la carta scalare] o vai in una biglietteria.
>
>🚌 **Autobus urbani**: il biglietto costa 2 € e vale solo per una corsa. Non puoi acquistare biglietti orari o giornalieri a bordo. Alcune linee urbane usano le tariffe extraurbane, [verificalo qui].
>
>⛰️ **Autobus extraurbani**: il costo del biglietto dipende dalla destinazione che vuoi raggiungere e ha un sovrapprezzo di 0,50 € se lo acquisti a bordo. Trovi i dettagli [in questa pagina].
>
>Se paghi con banconote, per favore usa il taglio più piccolo possibile. Esempio: se devi pagare 2 € usa una banconota da 5 € e non da 10 € o più.

Più chiaro no?

Bonus: **cosa c'è scritto sui cartelli alle fermate?** Che il sovrapprezzo è di 2 € (quello abolito!). Anche in questo caso con una sbrodolata di testo per lo più inutile e incomprensibile (la frase "nessuna giustificazione potrà essere addotta avverso la contestazione" sarà anche italiano ma si capisce solo a sentimento):

{{< fig src="sovrapprezzo-bus-cartello.jpg" width="100%" alt="AVVISO. Servizio Urbano Trento. ACQUISTO BIGLIETTO A BORDO AUTOBUS. DA LUNEDI 11 SETTEMBRE,2017 E' POSSIBILE ACQUISTARE UN BIGLIETTO DI CORSA SEMPLICE, VALIDO FINO A FINE CORSA E NON RIUTILIZZABILE, A TARIFFA FISSA DI € 2,00, A BORDO DELL'AUTOBUS, SU TUTTE LE LINEE DELLA RETE URBANA. L'OPPORTUNITA' E' OFFEFTA ALL'UTENTE CHE NON ABBIA PROVVEDUTO A DOTARSI PREVENTIVAMENTE DI UNO DEI TITOLI DI VIAGGIO PIU' DIFFUSI, DISPONIBILI A PREZZI PIU' CONVENIENTI E A CONDIZIONI DI MAGGIOR FAVORE (ABBONAMENTO, SMART-CARD, APP SU SMARTPHONES, BIGLIETTO CARTACEO). E' QUINDI DA CONSIDERARSI L'ULTIMA POSSIBILITA' DI TRANSAZIONE OFFERTA PER L'UTILIZZO DEL SERVIZIO, INDIPENDENTE ANCHE DALLE LIMITAZIONI DELL'ORARIO DI APERTURA DI BIGLIETTERIE E RIVENDITE CONVENZIONATE, EVITANDO IL RISCHIO DI INCORRERE NELLE SANZIONI PREVISTE IN CASO DI CONTROLLO. PER QUESTE RAGIONI E PER LE FINALITA' DEL PROVVEDIMENTO, IL FONDO CASSA IN DOTAZIONE ALL'AUTISTA NON PUO' ESSERE ILLIMITATO. A TALE PROPOSITO, INVITANDO SEMPRE L'UTENTE A DOTARSI IN ANTICIPO DI UNA DELLE TIPOLOGIE DI TITOLO DI VIAGGIO PIU' DIFFUSE E CONVENIENTI E A CONSIDERARE LA POSSIBILITA' DI ACQUISTO IMMEDIATO A BORDO COME SOLUZIONE CERTAMENTE UTILE MA DI EMERGENZA, SI RACCOMANDA DI MUNIRSI, PER L'ACQUISTO, DI DENARO CONTATO ED EVENTUALMENTE DI BANCONOTE DI TAGLIO PROPORZIONATO ALL'ENTITA' DELL'IMPORTO. SI PRECISA CHE, IN CASO DI CONTROLLO, NESSUNA GIUSTIFICAZIONE POTRA' ESSERE ADDOTTA, AVVERSO LA CONTESTAZIONE E LA RELATIVA SANZIONE PER IRREGOLARITA' TARIFFARIA, DALL'UTENTE SPROVVISTO DI BIGLIETTO, CHE NON SIA STATO IN GRADO DI CONCLUDERE LA TRANSAZIONE A BORDO PER DIFFICOLTA' DI CAMBIO BANCONOTE DI GROSSO TAGLIO. Trento, 25 settembre 2017" >}}

## Comitive 👬

{{< fig src="faq-comitive.png" alt="Posso utilizzare i mezzi pubblici per visite didattiche? Sì è possibile ma occorre effettuare una comunicazione scritta e inviarla tramite e-mail al  servizio che si intende utilizzare con un anticipo di tre giorni lavorativi (esclusi i sabati e festivi)." >}}

Ok, devo "effettuare una comunicazione scritta" e poi "inviarla via email". Quindi devo comunicare la richiesta due volte? 🤔

In lingua umana:

>**Posso utilizzare i mezzi pubblici per visite didattiche?**
>
>Sì, ma devi inviare una richiesta di prenotazione via email almeno tre giorni lavorativi prima della data del viaggio. Trovi i dettagli e gli indirizzi email da contattare [in questa pagina].

## Bonus 🔈

Le [nuove tabelle degli orari (2024)](/it/trentino-trasporti-digitale-2) si presentano così:

{{< fig src="dopo.jpg" width="100%" >}}

E portano con sé anche in questo caso una lingua artificiosa e burocratica che nessuno parla. Perché scrivere "**azionare il dispositivo acustico per scendere**" anziché quello che dicono tutti, cioè "**premi il pulsante rosso per prenotare la fermata**"?

---

È così semplice. No?
