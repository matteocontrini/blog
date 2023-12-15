---
title: "La storia della CDN Rai Play, o come non scegliere una CDN"
date: 2023-12-15T14:30:00+01:00
lastmod: 2023-12-15T14:30:00+01:00
slug: rai-cdn
summary: "Le fragilità di come la Rai sceglie (senza scegliere) le CDN per Rai Play: 70 Petabyte al mese affidati senza nessuna valutazione tecnica e spesso senza nessuna concorrenza."
showtoc: true
---

*70 Petabyte al mese, in carico a TIM e Fastweb almeno dal 2016, con dei bandi aggiudicati senza nessuna valutazione tecnica e spesso senza nessuna concorrenza.*

*Le fragilità di come la Rai sceglie (senza scegliere) le CDN per Rai Play, la propria piattaforma digitale di punta, tra bandi, gare con un solo concorrente, ricorsi, tribunali che suggeriscono che le CDN non sono cambiate dagli anni novanta ad oggi, e il rischio che passi l'idea che una soluzione valga l'altra, basta che costi poco.*

---

Una particolarità di Rai Play, mai realmente chiarita, è che molti contenuti non sono disponibili in tutti i livelli di qualità su tutte le piattaforme.

Ad esempio, la serie *L'amica geniale*, una delle produzioni di punta della Rai, è visibile al massimo in HD 720p su desktop mentre sull'app Rai Play per la tv (HbbTV) arriva a 1080p. La serie è stata trasmessa in tv anche in 4K ma non risulta sia disponibile in streaming in tale risoluzione.

{{< fig src="playlist1.png" caption="La playlist HLS versione desktop, dove si vede che la massima risoluzione è 1280x720 con bitrate nominale di 2,4 Mbps." >}}

{{< fig src="playlist2.png" caption="La playlist HLS per lo stesso contenuto versione HbbTV. In questo caso la massima risoluzione è 1920x1080 con bitrate nominale di 5 Mbps." >}}

Una possibile ipotesi (oltre a quella di una generale disorganizzazione, comunque non da escludere) è che il motivo sia una **questione di costi**: secondo Audiweb nel mese di settembre 2023 Rai Play ha registrato **7 milioni di utenti unici** per una media di tempo di visualizzazione di 3 ore a testa. Ciò significa **21 milioni di ore visualizzate ogni mese**. Se un'ora di streaming in 720p usa facilmente 1 GB, a 1080p diventa circa il doppio, portando così rapidamente il traffico a decine di Petabyte al mese. (Prendendo come riferimento 1 GB come stima il traffico mensile sarebbe di 21 PB, cioè 21.000 TB.)

{{< fig src="audiweb.png" >}}

In ogni caso, la Rai non paga la banda delle CDN a consumo, ma in base a **contratti dalla durata di due o tre anni che stimano il consumo previsto, in anticipo**, per lo streaming video su Rai Play e sugli altri portali come Rai News.

Grazie ai bandi regolarmente pubblicati si possono ottenere diverse informazioni su ciò che sta dietro a Rai Play. In breve:

- il **consumo di banda medio mensile** stimato per il 2022-2025 è di circa **70 PB**, quasi il doppio rispetto al triennio precedente
- le CDN usate sono due: **Akamai** e **MainStreaming**, fornite rispettivamente da TIM e Fastweb. La Rai infatti non fa contratti direttamente con le CDN ma richiede al mercato di fornire un servizio di streaming delivery, che viene poi realizzato da CDN esterne (o così è stato finora)
- il **criterio di selezione** delle CDN è **puramente economico** senza una valutazione della qualità o affidabilità delle soluzioni
- l'azienda che si è classificata seconda nel 2019, la Mosai.co srl (con le CDN Lumen/LimeLight), ha fatto **ricorso** proprio per questo motivo: secondo l'azienda il test di carico non dimostrava che la soluzione offerta da Fastweb fosse tecnicamente idonea
- un pasticcio che ha portato nel bando successivo a **rimuovere del tutto il test di carico**: a fronte di una capacità di picco richiesta in caso di eventi speciali di 12 Tbps, ora viene solo chiesto di mostrare un esempio di streaming realizzato in passato con capacità di almeno 2 Tbps
- oltretutto, il lotto più grande di questi bandi viene assegnato dal 2016 a TIM, unica offerente senza concorrenti

Seguono i dettagli.

## I tre bandi

I tre bandi per le gare d'appalto finora pubblicati (2016, 2019 e 2022) sono a grandi linee simili tra loro. Richiedono di offrire sia un servizio di accelerazione dei siti web (cioè una CDN/WAF per i siti web Rai) sia il servizio di streaming video.

Per quando riguarda lo streaming si richiede che la CDN si occupi del **packaging dinamico, del caching e del delivery dei contenuti**. Significa, in pratica:

- nel caso dell'on-demand, i server Rai (l'origin della CDN) forniscono dei file MP4 già appositamente codificati per lo streaming e la CDN si occupa di fare packaging dinamico, cioè di convertire i file video nei **formati di streaming adattivo**, come HLS e MPEG-DASH, al momento della richiesta, on the fly
- i contenuti così generati finisco nella **cache della CDN**, che ha un suo storage
- la CDN serve i contenuti elaborati agli utenti (**content delivery**)

Il volume di traffico e di storage richiesti nel corso degli anni sono quelli della seguente tabella. Tutti i bandi sono stati divisi in due lotti, cioè in due parti, di cui il secondo sempre molto più piccolo del primo. I valori mostrati sono la somma di entrambi i lotti, con qualche leggera approssimazione.

|                           | 2017-2019 | 2019-2022 | 2022-2025 |
|---------------------------|-----------|-----------|-----------|
| **Traffico mensile**      | 12 PB     | 42 PB     | 70 PB     |
| **Storage medio**         | 148 TB    | 137 TB    | 360 TB    |
| **Capacità di delivery\*** | 0,7 Tbps  | 5 Tbps    | 7 Tbps    |
| **(in caso di eventi\*)**  | 1,2 Tbps  | 10 Tbps   | 17 Tbps   |
| **Utenti contemporanei**  | -         | -         | 4,5 mln   |

*(\*valori riferiti all'ultimo anno di contratto)*

Ci sono anche dei requisiti più specifici di rete:

|                                      | 2017-2019    | 2019-2022    | 2022-2025                                |
|--------------------------------------|--------------|--------------|------------------------------------------|
| **Capacità rete italiana (lotto 1)** | 1,8 Tbps     | 5 Tbps       | 10 Tbps                                  |
| **Capacità rete italiana (lotto 2)** | 0,5 Tbps     | 1 Tbps       | 4 Tbps                                   |
| **Peering (lotto 1)**                | almeno 2 ISP | almeno 3 ISP | almeno 10 ISP, 4 IXP, 5 città            |
| **Peering (lotto 2)**                | almeno 1 ISP | -            | almeno 2 IXP, 2 città                    |
| **Peering con Rai**                  | -            | -            | 10 Gbps via Teulada + 10 Gbps Saxa Rubra |
| **Hit rate CDN (lotto 1)**           | -            | -            | 99,5% per on demand, 99,9% per live      |
| **Hit rate CDN (lotto 2)**           | -            | -            | 95%                                      |
| **Protocolli (lotto 1)**             | -            | -            | IPv6, HTTP/2 e /3                        |
| **Protocolli (lotto 2)**             | -            | -            | -                                        |

Gli importi a base d'asta, cioè prima del ribasso delle offerte fatte dai partecipanti alla gara, sono:

|             | 2017-2019 | 2019-2022 | 2022-2025 |
|-------------|-----------|-----------|-----------|
| **Lotto 1** | 8,5 mln € | 17 mln €  | 18 mln €  |
| **Lotto 2** | 1,5 mln € | 4 mln €   | 5 mln €   |
| **Totale**  | 10 mln €  | 21 mln €  | 23 mln €  |

Il **criterio di aggiudicazione** è il **minor prezzo**: non c'è quindi un punteggio tecnico ma vince chi fa l'offerta più economica, salvo una verifica tecnica dell'idoneità. (A un certo punto nei bandi si parla di "importo non ribassabile", qualche esperto mi spiegherà cosa si intende, visto che il criterio è basato sul ribasso.)

Secondo la Rai quindi i servizi richiesti hanno **«caratteristiche standardizzate»** e sono «sprovvisti di carattere innovativo» perché si tratta di «protocolli di comunicazione che rispondono agli standard di comunicazione e trasferimento dei dati adottati da tutti i player del mercato», e per questo **la valutazione tecnica non è necessaria**.

Il problema è che qua non si sta acquistando un'implementazione di "standard di comunicazione" ma un servizio di streaming video con packaging dinamico, centinaia di TB di cache e capacità di delivery di diversi Tbps a milioni di utenti contemporanei. In questa combinazione di elementi **c'è ben poco di standardizzato** e difficilmente una CDN vale l'altra.

C'è da dire che il bando del 2022 sicuramente restringe di molto il campo. Non sono tante le CDN che possono offrire **interconnessioni in 4 IXP (!) e 10 ISP in 5 città italiane (!)**, specialmente con il supporto a IPv6 e HTTP/3. Sono requisiti piuttosto stringenti, ma **ci sono due problemi**:

- **non sembrano essere obbligatori**: nel momento in cui scrivo lo streaming Akamai su Rai Play avviene in HTTP/1.1, non c'è nessuna traccia di HTTP/3 e tantomeno di HTTP/2 (!!!)
- i requisiti riguardano soltanto il primo lotto: se nel secondo lotto ci fossero più soluzioni offerte (come è stato) e una avesse IPv6 e HTTP/3 e l'altra no, questo **non conterebbe nulla** ai fini dell'aggiudicazione proprio perché non è prevista nessuna valutazione tecnica

<!--Negli anni precedenti andava anche peggio: se nel 2016 la CDN scelta è finita per essere Akamai non è stato perché i requisiti del bando richiedevano una soluzione del livello di Akamai (che è ampiamente la CDN premium più grande e usata al mondo), ma perché alla gara ha partecipato solo TIM e TIM ha deciso di offrire una soluzione basata su Akamai, mentre alla Rai andava bene un po' tutto.-->

In alcuni casi poi i requisiti sono un po' particolari: nel bando del 2016 si chiedeva che i **tempi di transmuxing e di codifica fossero «nulli»**, cosa tecnicamente impossibile. Oppure nel 2022 si chiedeva un **offload di banda** (e quindi un hit rate della CDN) per l'on demand di **almeno il 99,5%**, un valore estremamente alto per una CDN tradizionale specialmente in caso di molti contenuti in "long tail".

## Le CDN "scelte"

|                    | Vincitore | CDN           | Ribasso | Altri partecipanti |
|--------------------|-----------|---------------|---------|--------------------|
| **2016 (lotto 1)** | TIM       | Akamai (?)    | ?       | Nessuno            |
| **2016 (lotto 2)** | Fastweb   | ?             | ?       | Nessuno            |
| **2019 (lotto 1)** | TIM       | Akamai        | ?       | Nessuno            |
| **2019 (lotto 2)** | Fastweb   | MainStreaming | 81,10%[^sentenza2]    | Altri 3, tra cui Mosai.co srl (con Lumen/CenturyLink e Edgio/LimeLight) |
| **2022 (lotto 1)** | TIM       | Akamai        | 10% (?) | Nessuno            |
| **2022 (lotto 2)** | Fastweb   | MainStreaming | 21% (?) | Un altro           |

Come si vede dalla tabella, da almeno il 2016 sono **TIM e Fastweb** a fornire le soluzioni di CDN. Solo nel 2019 c'è stata un po' di concorrenza con ben 4 offerte sul secondo lotto.

**TIM** fornisce un servizio basato su **Akamai**, ormai CDN di riferimento per la Rai ma non per scelta diretta: nei lotti in cui TIM ha vinto non c'è mai stata nessuna concorrenza. Non possiamo sapere come sono nati questi bandi e cosa si sono detti TIM e la Rai, ma viene quasi da pensare che Rai Play stia usando Akamai come CDN quasi "per caso", solo perché quella è stata l'unica offerta, e **non perché la Rai ritenga che quella sia la soluzione migliore a livello tecnico né tantomeno economico**.

Va poi forse spesa qualche parola su **MainStreaming**, che non è una CDN tradizionale: è una **startup italiana** nata a fine 2016 che si occupa di offrire soluzioni di streaming video "enterprise". Quando Fastweb l'ha scelta nel 2019 esisteva quindi da poco più di 2 anni e mezzo e aveva un fatturato di appena un milione di euro (contro gli oltre 800 milioni di Akamai).

MainStreaming ha scelto di costruirsi **una propria CDN** con apparati di proprietà e connettività fornita principalmente da **OneCom**, un operatore di transito IP abbastanza sconosciuto, che in Italia non aveva sostanzialmente nessuna rilevanza finché MainStreaming non è diventato importante non solo per la Rai ma anche per DAZN.

Senza nulla togliere a MainStreaming (ce ne fossero di più di startup così in Italia!) la qualità complessiva del servizio CDN è **difficilmente comparabile con quella di Akamai**, che è un riferimento per capacità e affidabilità (nel momento in cui scrivo Rai Play non mi funziona perché la CDN MainStreaming non risponde, va in timeout; avete mai sentito parlare di outage di Akamai?). Questo è un elemento in più che contribuisce all'idea che ci sia una certa fragilità nelle scelte tecniche della Rai: per come sono scritti i bandi Akamai e MainStreaming sono sostanzialmente messe sullo stesso piano!

Per finire, in ogni caso le soluzioni che hanno vinto i bandi sono sempre state **single-CDN** e non multi-CDN, come forse sarebbe opportuno su questa scala per distribuire meglio il traffico.

## Il ricorso di Mosai.co srl

La storia del **ricorso di Mosai.co srl** poteva diventare un perfetto esempio moderno della metafora di Davide contro Golia (basta considerare i 6 avvocati schierati da Rai e Fastweb), ma per via dei tempi della giustizia (più lunghi dei contratti stessi!) e una oggettiva scarsa preparazione tecnica dei tribunali **la questione è poi finita sostanzialmente nel nulla**.

Dopo l'aggiudicazione del secondo lotto del **bando del 2019** a Fastweb, e quindi a MainStreaming, **l'azienda arrivata seconda decide di fare ricorso**. L'azienda è **Mosai.co srl**, che sviluppa tra il resto una [piattaforma di streaming video](https://www.meride.tv/). È anche questa un'azienda relativamente piccola, nel 2019 ha fatturato 4,5 milioni (poi scesi a 2,6 milioni due anni dopo), ha tre dipendenti e il sito ufficiale indica 65 PB come quantità di traffico annuale servito.

Tra le varie contestazioni di Mosai.co, presentate formalmente al TAR del Lazio, ci sono alcune questioni tecniche, che sintetizzo:[^sentenza1]

[^sentenza1]: *Sentenza 10046/2020 pubblicata il 2/10/2020, TAR del Lazio, Roma* https://www.giustizia-amministrativa.it/web/guest/dcsnprr

- il **collaudo** della soluzione di Fastweb, avvenuto prima dell'aggiudicazione definitiva, avrebbe accertato solo "in maniera generica e parziale" l'idoneità tecnica del sistema
- il problema starebbe in particolare nel test **di carico**, che richiedeva di verificare che la CDN video fosse in grado di gestire lo streaming simultaneo di **almeno 100mila utenti** su una diretta streaming
- viene contestato che il report prodotto da Fastweb **non contiene dei log** e quindi non è possibile verificare realmente che il test sia stato superato, perché i risultati sono "autoreferenziali" e la Rai non può semplicemente fidarsi. Su specifica richiesta di Mosai.co la Rai è riuscita a fornire soltanto «un estratto di due righe» dei log
- secondo i dati contenuti in questo report risulterebbe che durante il test il **throughput** della piattaforma **con 10mila, 15mila e 34mila utenti** connessi era superiore rispetto a quando ce n'erano collegati **100mila**, una contraddizione (almeno in apparenza)
- il sistema di stress test non è stato documentato e quindi non è possibile sapere se si trattasse di un sistema di terze parti sufficientemente rodato in modo che potesse fornire delle «evidenze oggettive»
- a confermare questo sospetto ci sarebbe il fatto che Fastweb ha barrato "NO" in corrispondenza di una domanda dei documenti di gara in cui si chiedeva di confermare di non aver fornito dichiarazioni false (😅)

In pratica quindi Mosai.co sostiene che **il test di carico**, cioè la verifica del funzionamento con almeno 100mila utenti, **non sia stato effettivamente superato** e che di conseguenza la soluzione di Fastweb non soddisfa le richieste tecniche del bando.

Un altro punto contestato da Mosai.co è la decisione della Rai di prevedere il **criterio di aggiudicazione del minor prezzo «a fronte di un sistema tecnico complesso»**. Questo criterio avrebbe infatti **«inibito l’esame comparativo dei sistemi sotto l’aspetto tecnico**, basandosi solo ed unicamente sull’aspetto economico». La soluzione proposta da Mosai.co non solo era in linea con i parametri previsti ma li «superava ampiamente» e quindi avrebbe dovuto essere valutata «maggiormente idonea» rispetto a quella di Fastweb perché «di gran lunga migliore».

**Mosai.co perde il ricorso** in primo grado per diversi motivi:

- il tribunale giudica positivamente la risposta di Fastweb, che spiega la contraddizione sul throughput del test di carico con il fatto che per alcuni secondi il video trasmesso era molto statico e quindi la compressione ha causato una riduzione della banda utilizzata. Si tratterebbe quindi di un **errore di lettura da parte di Mosai.co**
- per quanto riguarda i log, il bando non richiedeva di fornire documentazione in nessun formato specifico e quindi il fatto che un ingegnere della Rai abbia giudicato sufficienti le prove «costitusce garanzia adeguata»
- secondo il tribunale, poi, **un servizio di CDN non presenta carattere tecnologico innovativo** e questo sarebbe provato dal fatto che questo tipo di servizio **«esiste dalla fine degli anni novanta»**. Inoltre «i protocolli di comunicazione previsti dal bando rispondono agli standard di comunicazione e trasferimento dei dati adottati da tutti i player del mercato (Netflix, Amazon Prime, Infinity, Sky ed altri)», cosa provata dal fatto che al bando sono state presentate almeno quattro CDN diverse

A livello tecnico queste motivazioni potrebbero far storcere un po' il naso perché:

- uno stress test dove a un certo punto nel momento clou il video diventa un'immagine statica per quasi 20 secondi **non sembra molto realistico**. Oltretutto, un sistema di streaming live adattivo ha come presupposto che il bitrate sia il più possibile costante per permettere agli algoritmi adattivi di lavorare al meglio, per cui non è chiarissimo perché la banda possa oscillare in modo così drastico (senza avere accesso alla documentazione si può però capire ben poco)
- la sentenza sembra dire che dato che "le CDN esistono dalla fine degli anni novanta" e "usano tutte gli stessi protocolli", allora **una vale l'altra**
  - anche volessimo prendere per buono questo ragionamento, **il più vecchio dei protocolli di streaming** menzionati nei requisiti del bando è **HLS**, che esiste **dal 2009** ma nel frattempo si è evoluto moltissimo, per cui il supporto al protocollo non è verificabile con un sì/no. I sistemi di packaging dinamico, tipici delle CDN video, sono invece una tendenza relativamente recente e tutt'altro che standardizzata (e poco hanno a che fare con le CDN classiche)
  - poi, il fatto che al bando sono state presentate diverse CDN dimostra piuttosto come sia **ancora più necessario che venga fatta una valutazione tecnica** per scegliere la più vantaggiosa, considerando non solo l'aspetto economico ma anche tecnico

**Mosai.co si appella** alla sentenza e il Consiglio di Stato **accoglie parzialmente il ricorso** con una nuova sentenza del febbraio 2022, quando ormai il contratto triennale sta andando verso la scadenza.[^sentenza2]

[^sentenza2]: *Sentenza 01039/2022 pubblicata il 13/2/2022, TAR del Lazio, Roma*

Nell'appello Mosai.co aggiunge ulteriori considerazioni, tra cui il fatto che fornire dei log sia considerata «regola tecnica della materia» e che un grafico mostrerebbe come a fronte di un throughput dichiarato di 1,6 Tbps e 45 Mbps per utente il test avrebbe così testato la presenza di 35mila utenti e non 100mila.

Il tribunale si affida a una consulenza tecnica per risolvere queste questioni e il consulente conferma che:

>“E’ oggettivo, infatti, che **la documentazione sulle modalità di configurazione e di conduzione del test “S5” sia a dir poco lacunosa**. Non esiste una descrizione dettagliata del piano di test, della architettura del testbed, delle pre-condizioni, delle operazioni da seguire per l’esecuzione del test, dei risultati attesi”, specificando che le suddette indicazioni rientrano “…nelle best pratice cui ci si dovrebbe sempre attenere in occasione delle procedure di collaudo di prodotti e servizi acquisiti da terze parti…”. E da ultimo: “In sintesi, il CTU ritiene che, dal punto di vista strettamente formale, **la documentazione fornita** a supporto del superamento del test S5 possa essere **considerata appena sufficiente**”.

Il giudice conclude che «il fatto che il capitolato fosse estremamente generico [...] non è ragione sufficiente a far ritenere superato il test in presenza di documentazione carente». **Era onere della Rai**, che dalla documentazione fornita non poteva arrivare a una conclusione, **«richiedere maggiori dettagli per poter validare ogni passaggio del test»**.

Dopo la sentenza, nel marzo 2022 **Fastweb esegue un nuovo collaudo e la Rai lo accetta come valido**. Mosai.co si rivolge di nuovo al tribunale per far presente come il test sia stato svolto **con le condizioni del 2022 e non del 2019**, e quindi con «condizioni tecnologiche e di capacità del fornitore allo stato attuale, differenti rispetto a quelle presenti al momento della presentazione dell’offerta».[^sentenza3]

[^sentenza3]: *Sentenza 01784/2023 pubblicata il 21/2/2023, TAR del Lazio, Roma*

In particolare, nel frattempo «**la capacità di Mainstreaming** all’interno del MIX di Milano [il più grande IXP in Italia] sarebbe **quanto meno duplicata** al marzo 2022». Un analogo potenziamento dell'infrastruttura sarebbe avvenuto «al Namex di Roma, il più importante IXP del centro-sud Italia, e comunque in tutti i principali nodi di interscambio».

Il Consiglio di Stato respinge queste nuove contestazioni di Mosai.co e le motivazioni spiazzano un po': **la questione non è più di merito**, cioè capire se il test nel 2019 era stato superato o no, **ma di forma**, cioè mostrare di aver compiuto l'azione di trasmettere la documentazione dettagliata. Per rimediare alla situazione Rai e Fastweb dovevano quindi solo ripetere la trasmissione della documentazione omessa nel 2019, ma senza che abbia più nessuna importanza il fatto che il test sia quello del 2019 o del 2022.[^giornalettismo][^giornalettismo2]

[^giornalettismo]: *Come si applica il principio dell’ora per allora a una sentenza sulle tecnologie di streaming* https://www.giornalettismo.com/come-si-applica-il-principio-dellora-per-allora-a-una-sentenza-sulle-tecnologie-di-streaming/
[^giornalettismo2]: *Il caso più emblematico dei problemi della governance RAI* https://www.giornalettismo.com/rai-causa-mosaico-digitalizzazione/

## Il test di carico sparito

Probabilmente "scottata" da questa esperienza, nel bando del 2022 la Rai risolve la questione dello stress test **rimuovendo del tutto il test di carico dalle procedura di collaudo**.

Come metodo di verifica viene invece richiesto un **report** che mostri i dettagli di un **evento di live streaming già avvenuto** in passato con un throughput di almeno **2 Tbps** per il primo lotto e di almeno **500 Gbps** per il secondo lotto.

{{< fig src="collaudo1.png" alt=`S1 - CAPACITÀ DI EROGAZIONE LIVE STREAMING
Descrizione
Il Fornitore mette a disposizione del Committente dettagliata documentazione di
esercizio anche fruibile via web tramite una dashboard del proprio ambiente deidati di
traffico di almeno un evento live streaming erogato sul territorio italiano in termini di:
• Data e descrizione della tipologia di evento
• Andamento del traffico dell’evento
• Throughput di picco
• Bitrate medio erogato
• Utenti unici contemporanei
• Distribuzione geografica degli utenti
• Distribuzione tipologia differenti device connessi
• Tipologia e percentuale errori sullo streaming dell’evento` >}}

La cosa che forse crea qualche dubbio è il confronto tra il throughput richiesto dal test e i requisiti del bando: il primo lotto del bando richiede infatti una capacità di picco in caso di eventi di **12 Tbps** (vs 2 Tbps di test) mentre il secondo di **5 Tbps** (vs 500 Gbps di test).

In condizioni di eventi speciali, come il Festival di Sanremo, si può supporre che il traffico istantaneo sia monopolizzato dallo streaming live dell'evento singolo per cui non è molto chiaro come questa verifica dimostri l'effettiva idoneità della CDN. (Non a caso le lamentele sulle pessime prestazioni delle dirette Rai in streaming durante Sanremo [non mancano mai](https://forum.fibra.click/d/16829-le-dirette-su-raiplayit-fanno-letteralmente-schifo).)

## La CDN Rai Way

In parallelo a tutto ciò, **Rai Way**, la società della Rai che si occupa di gestire le infrastrutture di trasmissione, sta realizzando [**Rai Way Edge**](https://edge.raiway.it/), un sistema di datacenter distribuiti sul territorio italiano con l'obiettivo di offrire servizi di edge computing.

Tra questi servizi c'è anche una **CDN**, che pare sia ancora in corso di realizzazione e non è molto chiaro se a un certo punto sarà sfruttata anche per lo streaming video di Rai Play.

La CDN non sarà comunque realizzata da Rai Way direttamente: nel 2022 si è svolto un bando con base d'asta di 23 milioni di euro per affidare la realizzazione e gestione della CDN per quattro anni a un'azienda. A marzo 2023 l'incarico è stato affidato al raggruppamento di imprese Sielte-MR Telecom per 10 milioni di euro (-56%) e prevede la fornitura di hardware, software e servizio NOC.

Nel frattempo comunque Rai Play continua ad utilizzare una combinazione di Akamai e MainStreaming per lo streaming video, e vedremo come la situazione si evolverà nei prossimi anni.
