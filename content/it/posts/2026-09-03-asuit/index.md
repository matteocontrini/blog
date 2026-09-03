---
title: "Il fallimento digitale della sanità del Trentino"
date: 2026-09-03T11:00:00+02:00
lastmod: 2026-09-03T11:00:00+02:00
slug: asuit-digitale
summary: "I disservizi informatici dell'ASUIT e cosa succede a dismettere le competenze interne rinunciando all'innovazione e al controllo dei sistemi critici."
---

La cronaca trentina degli ultimi mesi è stata spesso occupata dai **disservizi software dell'azienda sanitaria provinciale** (**ASUIT**, o APSS fino all'anno scorso). I problemi hanno riguardato numerosi sistemi che sembrano avere il denominatore comune di essere software acquisiti tramite appalti, a differenza delle applicazioni storicamente realizzate internamente dalla provincia.

Vorrei lasciare qui una panoramica della situazione e qualche riflessione che non mi sembra di leggere tra le varie opinioni, accuse e difese. Sarà che le questioni in gioco diventano rapidamente tecniche e quindi non di immediata comprensione, ma alcune dichiarazioni che leggo sono al limite dell'assurdo. Capendoci qualcosa di software e servizi digitali aggiungo quindi la mia versione.

Mi baso sulle sintesi fatte dagli organi di stampa e da alcune interrogazioni provinciali per elencare i disservizi:[^rai][^int1][^int2][^int3][^int4][^int5]

- A dicembre 2025 arriva il **nuovo sistema CUP** per la prenotazioni di visite ed esami. La migrazione è travagliata ([richiede giorni](https://www.ufficiostampa.provincia.tn.it/Comunicati/Prenotazioni-online-TreC-non-accessibile-dalle-13-di-sabato-6-dicembre-alle-12-di-martedi-9)) e presto si scopre che è tutto mezzo rotto. Si possono prenotare appuntamenti che non dovrebbero essere prenotabili, risultano aperte agende di medici in pensione, si genera [overbooking](https://www.ufficiostampa.provincia.tn.it//content/view/full/292215). Le segreterie impostano giornate di apertura degli ambulatori ma questo poi non risultano nel sistema (sia online che al telefono) e quindi negli ambulatori si girano i pollici perché le disponibilità restano senza prenotazioni. Servono un paio di mesi per normalizzare la situazione. Il software del CUP è gestito [da GPI](https://www.gpigroup.com/news/gpi-vince-gara-cup-apss-trento/), società per azioni con sede a Trento specializzata in sanità digitale con più di 300 milioni di euro di fatturato annuo. Si è aggiudicata la gestione del CUP per 6 anni [per 52 milioni di euro](https://sicopat2.provincia.tn.it/trasparenza-fe/#/page/dettaglio-atti-procedure-page?codgara=205304), di cui circa 5 milioni per il software e il resto per call center e sportelli.
- Nell'ambito del progetto PNRR "cartella clinica elettronica", nel 2025 è iniziata l'attivazione del **nuovo sistema informativo ospedaliero (SIO)**, in sostituzione di un sistema di proprietà sviluppato internamente. Per ora è stato introdotto solo nei pronto soccorso, dove gestisce l'accettazione dei pazienti e le cartelle cliniche. Oltre ad avere frequenti malfunzionamenti, anche di ore (parliamo dei pronto soccorso!), pare avere scarsa compatibità con i formati di interscambio (Clinical Document Architecture) e un'interfaccia inadatta. Il software è stato [fornito e personalizzato](https://sicopat2.provincia.tn.it/trasparenza-fe/#/page/dettaglio-atti-procedure-page?codgara=240368) da Engineering, con una spesa prevista fino a 7 milioni di euro. Engineering ha poi scorporato la divisione sanità in Alfahealth e l'ha ceduta ad Accenture (quindi dalla padella alla brace). Il piano di ASUIT è di estendere questo nuovo SIO a tutti i reparti ospedalieri e c'è già chi si mette le mani nei capelli.
- Nel 2023 è stato [introdotto](https://www.ildolomiti.it/cronaca/2023/il-sistema-informatico-dellapss-fa-acqua-da-tutte-le-parti-operatori-in-allarme-rischio-blocco-dei-reparti-lazienda-alcune-situazioni-complesse-le-stiamo-affrontando) il **nuovo sistema ERP**, il gestionale per gli ordini di medicinali, strumenti, protesi, ecc. e da subito sono stati segnalati malfunzionamenti. Si legge nell'interrogazione di quest'anno che «invece di rappresentare un avanzamento ha reso più complesso effettuare gli ordini, senza grossi vantaggi». Si tratta in questo caso di SAP S/4HANA, fornito dall'omonimo colosso tedesco tramite un appalto che vale più di 5 milioni di euro ogni tre anni (CIG 805697279F + varianti).
- A gennaio 2026 il sistema di **gestione dei laboratori analisi** è stato offline per due giorni, con sospensione dei prelievi di sangue negli ospedali. Il sistema si chiama "LIS".
- Ci sono stati problemi anche nel sistema informativo di **radiologia** (RIS/PACS) e nel sistema per l'**integrazione con i medici di base e pediatri** (Ampere), in quest'ultimo caso anche [più volte alla settimana](https://www.rainews.it/tgr/trento/articoli/2026/09/ancora-problemi-informatici-nella-sanita-in-tilt-il-software-dei-medici-di-base-8e0b1805-ecc1-4bdd-8062-43f3100b89bf.html).

Una menzione d'onore andrebbe al fascicolo sanitario elettronico per il cittadino (TreC+), un abominio di cui qui non si sta parlando ma che per mia esperienza ha un problema diverso ogni volta che lo apro. Spero vivamente che questa non sia l'esperienza media del personale sanitario.

{{< fig src="trec.jpg" >}}

[^rai]: https://www.rainews.it/tgr/trento/articoli/2026/07/i-problemi-informatici-della-sanita-trentina-gli-ultimi-episodi-9776d2c4-0f1b-43d5-bf0e-36edf02b0669.html
[^int1]: https://www.consiglio.provincia.tn.it/attivita/atti-politici/Pages/atto.aspx?uid=3008247
[^int2]: https://www.consiglio.provincia.tn.it/attivita/atti-politici/Pages/atto.aspx?uid=3009739
[^int3]: https://www.consiglio.provincia.tn.it/attivita/atti-politici/Pages/atto.aspx?uid=3009738
[^int4]: https://www.consiglio.provincia.tn.it/attivita/atti-politici/Pages/atto.aspx?uid=3009737
[^int5]: https://www.consiglio.provincia.tn.it/attivita/atti-politici/Pages/atto.aspx?uid=3009722

Di fronte a questa situazione nel luglio 2026 l'ASUIT ha iniziato a rispondere più concretamente dei problemi.

Il 4 agosto 2026 l'ASUIT [ha organizzato](https://www.rainews.it/tgr/trento/articoli/2026/08/la-storia-si-ripete-ancora-nuovi-problemi-ai-sistemi-informatici-asuit-siamo-imbarazzati-32010c9b-6482-4e6e-812b-c0cbdaf5e31f.html) una conferenza stampa in cui **i dirigenti spiegano di "avere le mani legate"** e che sono stati "costretti" a cambiare i sistemi e a spendere i soldi:

> La dirigenza dell'azienda sanitaria in una conferenza stampa ha ammesso di “avere le mani legate”. “Ci sono quattro piattaforme - spiega Asuit - a abbiamo avuto problemi con tutte e quattro. Per i sistemi informatici abbiamo ricevuto 20 milioni di euro portati dal Pnrr e questo ci ha costretto a cambiare i sistemi. Le personalizzazioni necessarie al nostro territorio stanno causando questi problemi”. I fornitori però, fa capire l'Azienda, non si possono cambiare.

Si è arrivati qui perché nel 2022 si è [deciso](https://www.asuit.tn.it/notizie/trasformazione-digitale-e-continuita-operativa-asuit-illustra-lo-stato-dei-sistemi-e-il) di non avere più software sviluppati internamente:

> Si è trattato di un progetto Pnrr molto importante, che, se da una parte ha portato in Trentino risorse economiche rilevanti, senza le quali le azioni di rinnovo delle applicazioni sarebbero state a totale carico dell’azienda e della collettività, dall’altra è partito con vincoli stringenti di tempi, standard tecnologici e percorso di acquisto tipici del Pnrr stesso. Si è deciso nel 2022 – come la quasi totalità delle aziende sanitarie italiane – di **non procedere a sviluppi interni o a evoluzione dell’attuale sistema** ma alla selezione di un prodotto di mercato certificato.

L'assessore alla sanità Antonio Tonina è sotto le bombe ma non pare avere molta contezza della situazione visto che il 30 luglio 2026 [ha detto](https://www.rainews.it/tgr/trento/video/2026/07/ennesimo-tilt-dei-sistemi-informatici-della-sanita-trentina-285fd54b-0df7-4387-bf02-45bcd53e5f11.html):

> Credo che adesso chi ha la competenza, chi ha la professionalità assolutamente ci deve dire perché questa situazione diventa veramente difficile.

Il direttore generale [Antonio Ferro](https://trentinotv.it/news_dettaglio.php?id=19876586) ha invece parlato dell'ipotesi di fare un'altra gara (ancora!) per risolvere i problemi:

> Se io potessi con alcuni farei anche una disdetta, una recessione dell'incarico, ma è chiaro che poi cosa fa l'azienda? Non c'è assolutamente possibilità perché per fare dei subentri ci vogliono mesi e mesi, ci vuole un'altra gara.

Ha anche detto che "immaginare di avere zero problemi per sempre è pura utopia" e che bisogna pensare a "come garantire agli operatori di proseguire nel loro lavoro anche a fronte di crash informatici".

Alessandro Bazziga, direttore dipartimento tecnologie e trasformazione digitale, ogni tanto tirato in ballo perché è laureato in pedagogia indirizzo filosofico, [ha](https://www.radioetv.it/2026/08/04/rttr-notizie-sera-del-04-08-2026/) [detto](https://sitotv33.s3.eu-central-003.backblazeb2.com/tg33tn/tg33tn_2026-08-04_1900.mp4):

> Abbiamo un prodotto che pur essendo presente in moltissime altre parti d'Italia ha in Trentino instabilità dovute alle personalizzazioni, che giustamente in modo sacrosanto abbiamo chiesto perché il prodotto deve fare quello che i nostri medici ci chiedono che debba fare e non deve fare quello che si inventa l'informatica di fare. Abbiamo fatto queste personalizzazioni, abbiamo chiesto al fornitore che le faccia, e il risultato è nell'ultimo periodo assolutamente insoddisfacente, lo definirei imbarazzante.

L'ASUIT ha annunciato delle contromisure, che sarebbero:
- Saranno imposte penali alle aziende appaltatrici responsabili dei software problematici.
- Sarà garantita la presenza 24 ore su 24 di un tecnico informatico in ognuno dei 7 ospedali.
- Sarà svolto un audit esterno, probabilmente da parte del politecnico di Milano, del percorso di digitalizzazione dell'ASUIT.

---

Se devo riassumere in pochi punti la situazione, direi questo:

- L'ASUIT ha scelto di **non avere più competenze interne** e di **delegare il software che fa funzionare il sistema sanitario a fornitori esterni**, acquistandolo di fretta perché c'erano 20 milioni di euro da spendere e sono stati "costretti" (cit.) a spenderli.
- I fornitori esterni si sono dimostrati poco competenti, in linea con la **reputazione delle grandi software house multinazionali** (Accenture, Engineering, Reply, ecc.) che da decenni producono sistematicamente software mediocre, malprogettato e di generale scarsa qualità con costi elevati per i cittadini che non possono così godere di servizi digitali di qualità né vedere rispettati i propri diritti.
- Il direttore generale sostiene di avere le mani legate (chi le ha legate? mumble mumble), mentre il quasi settantenne assessore alla sanità probabilmente [non ci capisce molto](https://static.wikia.nocookie.net/memepediadankmemes/images/0/01/297.jpg/revision/latest?cb=20180908193511) e si limita a dire che chi ci capisce deve dire qualcosa.
- Il direttore generale se potesse farebbe già disdetta, dopo meno di un anno, e pensa che sia inevitabile che il software continuerà ad avere problemi.
- Il direttore delle tecnologie dice che il software non era adatto e che è stato modificato per evitare che facesse "quello che l'informatica si inventa di fare".

La situazione è assurda: **si sceglie di proposito di dismettere le competenze interne**, lo si sbandiera nei comunicati stampa, si acquistano di fretta software non adatti, per poi arrabbiarsi battendo i pugni che le cose non funzionano e difendendosi dicendo che si ha essenzialmente zero controllo sui propri sistemi critici. Senza però riconoscere che il risultato è il frutto delle proprie scelte, in teoria consapevoli ma evidentemente **poco lungimiranti**.

Il famoso SIO, che sta facendo impazzire i pronto soccorso, era [precedentemente](https://www.trentinosalute.net/content/download/12170/224788/file/is013web.pdf) sviluppato internamente e aveva supportato il sistema sanitario per due decenni, senza problemi rilevanti da quel che risulta cercando online. Un caso di successo da tenere a mente, replicare e migliorare, si potrebbe dire.

Eppure la direzione scelta negli ultimi anni è stata esattamente opposta, cioè **esternalizzare il più possibile** riducendo progressivamente le competenze interne ed essenzialmente ignorando l'esistenza della in-house Trentino Digitale (che in teoria dovrebbe avere le capacità per portare avanti progetti complessi ma che nel concreto è in buona parte una stazione appaltante con sempre meno competenze e poca visione).

Una possibile obiezione a queste righe è che la scelta fatta comporti un **risparmio** e che acquisire prodotti dal mercato anziché realizzarli e mantenerli costi quindi meno, ma non ne sono convinto. Sono in gioco decine di milioni di euro, quando il bilancio intero di Trentino Digitale, che gestisce centinaia di servizi e applicazioni della provincia, è di circa 60 milioni.

Nell'era dell'AI, che ha aumentato significativamente la produttività, **queste risorse potrebbero finanziare interi team interni (e locali) di eccellenza**, con alta specializzazione e con retribuzioni adeguate, per modernizzare l'ecosistema software. Sostenere che affidarsi ai bandi PNRR non ricadata sulla collettività è insensato dato che fra pochissimi anni questi appalti milionari (che puntualmente finiscono in mano di multinazionali concentrate a Milano) andranno rinnovati.

La provincia autonoma di Trento ha a disposizione **risorse economiche** che le regioni a statuto ordinario non hanno: sarebbe un'occasione imperdibile per finanziare un sistema che renda **il Trentino pioniere di una nuova generazione di servizi pubblici locali digitali, innovativi, moderni e open source** (come previsto dal CAD). Seguendo le migliori pratiche di progettazione e sviluppo, raccogliendo i migliori talenti dell’università, mettendo alla guida un CTO laureato in informatica in questo secolo, magari liberandoci del concetto di “trasformazione digitale” (non c'è più niente da trasformare, si tratta di progettare digital-first) e rendendo questo lavoro, questa competenza e questa trasparenza **la miglior pubblicità per alimentare automaticamente il sistema dell’innovazione locale**.

Non significa ovviamente bandire completamente servizi e software privati dalla pubblica amministrazione, ma rendersi conto che l'approccio attuale porta *sistematicamente* a servizi mediocri. Le grandi software house a cui vengono assegnati questi appalti si dimostrano *ogni singola volta* completamente incapaci di realizzare servizi digitali di qualità. Di fronte a questo **non c'è nessun motivo ragionevole per continuare a spendere valanghe di soldi per fare le cose male.**

(Queste software house sono onnipresenti perché sono le uniche in grado di partecipare alle gare enormi indette da CONSIP; le regioni sono spesso forzate ad aggregarsi a questi bandi, anche se sono fatti con un metodo criticato da [almeno un decennio](https://teamdigitale.governo.it/it/future.htm) perché escludono quasi sempre le piccole e medie imprese e le startup tecnologiche, spostando tra l'altro le risorse dai territori verso multinazionali tipicamente di proprietà di fondi internazionali di private equity senza alcun reale interesse per il contesto locale. Cosa succeda dentro queste aziende di consulenza, che spesso lavorano in modalità *body rental* di basso livello, e cosa ne pensino in media le persone di lavorare lì lo si capisce sfogliando [testimonianze](https://www.reddit.com/r/ItaliaCareerAdvice/comments/1tc29h3/convincetemi_a_lasciare_accenture/) e [opinioni](https://www.reddit.com/r/techcompenso/comments/1u86xog/accenture_si_rafforza_in_italia_con_due/) che si trovano online.)

E insomma è faticoso sapere che fare le cose diversamente è possibile — è stato fatto in un contesto più complesso e con maggiori resistenze [come quello nazionale](https://teamdigitale.governo.it/it/future.htm) — e vedere che si preferisce invece fischiettare, quando va bene, o direttamente sfasciare di proposito quel poco che resta, alimentando un declino di competenze che porta a servizi critici palesemente inadeguati a discapito di tutti.

I disservizi *sono* evitabili e un software *può* essere stabile. Ma mentre siamo occupati a far funzionare le basi, come garantire che l'accettazione al pronto soccorso funzioni senza interruzioni (!), **ci stiamo perdendo e stiamo rinunciando a infinite possibilità di innovazione** che dovrebbero invece occupare gli ordini del giorno.

(Solo per il fascicolo sanitario elettronico mi vengono in mente un milione di idee che di questo passo potremmo non vedere mai: al momento non si possono pagare le visite in anticipo tramite l'app, non si possono vedere le ricette bianche, non ci sono le notifiche per nuovi referti come i risultati delle analisi [a due anni dall’annuncio](https://www.ufficiostampa.provincia.tn.it/Comunicati/TreC-ampliate-le-funzionalita-di-app-e-portale) dell'attivazione delle notifiche, non ci sono promemoria per i richiami vaccinali o per gli screening, non si vedono gli appuntamenti vaccinali una volta fissati, per trovare le informazioni su una visita (a che ora è, dove bisogna andare) servono 4 tap, decine di secondi di caricamento per finire su un PDF in A4, ecc.)

Se si continuerà sulla strada attuale di **appaltare l'innovazione**, i servizi pubblici che dovrebbero essere nativamente digitali si fossilizzeranno, proprio nel momento di massima potenzialità.

In ogni momento dovrebbe invece esserci una roadmap che stabilisca “cosa facciamo nei prossimi tre mesi per semplificare la vita delle persone”, che sia il personale sanitario o i cittadini. Fare questo dipendendo da bandi e fornitori completamente disallineati con la missione e senza una cultura della qualità (la Accenture di turno ritiene un progetto completato con successo una volta spuntate tutte le checkbox; ha ragione perché c'è scritto così nel contratto, ma è un approccio lontanissimo dal mettere al centro le persone nella progettazione e sviluppo dei servizi) è **garanzia di fallimento**.
