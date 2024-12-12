---
title: "Come funzionerà IT Wallet"
date: 2024-12-12T09:00:00+01:00
lastmod: 2024-12-12T09:00:00+01:00
slug: it-wallet
summary: "Sono arrivati i documenti digitali nell'app IO, un primo passo verso IT Wallet e l'interoperabilità con EUDI Wallet."
showtoc: true
---

Da dicembre 2024 nell'app IO è possibile creare la **versione digitale** di documenti come **la patente, la tessera sanitaria** e la carta europea della disabilità, un primo passo verso l'implementazione del sistema **IT Wallet** e la relativa interoperabilità con gli altri paesi europei tramite il progetto EUDI Wallet.

Ho notato che **c'è una grande confusione online**, specialmente attorno alla patente digitale: molti pensano che la patente digitale sia l'immagine della patente mostrata nell'app, altri pensano che la patente sia qualcosa di verificabile tramite il codice QR mostrato nell'app e che quindi il QR vada mostrato alle forze dell'ordine per le verifiche.

Non è vera né una né l'altra cosa, quindi facciamo un po' di ordine.

*Mega disclaimer: IT Wallet e EUDI Wallet sono sistemi molto complessi di cui ho una comprensione parziale. Commenti e precisazioni sono apprezzati.*

{{< fig src="documenti-su-io.jpg" >}}

Per cominciare, alcune cose che **IT Wallet non è o non fa**, attualmente:

- Il documento digitale non è un'immagine: la rappresentazione della patente che vedete nell'app IO è appunto solo una rappresentazione grafica del documento digitale.
- Il "certificato di autenticità" offerto come codice QR nell'app IO non contiene i dati della patente o del documento digitale.
- La presentazione del documento digitale per la verifica al momento non avviene con la scansione del codice QR.

Cos'è invece IT Wallet:

- È l'implementazione di **eIDAS 2**, il regolamento europeo per l'identificazione elettronica, che definisce i requisiti base del sistema EUDI (portafoglio digitale europeo). Sarà obbligatorio per tutti gli Stati dell'Unione Europea entro il 2026.
- Nello specifico, IT Wallet si basa sull'[architettura di riferimento](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/1.4.0/arf/) EUDI Wallet, che specifica la terminologia, le best practice e i protocolli da usare. L'implementazione italiana è documentata [qua](https://italia.github.io/eudi-wallet-it-docs/versione-corrente/en/index.html).

### L'architettura EUDI Wallet

L'architettura di un wallet europeo è a prima vista piuttosto complessa:

{{< fig src="eudi-wallet-architecture.png" >}}

In sintesi:

- L'utente installa un'app EUDI Wallet (*EUDI Wallet Instance* nello schema). In Italia è **l'app IO**.
- Andando verso sinistra, l'app [si interfaccia](https://italia.github.io/eudi-wallet-it-docs/versione-corrente/en/pid-eaa-issuance.html) con diversi possibili provider di documenti digitali. Ad esempio il **PID Provider** fornisce la carta d'identità digitale, mentre il **QEAA Provider**, che sta per *Qualified Electronic Attestation of Attributes*, fornisce documenti di altro tipo ma riconosciuti dalla legge, come la patente digitale. In entrambi i casi si usano degli appositi [formati standard](https://italia.github.io/eudi-wallet-it-docs/versione-corrente/en/pid-eaa-data-model.html). Nel caso italiano al momento l'unico *QEAA Provider* è **l'Istituto Poligrafico e Zecca dello Stato (IPZS)**, che emette le versioni digitali dei documenti. La carta d'identità non è ancora supportata ma sarebbe anch'essa emessa dall'IPZS, come avviene per la CIE.
- Ciascun provider si affida a delle sorgenti (*Authentic Source*) per ottenere i dati. Ad esempio per la patente è **la motorizzazione civile**, che fa capo al Ministero dell'Interno.
- Infine, i *PID* (le carte d'identità) e le *QEAA* (le attestazioni di altri documenti come la patente) possono essere esposti per la verifica a una *Relying Party*, cioè ad altri enti (pubblici o privati) che possono voler accedere ai documenti digitali, sia in presenza che in remoto. Questa fase richiede sempre una conferma interattiva da parte dell'utente.

### IT Wallet nelle more 😋

IT Wallet al momento **implementa solo i primi tre punti**, e cioè l'app IO si interfaccia con l'Istituto Poligrafico e Zecca dello Stato per generare i documenti digitali, i cui dati vengono importati dal ministero o dall'ente di turno e poi **firmati digitalmente** in modo da garantirne la validità e l'integrità a livello crittografico.

Manca però [ancora](https://github.com/pagopa/io-react-native-wallet/tree/3d801ea6162aab4d06510c56eb42d0113be42a15/src/credential/presentation) l'ultimo pezzo, cioè la possibilità per l'app IO di trasmettere le attestazioni dei documenti in modo digitale, sicuro e certificato.

Si legge infatti nell'articolo 64-quater del Codice dell'Amministrazione Digitale che le versioni digitali dei documenti sono esposte dall'app IO **«nelle more della piena funzionalità del Sistema IT-Wallet»**, cioè in modo transitorio in attesa che si completi l'implementazione.

Per quanto riguarda la patente si dice ad esempio che:

> La patente di guida mobile è la versione digitale della patente di guida di cui un conducente residente [...] è titolare. Tale patente mobile consente la verifica, tramite collegamento con l'anagrafe nazionale degli abilitati alla guida [...] dell'esistenza e della validità del diritto alla guida del suo titolare ed è equipollente a documento di identità dello stesso. Ai fini della circolazione sul territorio nazionale la patente di guida mobile soddisfa gli obblighi di cui all'articolo 180 [del codice della strada, cioè l'obbligo di esibire il documento quando richiesto].

Tradotto: la patente digitale è equiparata alla patente fisica e **la procedura di verifica della patente è la stessa di sempre**, cioè le forze dell'ordine una volta letti i dati della patente possono inserirli nell'anagrafe delle patenti per verificarne la validità.

Questa versione è confermata anche da una [circolare](http://www.patente.it/normativa/circolare-22-10-2024-n-32079-sistema-it-wallet?idc=4909) del 22 ottobre del Ministero dell'Interno, dove si dice che la verifica dell'esistenza e della validità della patente «deve essere svolta, come di consueto, attraverso la consultazione dell’anagrafe nazionale degli abilitati alla guida».

Non c'è quindi da mostrare (per ora) nessun codice QR. Ognuno poi valuti la scomodità di dover (probabilmente) consegnare il proprio smartphone agli agenti di turno per la verifica, dato che devono trascrivere i dati necessari per la ricerca nei sistemi.

### A cosa serve il codice QR?

Il codice QR, che l'app chiama "certificato di autenticità" senza spiegare molto bene cosa sia, contiene un URL fatto così:

```http
https://verify.wallet.ipzs.it/?tm=eyJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJleUowZVh...
```

Va avanti così per quasi 2.000 caratteri perché contiene un token **JWT**, cioè un testo firmato digitalmente in modo da garantirne la validità.

Guardiamo cosa c'è dentro il JWT, dopo averlo decodificato:

```json
{
  "alg": "ES256"
}
{
  "iss": "eyJ0eXAiOiJ3Y...",
  "sub": "**93**2**L",
  "subtyp": "MDL",
  "iat": 1733923793,
  "exp": 1733923913
}
```

Come si vede, non ci sono i dati della patente, ma soltanto:

- Il **tipo di documento** digitale (in questo caso "MDL", Mobile Driver License).
- Il **numero del documento**, [offuscato](https://github.com/pagopa/io-react-native-wallet/blob/3d801ea6162aab4d06510c56eb42d0113be42a15/src/utils/string.ts) dall'app (ho modificato soltanto le cifre, gli asterischi c'erano già).
- Il momento in cui il JWT è stato generato e la relativa scadenza (2 minuti dopo).

Il campo `iss` contiene un altro JWT firmato che [attesta](https://github.com/pagopa/io-react-native-wallet/blob/3d801ea6162aab4d06510c56eb42d0113be42a15/src/credential/trustmark/get-credential-trustmark.ts#L103) la validità e l'integrità della *Wallet Instance*, cioè l'installazione dell'app, con un complesso formato documentato [qua](https://italia.github.io/eudi-wallet-it-docs/versione-corrente/en/wallet-attestation.html).

Questo sistema è chiamato [Trust Mark](https://github.com/pagopa/io-react-native-wallet/tree/3d801ea6162aab4d06510c56eb42d0113be42a15/src/credential/trustmark) e l'IPZS [spiega](https://verify.wallet.ipzs.it/condizioni_generali.html) che «ha come finalità esclusiva quella di offrire agli utenti informazioni in merito all’autenticità del documento digitale [...] e all’emissione dello stesso ad opera della medesima Società». Certifica cioè che il documento è stato **effettivamente emesso dall'Istituto Poligrafico** e che è legato alla specifica installazione dell'app, ma non è un modo per trasmettere in modo sicuro i dati del documento.

### Come ci si autenticherà con IT Wallet

A regime, il sistema permetterà la trasmissione e la verifica dei documenti digitali [tramite due sistemi](https://italia.github.io/eudi-wallet-it-docs/versione-corrente/en/relying-party-solution.html):

- **In remoto**: l'utente potrà ad esempio scansionare un codice QR e autorizzare la trasmissione dei dati a un servizio online terzo (sia pubblico che privato), oppure in modo analogo tramite un protocollo apposito se si è sullo stesso dispositivo.
- **In presenza**: le attestazioni dei documenti sono scambiate in modo sicuro tramite una combinazione di tecnologie di prossimità, ad esempio codici QR a breve durata, NFC o Bluetooth, anche in assenza di connettività.

In entrambi i casi i dati sono scambiati tramite un formato standard internazionale che permetterà l'interoperabilità con gli altri wallet europei.

{{< fig src="remote-flow.png" >}}

Il secondo sistema, chiamato ***proximity flow***, è quello che permetterà (eventualmente) alle forze dell'ordine di ottenere la versione digitale della patente su un dispositivo di verifica. Nella versione italiana dovrebbe funzionare così:

1. L'utente mostra un apposito **codice QR al verificatore**, che lo scansiona tramite un'apposita app certificata.
2. Tramite i dati contenuti nel codice QR (tra cui ci sono delle chiavi crittografiche da cui derivare una chiave di sessione condivisa e temporanea) viene stabilita una connessione sicura tramite **Bluetooth Low Energy** tra il dispositivo del verificatore e lo smartphone dell'utente. Il dispositivo verificatore trasmette quindi tramite Bluetooth una richiesta di accesso al documento digitale, e le sue chiavi crittografiche.
3. L'utente revisiona i dati per i quali è stato richiesto l'accesso e **conferma la condivisione**. I dati vengono quindi trasmessi in modo cifrato al verificatore e la sessione viene chiusa subito dopo.

{{< fig src="proximity-flow.svg" >}}

La fase più critica è probabilmente quella che richiede una connessione Bluetooth, che sarà comunque completamente automatizzata, trasparente e idealmente istantanea. Lo standard che definisce la procedura è ISO/IEC 18013-5, che purtroppo come tutti gli standard ISO è consultabile solo a pagamento. Dalle bozze che si trovano online si legge però che il dispositivo verificatore deve poter agire sia da server che da client nella connessione Bluetooth ed è identificato da un UUID fisso per tutti i dispositivi verificatori. Non c'è comunque il rischio di inviare i dati al dispositivo errato grazie al flusso con doppio scambio di chiavi descritto sopra.

Ipotizzo che il sistema sia così complesso perché deve supportare non solo lo scenario di fornire i documenti a un'autorità pubblica ma anche ad enti privati, supportando documenti digitali di vario tipo. C'è quindi la necessità che i documenti siano trasmessi solo **dopo esplicita autorizzazione, in modo non intercettabile, non replicabile e anche in assenza di connettività**.

---

Per ora questo è quello che sono riuscito a ricavare. Nei prossimi mesi si dovrebbe sapere di più su come si evolverà IT Wallet nell'app IO: dovrebbero arrivare la verifica dei documenti con il sistema descritto sopra, il funzionamento offline e la carta d'identità.

Per aggiungere qualcosa o inviare correzioni, i commenti sono qua sotto. Sessione chiusa.
