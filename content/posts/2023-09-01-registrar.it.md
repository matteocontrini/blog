---
title: "Confronto registrar domini .IT"
date: 2023-09-05T09:00:00+02:00
lastmod: 2023-09-05T09:00:00+02:00
slug: registrar
summary: "Un confronto dettagliato tra alcuni registrar accreditati per i domini .IT."
showtoc: true
---

Ho selezionato alcuni tra i principali registrar accreditati presso il Registro.it che vendono domini con TLD .IT e raccolto le principali funzionalità che ritengo un registrar dovrebbe avere.

Questi parametri di valutazione sono solo quelli oggettivi: non includono cioè la valutazione della generale reputazione e affidabilità dell'azienda o del servizio, l'assistenza, la qualità della UI, l'accettabilità del prezzo, simpatie varie, ecc.

Tutti i prezzi sono IVA esclusa.

<div id="mobile-instructions">

*Se navighi da smartphone o tablet, puoi scorrere la tabella orizzontalmente.*

</div>

<style>
@media screen and (min-width: 1200px) {
    #table-container {
        margin-left: calc(-100vw / 2 + (var(--main-width)) / 2 + var(--gap));
        margin-right: calc(-100vw / 2 + (var(--main-width)) / 2 + var(--gap));
    }
    #table-container > table {
        margin: 32px auto;
        width: fit-content;
        max-width: 100%;
        overflow-x: visible;
    }
    #mobile-instructions {
        display: none;
    }
}
#table-container > table thead th {
    font-size: 100%;
}
#table-container > table td,
#table-container > table th {
    border: 1px solid var(--border);
    padding: 8px 8px;
    line-height: 1.4;
}
#notes-container p {
    margin: 0;
}
</style>

<div id="table-container">

|                                          | Aruba                          | Register.it           | Keliweb                 | Host.it               | Netsons               | Shellrent                  | Tophost               | Flazio           | OVH                   | Bitname          |
|------------------------------------------|--------------------------------|-----------------------|-------------------------|-----------------------|-----------------------|----------------------------|-----------------------|------------------|-----------------------|------------------|
| Prezzo .it (1° anno)                     | 0,99€                          | 0€                    | 6,90€                   | 6€                    | 7,59€                 | 4,90€                      | 5,99€                 | 3,99€            | 2,99€                 | 6,25€            |
| Prezzo .it (dal 2° anno)                 | 10,99€                         | 45,55€                | 7,90€                   | 6€                    | 7,59€                 | 9,99€                      | 5,99€                 | 3,99€            | 8,99€                 | 6,25€            |
| Azienda italiana 🇮🇹                    | ✅                              | ✅                     | ✅                       | ✅                     | ✅                     | ✅                          | ✅                     | ✅                | ❌                     | ✅                |
| Consenso whois                           | ✅                              | ✅                     | ❌ <small>ticket</small> | ✅                     | ✅                     | ✅ <small>sempre no</small> | ✅                     | ✅                | 🔸                    | ✅                |
| Nameserver custom                        | ✅                              | ✅                     | ✅                       | ✅                     | ✅                     | ✅                          | ❌                     | ✅                | ✅                     | ✅                |
| Nameserver durante trasferimento         | ✅ <sup>(1)</sup>               | ✅ <sup>(1)</sup>      | ✅                       | ✅                     | ❌                     | ✅ <sup>(2)</sup>          | ❌                     | ✅ <sup>(1)</sup> | 🔸                    | ✅                |
| Cambio registrante                       | 10€                            | 45,55€                | 9€                      | ✅ <sup>gratis</sup>   | ✅ <sup>gratis</sup>   | ✅ <sup>gratis</sup>        | ✅ <sup>gratis</sup>   | 🔸               | ✅ <sup>gratis</sup>   | ✅ <sup>gratis</sup> |
| Cambio contatti amministrativo e tecnico | ✅ <sup>(3)</sup><sup>(4)</sup> | ✅ <sup>(5)</sup>      | ✅ <sup>(3)</sup>        | ✅ <sup>(5)</sup>      | ✅ <sup>(3)</sup>      | ✅                          | ✅ <sup>(4)</sup>      | ✅ <sup>(3)</sup> | 🔸                    | ✅ <sup>(4)</sup> |
| Redemption                               | +0€                            | ?                     | +5€                     | +10€                  | +0€                   | +10€?                      | +>0€?                 | 🔸               | 49,99€                | 19€              |
| Domini geografici                        | ✅                              | ✅                     | ✅                       | ❌                     | ✅                     | ✅                          | ✅                     | ❌                | ✅                     | ✅                |
| DNS Anycast                              | ❌                              | ✅ F5                  | ❌                       | ✅                     | ❌                     | ❌                          | ❌                     | ❌                | +1,09€                | ❌                |
| DNSSEC interno                           | ❌                              | ✅                     | ❌                       | ❌                     | ✅                     | ✅                          | ❌                     | ❌                | ✅                     | ❌                |
| DNSSEC esterno                           | ❌                              | ✅                     | ❌                       | ❌                     | ❌                     | ✅                          | ❌                     | ❌                | ✅                     | ❌                |
| ALIAS/CNAME apex                         | ❌                              | ❌ <sup>(6)</sup>      | ❌                       | ❌                     | ❌                     | ❌                          | ❌                     | ❌                | ❌                     | 🔸               |
| TTL record                               | ❌ <sup>min 1h</sup>            | ✅                     | ✅                       | ✅                     | ✅                     | ❌ <sup>min 1h</sup>        | ❌                     | ❌                | ✅                     | ❌                |
| Wildcard record                          | ✅                              | ❌                     | ✅                       | ✅                     | ✅                     | ✅                          | ✅                     | 🔸               | 🔸                    | 🔸               |
| Statistiche DNS                          | ❌                              | ❌                     | ❌                       | ❌                     | ❌                     | ❌                          | ❌                     | ❌                | ❌                     | ❌                |
| API gestione DNS                         | ❌                              | ❌                     | ❌                       | ❌                     | ❌                     | ✅                          | ❌                     | ❌                | ✅                     | ❌                |
| Backup/esportazione DNS                  | CSV, TXT <sup>(7)</sup>        | TXT <sup>(7)</sup>    | ❌                       | JSON                  | CSV                   | BIND, Excel                | ❌                     | ❌                | BIND                  | ❌                |
| Redirect                                 | ✅ <small>root</small>          | ✅ <small>path</small> | ✅ <small>path</small>   | ✅ <small>root</small> | ✅ <small>path</small> | ✅ <small>path</small>      | ✅ <small>root</small> | ❌                | ✅ <small>root</small> | ❌                |
| Inoltro email                            | ❌                              | ❌                     | ✅                       | ❌                     | ✅                     | ❌                          | ✅                     | ❌                | ✅ <small>inbox 1GB</small>  | ❌            |
| 2FA                                      | ❌                              | ✅                     | ✅                       | ❌                     | ✅                     | ✅                          | ❌                     | ❌                | ✅                     | ✅                |

</div>

<div id="notes-container">

🔸 = non chiaro/da verificare

(1) si possono solo mantenere i NS esistenti, non sceglierne di nuovi

(2) l’assistenza dice di sì, io non ho trovato dove si fa ma evidentemente mi sono perso qualcosa

(3) sembra che tutti i contatti siano sincronizzati con quelli del registrante

(4) a occhio, registrante e amministrativo sono sincronizzati, tecnico è il registrar

(5) solo contatto amministrativo

(6) il supporto non capisce la domanda, assumo non si possa

(7) non è chiaro se l’esportazione TXT sia in formato BIND, da verificare

</div>

---

Alcune informazioni aggiuntive utili per valutare:

- il costo di registrazione/trasferimento di un dominio .IT presso il registro è di 4,00€ + IVA, il costo di rinnovo è 3,30€ + IVA
- il cambio registrante/intestatario presso il registro .IT dovrebbe essere gratuito
- con "redemption" si intende il recupero del dominio nei 30 giorni successivi alla cancellazione del dominio per mancato rinnovo. Il costo di recupero presso il registro è di 4,00€ + IVA

Se hai notato errori, puoi segnalarli con un commento qua sotto. I dati sono stati raccolti a inizio settembre 2023.
