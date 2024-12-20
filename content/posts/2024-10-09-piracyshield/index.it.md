---
title: "La pericolosa legge antipirateria, spiegata semplice"
date: 2024-10-09T17:00:00+02:00
lastmod: 2024-10-29T14:00:00+01:00
slug: piracyshield
summary: "Come funziona Piracy Shield, cosa è cambiato con le modifiche del 2024 e perché sta danneggiando Internet in Italia."
showtoc: true
---

*L'articolo è stato aggiornato il 29 ottobre 2024 e include ora due nuove sezioni, riguardanti il blocco dei servizi Google avvenuto per errore il 19 ottobre e i costi di Piracy Shield.*

---

L'8 ottobre 2024 sono entrate in vigore le **modifiche alla legge antipirateria**, che cambiano in modo controverso alcuni aspetti già prima molto criticati.

La legge mira a mettere fuori gioco siti web e app che diffondono illegalmente eventi sportivi in diretta, colpendo anche il cosiddetto "**pezzotto**", cioè il sistema di abbonamenti illegali a basso costo che permette di vedere una gran quantità di canali televisivi in streaming in modo abusivo.

Dal punto di vista tecnico la legge e la sua implementazione sono universalmente giudicate come **dannose**, perché **mettono a rischio il regolare funzionamento di Internet** in Italia normalizzando nel frattempo una nuova forma di censura che non era mai stata applicata prima (senza tra l'altro nemmeno risolvere il problema per cui la norma è concepita).

Il funzionamento di base prevede infatti che alcune **aziende e associazioni private**, come DAZN e la Lega Serie A, siano incaricate di inserire in una apposita piattaforma le **richieste di blocco dei siti web** che distribuiscono illegalmente contenuti sportivi protetti dal diritto d'autore. Questi blocchi devono poi essere **eseguiti entro 30 minuti**.

{{< fig src="agcom5.jpg" >}}

Non esiste però **nessuna verifica** né approvazione da parte di un'autorità: poche e per lo più sconosciute persone in Italia (non c'è una lista aggiornata dei soggetti considerati «attendibili») hanno il **potere di bloccare in modo sostanzialmente istantaneo qualsiasi risorsa di Internet**, con effetti potenzialmente catastrofici, senza nessun obbligo di trasparenza o assunzione di responsabilità in caso di errori (che ci sono già stati). La legge stessa specifica esplicitamente che tutto il processo può avvenire **«senza contraddittorio»**.

È molto controverso anche il contesto in cui la legge è nata, cioè **su [forte spinta e influenza](https://www.key4biz.it/serie-a-e-telco-devono-cooperare-a-difesa-della-legalita-de-siervo-lega-serie-a-blocco-siti-pirata-entro-30-minuti/436090/) da parte della Lega Serie A**. È stata proprio la Lega Serie A a realizzare la piattaforma informatica per il blocco dei contenuti illegali, quella a cui ora ci riferiamo con **Piracy Shield**, persino **prima dell'approvazione della legge che l'avrebbe istituita**. (Il codice sorgente è tra l'altro stato illecitamente diffuso online ed è ancora online nel momento in cui scrivo, dopo più di 6 mesi.)

E nonostante formalmente la legge interessi non solo il calcio ma in generale i «contenuti trasmessi in diretta», è addirittura l'Autorità per le Garanzie nelle Comunicazioni (AGCOM), responsabile del coordinamento di Piracy Shield, a [scrivere](https://www.agcom.it/competenze/antipirateria-e-piracy-shield/piattaforma-piracy-shield) che la piattaforma riguarda «gli eventi sportivi live». (E, guarda caso, l'immagine scelta per la pagina del sito è quella di un campo da calcio.)

Stando alle [scarsissime informazioni](https://www.dday.it/redazione/48808/piracy-shield-blocchi-indesiderati-vpn-multe-e-trasparenza-cosa-e-uscito-dalintervento-di-agcom-in-commissione) disponibili, per ora il sistema sembra in effetti limitato agli eventi sportivi, e in prevalenza alle partite di calcio della Serie A trasmesse da DAZN.

{{< fig src="agcom1.png" >}}

Nei prossimi paragrafi approfondiremo come funziona questa legge, cosa è cambiato con le modifiche del 2024, quali sono i rischi e perché in ogni caso questa legge non risolverà il problema della pirateria.

## Come è stata approvata

La legge antipirateria è la [numero 93 del 2023](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2023-07-14;93) e nonostante le fortissimi perplessità tecniche sollevate da esperti di reti e di sicurezza informatica è stata incredibilmente **approvata senza nemmeno un voto contrario** sia [alla Camera](https://documenti.camera.it/apps/votazioni/votazionitutte/schedaVotazione.asp?legislatura=19&RifVotazione=73_28&tipo=dettaglio) che [al Senato](https://www.senato.it/leg/19/BGT/Schede/Ddliter/votazioni/86_8.htm).

{{< fig src="votazione1.png" >}}

{{< fig src="votazione2.png" >}}

La riforma del 2024 è stata invece inserita frettolosamente con un paio di emendamenti ([6.0.35](https://www.senato.it/loc/link.asp?tipodoc=EMENDC&leg=19&id=1428931&idoggetto=1429611) e [6.0.36](https://www.senato.it/loc/link.asp?tipodoc=EMENDC&leg=19&id=1428932&idoggetto=1429611)) nella legge di conversione di un decreto legge che tratta tematiche fiscali.

Per arrivare a questa specie di riforma [non sono stati acquisiti](https://www.senato.it/leg/19/BGT/Schede/Ddliter/documenti/58480_documenti.htm) pareri tecnici da esperti della materia né si è svolta una discussione sugli articoli specifici, perché l'approvazione è avvenuta con la "fiducia", cioè tutto in blocco, e gli articoli in questione sono stati formulati nella loro versione finale solo il giorno prima dell'inizio della discussione in Parlamento, [di domenica](https://www.senato.it/japp/bgt/showdoc/frame.jsp?tipodoc=SommComm&leg=19&id=1428972&part=doc_dc).

Uno degli autori, sia del [disegno di legge](https://www.senato.it/leg/19/BGT/Schede/Ddliter/58480.htm) del 2024 che della legge originale, era **Claudio Lotito**, senatore di Forza Italia in forte conflitto di interessi per il fatto che è presidente della squadra di calcio Lazio. (Durante la [discussione in Senato](https://twitter.com/matteosonoioo/status/1841061289558196629) si è detto sicuro che questa legge «porterà dei ricavi importanti».)

## Internet, in un minuto

Per capire come funziona Piracy Shield dobbiamo fare una **breve sintesi di come funziona la navigazione web su Internet**. I due concetti da tenere presente sono quello dei **nomi di dominio** (ogni tanto chiamati "FQDN": l'AGCOM usa questo termine) e gli **indirizzi IP**.

I nomi di dominio sono gli indirizzi testuali dei siti web: ad esempio ora vi trovate su `matteosonoio.it`, il dominio per questo blog. A un dominio corrisponde un solo sito web, ma lo stesso sito web può essere accessibile tramite più domini.

Quando si prova ad aprire un dominio tramite un browser o un'app viene innescato un meccanismo (detto di "risoluzione") che tramite il sistema **DNS** "converte" il nome di dominio in un indirizzo di rete, o **indirizzo IP**. L'indirizzo IP è un numero dalla lunghezza fissa, ad esempio `35.156.224.161`.

{{< fig src="dns.png" >}}

L'indirizzo IP permette di sapere quale server deve essere contattato per scaricare le pagine web. Per essere precisi lo stesso indirizzo IP potrebbe in realtà corrispondere a più server (potenzialmente anche migliaia) e **nella maggior parte dei casi lo stesso indirizzo IP ospita più di un sito web**.

È il caso ad esempio dei cosiddetti "hosting condivisi", che costano molto poco (pochi euro al mese) e sono quindi degli spazi condivisi tra più siti. Un altro caso importante è quello delle **CDN**, delle reti specializzate nel rendere i siti web più veloci: **la stessa CDN**, e quindi gli stessi indirizzi IP, **può ospitare anche milioni di siti web**.

Secondo una delle [stime](https://blog.cloudflare.com/consequences-of-ip-blocking/) disponibili, in Europa ad ogni indirizzo IP corrispondono in media 24 nomi di dominio: vuol dire che **bloccando un indirizzo IP in media bloccheremo 24 siti** probabilmente diversi, e non uno solo.

## Si blocca, e si aggira

Per **bloccare un nome di dominio** bisogna agire sul processo di risoluzione dei nomi, manomettendo il sistema per fare in modo che il risolutore DNS restituisca non più l'indirizzo IP corretto ma uno fasullo o irraggiungibile, impedendo così di accedere al sito web richiesto.

Questo sistema è facilmente aggirabile semplicemente affidandosi a dei **servizi DNS pubblici** diversi da quelli decisi dal proprio operatore, ad esempio quelli di Google o di Cloudflare, che non applicano blocchi. Per questo motivo la legge antipirateria prevede che si possano **bloccare anche gli indirizzi IP direttamente**.

Il blocco di un indirizzo IP viene applicato dal proprio fornitore di accesso a Internet (bloccando l'instradamento del traffico) e il modo più comune per aggirarlo è **utilizzare una VPN**, uno strumento che creando un **tunnel virtuale** fa in modo che tutto il traffico venga cifrato, trasportato di solito all'estero e quindi fatto "uscire", aggirando le limitazioni locali.

## «Univocamente», anzi «prevalentemente»

Dato che un indirizzo IP può corrispondere a più siti web, la legge antipirateria nella sua versione originale specificava che **si potevano bloccare solo «gli indirizzi IP univocamente destinati ad attività illecite»**.

**"Univocamente"** era la parola magica che almeno sulla carta costringeva a verificare che un indirizzo IP ospitasse solo contenuti illegali e non anche altri contenuti leciti. «L'unica piccola barriera contro una norma completamente folle», [ha scritto](https://twitter.com/raistolo/status/1839064433492111501) Stefano Zanero, professore associato del Politecnico di Milano che si occupa di sicurezza informatica da oltre vent'anni.

Questa formulazione era comunque risultata da subito controversa: non esiste tecnicamente un modo per verificare in modo preciso che cosa ospita un indirizzo IP, si possono solo fare assunzioni e stime.

Questo fatto è stato evidenziato anche durante una [audizione](https://www.youtube.com/watch?v=ZvnxuFUzR5Y) alla Camera davanti ai rappresentanti dell'AGCOM, quando la deputata Giulia Pastorella (Azione) ha fatto presente che:

> L'impossibilità di avere univocamente un solo indirizzo IP per un sito ma al contrario la regolare occorrenza che per un indirizzo IP ci sono più siti è un tema che continuerà ad essere presente.

(Pastorella ha votato a favore della legge del 2023.)

Nella nuova versione della legge **la parola «univocamente» è stata sostituita da «prevalentemente»**: significa che ora **si potranno bloccare anche indirizzi IP** che non sono dedicati esclusivamente alla diffusione di contenuti illegali ma **che ospitano anche altri contenuti legittimi**.

Non è chiaro di preciso cosa si intenda con **"prevalenza"** (la legge non lo specifica) e non è quindi chiaro nemmeno quali saranno le implicazioni pratiche di questa modifica.

Sicuramente però non si renderanno i blocchi più precisi di prima e **sarà più difficile contestare** il blocco di un sito web legittimo, visto che la possibilità di avere degli effetti collaterali è ora prevista dalla legge.

## Bloccati per errore

La conseguenza ovvia di una legge di difficile applicazione tecnica è che i blocchi tendano ad essere più estesi del dovuto.

Un caso eclatante si è verificato a meno di un mese dall'entrata in servizio di Piracy Shield (1° febbraio 2024), quando **è stato [bloccato](https://twitter.com/handymenny/status/1761421069561282743) per errore un indirizzo IP di Cloudflare**, una CDN molto popolare che ospita decine di milioni di siti web.

{{< fig src="cloudflare1.png" >}}

Cloudflare ha [stimato](https://t.me/notedimatteo/763) che in questo caso il problema abbia riguardato **decine di migliaia di siti web**, che sono rimasti irraggiungibili dall'Italia per diverso tempo. Tra questi [c'era anche](https://twitter.com/handymenny/status/1761480886174757168) il sito web di un (piccolo) operatore telefonico italiano.

Secondo l'AGCOM il problema è durato meno di mezz'ora, ma è falso: è [provato](https://twitter.com/handymenny/status/1762061176609939779) che **i problemi si siano protratti per almeno 40 ore** e il motivo è che, incredibilmente, la piattaforma Piracy Shield al momento **non prevede una procedura formale di "sblocco"**. E cioè i blocchi vanno eseguiti per legge entro 30 minuti, mentre gli sblocchi possono richiedere anche giorni.

{{< fig src="cloudflare2.png" >}}

Dalle [informazioni che si è riusciti a raccogliere](https://www.youtube.com/live/2CUzcZZQZSs?t=1928), sembra che l'AGCOM si sia resa conto del blocco dell'IP Cloudflare dopo una **segnalazione fatta via SMS da Stefano Quintarelli**, noto imprenditore informatico, ideatore di SPID ed ex deputato, ma senza alcun coinvolgimento nel sistema antipirateria, a conferma del fatto che non esiste una procedura formale per rendersi conto degli errori.

Anche Giovanni Zorzoni, presidente dell'Associazione Italiana Internet Provider (AIIP), ha [spiegato](https://twitter.com/matteosonoioo/status/1848386081143640317) in un'intervista che, nonostante gli operatori avessero richiesto un canale di comunicazione diretto attivo 24 ore su 24 ore, al momento **le comunicazioni urgenti di eventuali problemi avvengono via WhatsApp**. A complicare la situazione c'è il fatto che gran parte dei blocchi avviene **fuori dagli orari lavorativi di AGCOM**, e non sembra esistere un presidio continuo del sistema da parte dell'autorità.

Dai dati pubblicati da AGCOM risulta che in 4 casi sono stati bloccati indirizzi IP che poi hanno richiesto uno sblocco, ma il dato è sbagliato: [da un'altra fonte](https://twitter.com/relationsatwork/status/1850451803525038103) generalmente affidabile si è scoperto che gli **indirizzi IP riabilitati** nei primi nove mesi di funzionamento sono stati ben **78**.

Oltre al caso Cloudflare e al blocco dei servizi Google, di cui parleremo sotto, ci sono stati altri blocchi erronei che hanno fatto discutere: sempre a febbraio 2024 sono stati [bloccati](https://www.dday.it/redazione/48464/piracy-shield-sta-censurando-siti-che-non-hanno-nulla-a-che-fare-con-la-pirateria-ed-e-un-problema-serio) degli indirizzi IP del servizio CDN **Zenlayer**, che risulta tutt'ora parzialmente bloccato. A ottobre 2024 sono invece stati [bloccati](https://twitter.com/matteosonoioo/status/1848271841061748845) degli IP di **Imperva**, un servizio di protezione dei siti web usato da moltissime banche e assicurazioni in Italia. Anche in questo caso gli indirizzi IP risultano ancora bloccati.

La situazione più surreale si è però venuta a creare ad agosto 2024, quando Piracy Shield [ha bloccato](https://twitter.com/matteosonoioo/status/1849536016765550955) **gli indirizzi IP che ospitano le pagine di avviso dei blocchi di TIM e Tiscali**. Significa che quando un sito web viene bloccato non può essere mostrata mostrata la pagina che informa del blocco perché la pagina stessa è bloccata dal sistema antipirateria. Al 29 ottobre 2024, due mesi dopo, l'IP Tiscali risulta ancora bloccato, a conferma del fatto che non vengono fatte verifiche serie sulle risorse bloccate e che la cosiddetta "prova forense" che dovrebbe essere allegata a ciascuna segnalazione come prova delle motivazioni del blocco è irrilevante.

{{< fig src="agcom6.png" >}}

## Il blocco dei servizi Google

Alle 18:56 del 19 ottobre è stato inserito [da parte di DAZN](https://www.agcom.it/comunicazione/comunicati-stampa/comunicato-stampa-2) il **blocco di un dominio e di un indirizzo IP appartenenti a Google**.

Il nome di dominio bloccato era `drive.usercontent.google.com`, utilizzato per i download da Google Drive. L'ipotesi più probabile è che un file su Google Drive venisse usato per distribuire una lista di siti web o in generale di URL per lo streaming di partite di calcio e che per questo l'intero dominio sia stato bloccato.

Per come funziona Piracy Shield il blocco è stato applicato dagli operatori immediatamente, e perciò chiunque provasse a scaricare file da Google Drive [otteneva un errore](https://twitter.com/146comp/status/1847728497101279493). (Il blocco del dominio non ha riguardato chi usava un resolver DNS diverso da quello del proprio operatore, come ad esempio i resolver DNS pubblici di Google e di Cloudflare, che non applicano blocchi.)

{{< fig src="drive1.png" >}}

Oltre al dominio è stato bloccato anche l'indirizzo IP `142.250.180.129`, uno dei tanti indirizzi IP usati dalla CDN di Google per fornire i propri servizi web. A causa di questo blocco sono stati segnalati disservizi non solo di Google Drive ma **[anche di YouTube](https://twitter.com/handymenny/status/1847776702790861022) e [di Google Traduttore](https://twitter.com/handymenny/status/1847968588075778126)**.

Non esiste una conferma ufficiale, ma [sembra che](https://www.dday.it/redazione/50824/piracy-shield-fuori-controllo-bloccata-per-6-ore-una-cdn-di-google-urge-una-riforma) il blocco sia stato revocato poco dopo la mezzanotte del 20 ottobre, cioè **più di 5 ore dopo**. I problemi si sono comunque protratti anche per [diverse ore dopo](https://twitter.com/g_bonfiglio/status/1847873197552668937) lo sblocco, in certi casi [anche per un'intera giornata](https://twitter.com/handymenny/status/1848049051859648939) (fortunatamente festiva).

Il presidente di AIIP Zorzoni ha [detto](https://twitter.com/matteosonoioo/status/1847973167806988593) in un'intervista che nemmeno agli operatori sono stati forniti dettagli su quanto avvenuto e che non si sa quindi né quale sia stata la reale motivazione del blocco né perché ci sono volute così tante ore per rendersene conto.

**L'AGCOM ha inizialmente minimizzato l'evento**, [dicendo che](https://www.youtube.com/watch?v=2CUzcZZQZSs) «il sistema funziona», parlando di «distrazione» ed evidenziando che nessuna trasparenza era dovuta («chi ha fatto la segnalazione è irrilevante») e che la piattaforma restava **«geniale, anche se un po' esplosiva»**, per poi invece pubblicare un [comunicato stampa](https://www.agcom.it/comunicazione/comunicati-stampa/comunicato-stampa-2) in cui accusava DAZN dell'errore.

In risposta a un'[interrogazione parlamentare](https://aic.camera.it/aic/scheda.html?numero=3/01513&ramo=CAMERA&leg=19) il Ministro delle imprese e del made in Italy Adolfo Urso (in Italia al momento non c'è un ministro per il digitale) ha invece [detto](https://twitter.com/matteosonoioo/status/1849096493463929171) che la causa del problema è Google, che non si era fatta inserire nella "whitelist", cioè la [lista delle risorse non bloccabili](https://www.wired.it/article/piracy-shield-white-list-come-funziona-domini/). Non risulta però esistere una procedura per farsi inserire in questa lista, che al momento evidentemente non include nemmeno Google, il sito web più visitato in Italia.

{{< fig src="interrogazione1.jpg" >}}

L'errore ha insomma evidenziato ancora una volta l'inadeguatezza del sistema ma ha anche esposto delle **spaccature all'interno di AGCOM**.

Il commissario Antonello Giacomelli, uno dei cinque membri del consiglio dell'AGCOM, ha [chiesto](https://www.fanpage.it/innovazione/tecnologia/piracy-shield-resta-in-funzione-il-commissario-agcom-cosi-non-va-andava-sospesa/) di **sospendere Piracy Shield** per permettere di ridefinire le responsabilità, revisionare le procedure e reingegnerizzare la piattaforma. Anche la commissaria Elisa Giomi ha chiesto la sospensione del sistema [esponendosi pubblicamente](https://www.linkedin.com/feed/update/urn:li:activity:7255158083138572290/) ed evidenziando **conflitti di interesse, mancanza di trasparenza e frettolosità**, problemi che avrebbe fatto notare dal principio ricevendo però spesso in risposta «reazioni virulente dei colleghi».

## Blocchi permanenti

Prima delle recenti modifiche alla legge **i blocchi di domini e indirizzi IP erano pensati per essere permanenti**, cioè una volta inseriti non era prevista ufficialmente una procedura per annullarli nel caso in cui non fossero più necessari.

Nel caso dei domini questo ha comportato che in pochissimi mesi si raggiungesse la quantità di **17mila domini bloccati**, un numero che rischiava di crescere ancora e che ha [costretto](https://www.wired.it/article/piracy-shield-limite-blocco-domini-governo-sblocco-indirizzi-ip/) l'autorità a pensare allo sblocco di alcuni di questi (ad oggi sono comunque quasi 18mila).

Se per i domini tutto sommato un numero così alto di blocchi non crea grossi problemi, per gli indirizzi IP la storia è diversa.

Va infatti considerato che **un indirizzo IP "bruciato"** molto probabilmente smetterà di essere utilizzato dai criminali che diffondono contenuti abusivamente e **tornerà quindi nella disponibilità del fornitore cloud** da cui l'IP è stato affittato.

Questo meccanismo "elastico" è la normalità nella maggior parte dei servizi cloud e implica che un indirizzo IP bloccato perché diffondeva streaming illegali **il giorno dopo potrebbe essere già stato riassegnato a un altro cliente "legittimo"**, non necessariamente italiano, ignaro del fatto che il proprio server non sarà raggiungibile dall'Italia. (C'è almeno un caso di questo tipo che è stato reso noto [pubblicamente](https://twitter.com/infinitybofh/status/1772933997988872578) da un utente, anche se non mi risulta sia stato poi verificato da altri.)

Al momento **gli indirizzi IP bloccati sono 5841** e di questo passo si finirebbe per bloccare **decine di migliaia di indirizzi IP in pochi anni**. Gli indirizzi IP sono tra l'altro una risorsa scarsa e **si eroderebbe così gradualmente e inutilmente lo spazio di indirizzamento utilizzabile**, che è già interamente in uso.

Tra l'altro, con le modifiche del 2024 la legge specifica esplicitamente che **non possono essere previsti limiti ai blocchi**, salvo poi contraddirsi una riga sotto imponendo che vengano considerati i limiti tecnici dei sistemi di blocco degli operatori, per cui non è al momento chiaro se un limite possa esserci oppure no (articolo 7-bis).

Nello stesso articolo c'è però una leggera miglioria su questo aspetto: una volta passati **6 mesi dall'inizio di un blocco** l'AGCOM dovrà ordinare la **riabilitazione** del dominio o dell'indirizzo IP, apparentemente a prescindere dal fatto che questi siano ancora usati per scopi illegali.

È stato inserito un altro nuovo articolo, il 5-bis, che dal punto di vista tecnico è insensato: richiede infatti ai «servizi di assegnazione di indirizzi IP» e ai registri dei domini di riabilitare i siti bloccati dopo «almeno sei mesi». La cosa strana è che questi soggetti non sono coinvolti in Piracy Shield e non sono mai menzionati altrove nella legge, per cui non è chiaro perché e come dovrebbero avere il potere di sbloccare le risorse.

## I reclami impossibili

Durante l'audizione alla Camera di marzo 2024, richiesta proprio in seguito al blocco per errore di Cloudflare, il presidente di AGCOM ha voluto minimizzare il problema:

> A noi non sono arrivati reclami, quindi questo fenomeno che è stato anche enfatizzato da taluni sul web in fondo non ha avuto una ricaduta in termini di specifici reclami. Non sono stati buttati giù siti che ospitavano anche altre cose.

Della stessa opinione era il commissario AGCOM Massimiliano Capitanio, che in un'intervista [aveva detto](https://tg24.sky.it/tecnologia/2024/02/21/piracy-shield-piattaforma-antipirateria) che si trattava di **«notizie assolutamente infondate e fasulle»** e che la procedura è «talmente rigorosa» che nessuna «pubblica amministrazione, ospedale, cantante, influencer» (sic) si sono lamentati.

Il blocco ha in realtà riguardato **decine di migliaia di siti web** e secondo delle indiscrezioni pubblicate dai giornali l'AGCOM [avrebbe ricevuto](https://twitter.com/matteosonoioo/status/1794763568266776938) (su stimolo di Cloudflare) circa **2.000 email di segnalazione**. Ci sono poi testimonianze di reclami formali inviati [tramite PEC](https://twitter.com/ernytech/status/1761723775169519688), difficilmente negabili proprio per il loro carattere "certificato".

Il problema di fondo è che inviare un reclamo secondo le regole di AGCOM è impossibile: l'autorità dice che ci si può lamentare solo **«entro 5 giorni dalla pubblicazione della lista dei blocchi effettuati»** (dopodiché i blocchi diventano definitivi), ma **la lista dei blocchi effettuati non esiste**.

{{< fig src="agcom2.jpg" >}}

La cosa più dettagliata che si trova [sul sito AGCOM](https://www.agcom.it/competenze/antipirateria-e-piracy-shield/piattaforma-piracy-shield) è un **file PDF** che si chiama "Elenco indirizzi IP bloccati" ma che in realtà non contiene un elenco di indirizzi bloccati ma soltanto il **numero dei blocchi effettuati**. Oltretutto, anche se questi dati fossero dettagliati va notato che spesso sono pubblicati anche con 20 giorni di ritardo, rendendo molto difficile farci affidamento.

{{< fig src="agcom3.png" >}}

A molti questo sembra un sistema appositamente pensato per disincentivare i reclami.

La deputata Pastorella ha fatto presente il problema al presidente di AGCOM:

> Come può qualcuno fare un reclamo se non sa che il proprio sito è stato oscurato a causa di questa normativa? La domanda è se i proprietari dei siti che vengono oscurati ricevono una notifica che fa riferimento a questa norma e quindi l'eventuale reclamo può avvenire sulla base di quella conoscenza, perché se semplicemente il mio sito web risulta oscurato ci possono essere mille motivi per cui questo succede, anche tecnici o di altra natura.

In risposta, il presidente ha dichiarato che è stata «predisposta la **possibilità di interrogazione** del sito dell'autorità che prevede che si possa immettere un indirizzo IP e ottenere la risposta». **Non è vero**: non esiste nulla del genere sul sito dell'AGCOM.

Anche nel caso in cui si riuscisse a capire come vanno inviati questi reclami (e si riesca a farlo entro i termini), l'AGCOM ha formalmente chiarito che non intende né divulgare alcuna informazione sui blocchi (nemmeno quelli erronei) né garantire che chi ha provocato il danno si assuma la responsabilità.

In risposta a una istanza di accesso civico l'AGCOM ha infatti [detto](https://twitter.com/ernytech/status/1772969422891647229) che la richiesta è stata «negata per motivata opposizione dei soggetti controinteressati». E cioè: le aziende e le associazioni come DAZN e la Lega Serie A hanno il **potere di bloccare senza verifica qualsiasi risorsa su Internet**, e se sbagliano possono poi **opporsi a qualsiasi richiesta di trasparenza o assunzione di responsabilità** e per l'Autorità per le Garanzie nelle Comunicazioni (!) va bene così.

{{< fig src="agcom4.png" >}}

L'AGCOM non ha mai corretto queste affermazioni false né ha chiarito l'influenza che i segnalatori sembrano avere sui processi interni dell'autorità, le cui attività [dovrebbero essere caratterizzate](https://www.agcom.it/istituzione) da «indipendenza e autonomia» con lo scopo di «tutelare i consumi di libertà fondamentali degli utenti».

## La piattaforma, e i costi

Un altro aspetto che ha suscitato dei dubbi è **l'opacità del processo** con cui **l'implementazione tecnica** della piattaforma Piracy Shield è avvenuta.

Il sistema risulta infatti [donato](https://www.agcom.it/provvedimenti/delibera-190-23-cons) ad AGCOM dalla Lega Serie A, che è anche uno dei soggetti segnalatori, e realizzato da SP Tech srl, startup innovativa "spin-off" dello studio Previti che si occupa tra il resto di contrasto alla pirateria online.

Una delle cose che fa storcere il naso è che la piattaforma sia stata **realizzata prima dell'approvazione della legge**: la legge è del 14 luglio 2023 e una settimana dopo la piattaforma era già pronta:

{{< fig src="agcom7.png" >}}

Seppur Piracy Shield sia stato donato, [risultano già](https://aic.camera.it/aic/scheda.html?numero=4/03300&ramo=CAMERA&leg=19) **66mila € di costi di manutenzione**. Secondo altre fonti l'impegno sarebbe invece di 58.500 € e farebbe parte di un **contratto di manutenzione** con la startup SP Tech srl. Un'[interrogazione parlamentare](https://aic.camera.it/aic/scheda.html?numero=4/03300&ramo=CAMERA&leg=19) ha però evidenziato come non risultino procedure pubbliche di affidamento per la piattaforma o per la sua manutenzione e l'associazione Assoprovider ha [presentato](https://assoprovider.it/piracy-shield-assoprovider-corte-dei-conti/) un esposto alla Corte dei Conti per **danno erariale**.

Dopo solo 4 mesi dall'entrata in funzione della piattaforma il commissario Capitanio ha [annunciato](https://www.calcioefinanza.it/2024/06/09/capitanio-agcom-nuova-piattaforma-antipirateria/) che è in sviluppo una nuova versione di Piracy Shield in grado di accogliere più operatori. Capitanio ha infatti dichiarato che il sistema «era pensato per 60/70 operatori» ma se ne sarebbero accreditati 300. (L'iscrizione a Piracy Shield è obbligatoria per tutti gli operatori, per cui AGCOM dovrebbe sapere quanti sono.)

Secondo indiscrezioni [riportate da Repubblica](https://www.repubblica.it/economia/2024/06/18/news/pezzotto_pirateria_agcom_dazn-423247121/) il costo della nuova versione di Piracy Shield sarebbe di ben **2 milioni di euro all'anno**, e infatti il commissario Giacomelli ha detto che i costi di gestione sono già andati [oltre quanto preventivato](https://www.repubblica.it/economia/2024/10/23/news/dazn_google_drive_piracy_shield_agcom_diffida-423573427/).

In ogni caso, è opinione diffusa che la piattaforma sia tecnicamente inadeguata: [si sono verificati](https://www.dday.it/redazione/48422/piracy-shield-nel-weekend-centinaia-di-blocchi-troppi-per-la-piattaforma-che-va-in-tilt) da subito problemi di stabilità del sistema e gli operatori hanno [lamentato](https://www.youtube.com/watch?v=expLn41hLMg) che per un periodo il 70% dei tentativi di accesso non andavano a buon fine. In generale il modello con cui è stato concepito scarica sugli operatori la responsabilità [e i costi](https://www.punto-informatico.it/piracy-shield-la-piattaforma-regalata-dalla-serie-a-costa-66-mila-euro/) per l'integrazione (particolarmente impattanti per gli operatori più piccoli).

## I DNS pubblici e le VPN

Era già chiaro nel periodo in cui la legge è stata concepita che questa legge non avrebbe risolto il problema della pirateria. Tutti i blocchi di cui abbiamo parlato sono infatti **facilmente aggirabili con strumenti come le VPN**, spesso gratuiti.

Sempre la deputata Pastorella, alla Camera:

> Le VPN sono un tema impossibile da gestire, sono strumenti che anche ragazzini di dieci anni sanno usare. Lo scetticismo è sul fatto che si possa combattere il fenomeno [delle VPN] all'interno di un provvedimento così.

Hanno deciso di provarci lo stesso: le modifiche del 2024 prevedono che ad applicare i blocchi entro 30 minuti non dovranno essere solo gli operatori ma anche «i fornitori di servizi di VPN e quelli di DNS pubblicamente disponibili ovunque residenti e ovunque localizzati».

In teoria quindi **anche i servizi DNS pubblici** come Google Public DNS e Cloudflare 1.1.1.1, così come **tutti i servizi VPN**, dovranno **aderire a Piracy Shield**. (Un testo precedente dell'emendamento parlava di "DNS alternativi" anziché "DNS pubblici", definizione che avrebbe assurdamente incluso anche tutti i resolver interni di aziende e università.)

È ovviamente impensabile che i servizi VPN basati all'estero e il cui scopo è precisamente fornire strumenti per aggirare le censure si adegueranno. Ma c'è il rischio che alcune VPN decidano di **uscire dal mercato italiano**, come è già avvenuto con [AirVPN](https://airvpn.org/forums/topic/57256-termination-of-service-in-italy/), uno dei servizi più sicuri e affidabili.

Anche ipotizzando che altri servizi seguano la strada di AirVPN, è comunque irrealistico pensare che lo facciano tutti i servizi VPN esistenti al mondo. Ci sarà quindi sempre un modo per aggirare i blocchi. (A meno che, naturalmente, non si inizi a bloccare persino l'accesso alle VPN (!) dall'Italia, o a sanzionare chi le usa, un'eventualità piuttosto distopica che per ora fortunatamente non sembra sia stata proposta da nessuno.)

## Segnali, o vai in carcere

La legge del 2024 modifica anche la legge sul diritto d'autore del 1941, introducendo l'obbligo per i fornitori di servizi di «**segnalare immediatamente** all'autorità giudiziaria o alla polizia giudiziaria» **situazioni «penalmente rilevanti»** legate alla pirateria o all'accesso abusivo a sistemi informativi nel momento in cui «vengono a conoscenza che siano in corso o che siano state compiute o tentante» queste condotte.

La lista di soggetti coinvolti è molto estesa: ci sono gli ISP (gli operatori), i motori di ricerca, le VPN, le CDN, i servizi DNS e altri servizi che agiscono come «reverse proxy server» (più o meno le CDN, ma la formulazione è un po' ambigua).

Non è al momento completamente chiaro cosa si intenda di preciso con «condotte penalmente rilevanti», ma dato che solo la diffusione abusiva di contenuti protetti da copyright è reato non dovrebbe rientrare la fruizione illegale (cioè ad esempio guardare una partita in streaming, nel cui caso è prevista "solo" una sanzione fino a 5.000 €). Potrebbe però rientrare l'uso del protocollo BitTorrent, dato che in quel caso lo scambio dei dati è quasi sempre bidirezionale.

Gli operatori, ecc. che vengono a conoscenza di questo tipo di attività illegale sono obbligati a «segnalare immediatamente», e se non lo fanno **la pena è «la reclusione fino ad un anno»** (non è chiaro di chi, di preciso).

Al momento non si sa nemmeno cosa si intenda con "venire a conoscenza", frase [contestata](https://x.com/matteosonoioo/status/1841061292544553083) anche al Senato dall'opposizione, in particolare dal senatore Antonio Nicita (PD). Crea qualche dubbio anche il fatto che andrebbero segnalate condotte illegali anche solo «tentate» e non compiute: il confine è insomma molto fumoso.

L'obbligo di segnalazione vale in teoria non solo per chi si trova in Italia ma per tutto il mondo: i soggetti menzionati sopra che si trovano fuori dall'Unione Europea dovrebbero quindi incaricare un rappresentante locale e comunicarlo all'Autorità.

Questa parte della legge sta ricevendo molte critiche perché è **molto vaga e di difficile applicazione**: sono pervenute «a mezzo governo» [lamentele](https://www.startmag.it/economia-on-demand/perche-google-tim-vodafone-wind-tre-iliad-e-fastweb-lanciano-pezzotti-al-governo-sulla-pirateria-on-line/) da moltissime aziende, tra cui **Google, TIM, Vodafone, Wind Tre, Iliad e Fastweb**, che fanno presente che **non esistono regole analoghe nel resto d'Europa**.

Si stanno lamentando anche **moltissime associazioni** che rappresentano gli operatori Internet e il mondo dell'informatica, tra cui [AIIP](https://www.aiip.it/legge-antipirateria-il-senato-tira-dritto-e-approva-gli-emendamenti-concordemente-contestati-da-tutti-gli-internet-provider-italiani/), [Assoprovider](https://assoprovider.it/tlc-assoprovider-allarme-per-il-rischio-carcere-agli-isp-nel-dl-omnibus-sulla-pirateria/), [Asstel-Assotelecomunicazioni](https://www.asstel.it/dl-omnibus-responsabilizzare-a-livello-penale-gli-operatori-di-telecomunicazioni-non-e-utile-a-contrastare-la-pirateria/) e [Anitec-Assinform](https://www.primaonline.it/2024/10/02/420890/dl-omnibus-e-pirateria-online-anitec-assinform-responsabilita-penale-sproporzionata-e-inefficace/).

Ad esempio, il presidente di AIIP ha dichiarato che questa è una «iniziativa irresponsabile che, nel solo interesse della lobby del calcio, calpesta gli operatori, l'Autorità e l'ecosistema Internet». Altri hanno fatto presente che questa nuova norma genererà ulteriori **nuovi costi per gli operatori**, costi che finora sono stati sostenuti in prima persona dagli operatori, oltre a **sovraccaricare l'autorità giudiziaria** con il rischio di generare anche un gran numero di ricorsi.

## 24mila blocchi dopo...

Secondo un dato riportato da TorrentFreak, [si stima](https://torrentfreak.com/10k-pirate-sites-blocked-in-60-days-piracy-shield-triggers-italian-kool-aid-crisis-240409/) che in Europa esistano circa 5mila siti che diffondono abusivamente contenuti sportivi in streaming. A ottobre 2024 Piracy Shield aveva bloccato quasi 24mila risorse tra domini e indirizzi IP, eppure, stranamente, il problema della pirateria non era ancora risolto.

Stride anche il fatto che [secondo l'AGCOM](https://www.agendadigitale.eu/mercati-digitali/capitanio-agcom-piracy-shield-funziona-smontiamo-le-critiche/) la piattaforma «funziona troppo bene» ed è un successo «mostruoso che meriterebbe titoli ad otto colonne» mentre per il senatore Lotito la legge ha avuto «scarsa applicazione» e per questo è stata modificata. In più, si sta anche [studiando](https://www.wired.it/article/piracy-shield-campionato-siti-ricorso-costi-concerti-film/) una nuova versione della piattaforma Piracy Shield, visto che la prima era a quanto pare tecnicamente inadeguata.

Non c'è al momento **nessun dato pubblicamente disponibile** che dimostri l'impatto che la legge antipirateria avrebbe avuto sulla pirateria, e soprattutto per ora **nulla suggerisce che la legge sia servita a spingere gli utenti ad abbonarsi ai servizi ufficiali**.

La realtà, in fondo nota a tutti, è che **la repressione non risolve il problema della pirateria**: ad esempio in Francia, dove sono previsti avvisi automatici agli utenti in caso di pirateria, i casi sono addirittura [aumentati](https://fr.wikipedia.org/wiki/Haute_Autorit%C3%A9_pour_la_diffusion_des_%C5%93uvres_et_la_protection_des_droits_sur_internet#Bilan) dopo l'introduzione della legge antipirateria nel 2009.

I sistemi di blocco sono inoltre facilmente aggirabile con una VPN: chi non vuole pagare per un contenuto sportivo o artistico non cambierà improvvisamente idea dopo aver letto che c'è una nuova legge più mirata. Se mai, si ingegnerà più di prima per aggirare i blocchi e i controlli.

A guardar bene poi il fenomeno della pirateria è già di suo [in costante declino](https://www.euipo.europa.eu/it/publications/online-copyright-infringement-in-eu-2023) da molti anni: **in Europa tra il 2017 e il 2020 è dimezzato**, per poi crescere leggermente durante la pandemia e poi stabilizzarsi.

{{< fig src="grafico1.png" >}}

Anche in Italia:

{{< fig src="grafico2.png" >}}

Lo certifica anche la FAPAV, un'associazione per la tutela dell'industria audiovisiva i cui studi sono spesso presi come riferimento per giustificare la necessità di Piracy Shield, [misurando](https://fapav.it/wp-content/uploads/2018/11/FAPAV_Ricerca-sulla-pirateria-audiovisiva-2023.pdf) un -52%:

{{< fig src="grafico5.png" >}}

L'Italia è tra l'altro il secondo paese con meno accessi pro capite alla pirateria nell'Unione Europea:

{{< fig src="grafico3.png" >}}

Il settore in cui la pirateria si è ridotta maggiormente a livello europeo è quello della musica, dove è stata stimata una riduzione degli accessi illegali dell'81% tra il 2017 e il 2020.

Uno dei motivi più citati è che la diffusione dei servizi in abbonamento come Spotify ha reso l'ascolto legale più comodo e persino più conveniente della pirateria. Secondo un [sondaggio](https://www.statista.com/forecasts/1000834/drivers-of-digital-video-or-audio-content-purchases-in-italy) pubblicato da Statista, il primo motivo per cui le persone in Italia acquistano contenuti video e audio legalmente è "per accederci in qualsiasi momento" e il secondo è proprio la convenienza economica.

Si può dire qualcosa di simile anche per il mercato dei film, delle serie tv e dei libri, ma difficilmente per lo sport in diretta, dove ad esempio **nel caso di DAZN i prezzi [continuano ad aumentare](https://www.ilpost.it/2024/05/17/dazn-aumenti-prezzi-2024-2025/)** a fronte di lamentele [ancora frequenti](https://www.digital-forum.it/threads/dazn-qualit%C3%A0-del-servizio-e-segnalazione-problemi.211543/page-568) per la **scarsa qualità del servizio**.

E a conferma del fatto che a differenza delle altre categorie di contenuti le piattaforme per vedere sport in diretta non sono considerate appetibili per i consumatori c'è il fatto che il consumo illegale di eventi sportivi è cresciuto negli ultimi anni (paradossalmente però è diminuito nel 2023, prima dell'entrata in servizio di Piracy Shield), anziché diminuire come per le altre categorie:

{{< fig src="grafico6.png" >}}

Secondo l'indagine FAPAV comunque **la pirateria di eventi sportivi in diretta è di gran lunga la meno rilevante**, con un'incidenza sulla popolazione del 15% contro il 21-30% delle altre categorie. (L'Italia è inoltre nella media europea per pirateria sportiva e non è quindi il paese europeo con più pirateria, come [sostiene](https://www.ilovepalermocalcio.com/de-siervo-italia-paese-del-pezzotto-e-qui-il-maggior-numero-di-pirati-in-europa/) la Lega Serie A.)

Non seguendo il calcio mi viene in aiuto Fanpage nello [spiegare](https://www.fanpage.it/sport/calcio/quanto-costava-vedere-il-calcio-in-tv-20-anni-fa-quando-la-serie-a-era-una-cosa-seria/) le difficoltà del settore calcistico:

> La Serie A ha tratto sostentamento in maniera quasi totalitaria dalla vendita dei diritti, che al momento in cui sono stati gestiti esclusivamente dalla Lega hanno rappresentato l'unica fonte di sostentamento dei club. Per questo in occasione di ogni bando di vendita l'istituzione che cura gli interessi del massimo campionato ambisce ad incassare cifre più alte.
>
> Questo spinge le emittenti ad alzare le cifre da far pagare poi per gli abbonamenti, con le conseguenze del tutto dunque che ricadono direttamente sugli appassionati.

A conferma di ciò c'è ad esempio il fatto che **DAZN paga la Lega Serie A ben [700 milioni di euro all'anno](https://www.milanofinanza.it/news/serie-a-diritti-tv-assegnati-a-dazn-e-sky-fino-al-2029-ai-club-vanno-900-milioni-l-anno-202310231516514546)** per i diritti di trasmissione, un importo molto elevato che l'azienda non sta riuscendo a sostenere con gli abbonamenti, con conseguente [riduzione dei costi di produzione](https://www.ilpost.it/2024/07/19/dazn-strategia-2025-esuberi-tagli/), e quindi della copertura giornalistica degli eventi, e aumento dei prezzi del servizio, visto che i circa 2 milioni di abbonati sembrano a malapena sufficienti per sostenere il costo dei diritti di trasmissione.

Come scrive Fanpage, con un modello di business migliore «ne avrebbero giovato tutti, con maggiori introiti per i club, e prezzi più accessibili ai tifosi che al momento hanno sulle spalle anche il sostentamento dei club, attraverso gli abbonamenti TV».

Va anche considerato che gli spettatori del calcio in TV sono [in continua diminuzione](https://www.dday.it/redazione/50722/calcio-in-tv-gli-ascolti-crollano-il-dieci-anni-persi-la-meta-degli-spettatori), e questo dovrebbe indurre a qualche riflessione. Scrive DDay:

> Se il prodotto non appassiona più, e deve essere così altrimenti gli ascolti non sarebbero calati così vertiginosamente, si preferisce spendere in altro.
>
> La Lega di Serie A, che chiede ogni tot di anni sempre più soldi portando inevitabilmente all'aumento dei prezzi degli abbonamenti, dovrebbe farsi qualche domanda.

E forse poi non ci sarebbe nemmeno il bisogno di interferire con il funzionamento di Internet per tentare di proteggere, probabilmente con scarsi risultati, l'industria del calcio.

---

*Grazie a [@handymenny](https://twitter.com/handymenny/), Hadx e Matteo C., enciclopedie viventi, per aver revisionato questo articolo, e a Andy Maxwell di TorrentFreak per il gentile aiuto nel lavoro di ricerca per la scrittura di questo articolo.*

*Sponsor moment: se hai un'azienda e invii tante email dai un'occhiata al mio servizio di monitoraggio [DMARCwise](https://dmarcwise.io/?ref=matteosonoio) (almeno non era un popup a schermo intero, dai).*
