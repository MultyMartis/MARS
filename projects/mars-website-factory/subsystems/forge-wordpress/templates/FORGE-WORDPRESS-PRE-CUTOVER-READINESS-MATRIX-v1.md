# WP Forge — Pre-cutover readiness matrix template v1

Project:  
Host now:  
Final host:  
Date:

| ID | Gate | PASS/FAIL/NA | Evidence |
|----|------|--------------|----------|
| ENV | Environment = production; debug off | | |
| HYG | Public webroot hygiene | | |
| USR | Users/admin set clean | | |
| PAR | Source/prod code parity | | |
| BAK | Fresh full backup after freeze | | |
| RED | Legacy redirects | | |
| DNS | Zone inventoried (A/AAAA/MX/SPF/DKIM/TXT/…) | | |
| MAIL | Mail records copy plan | | |
| NS | A-record vs NS delegation decided | | |
| SSL | Cert steps after DNS | | |
| URL | home/siteurl + bounded URL migrate plan | | |
| FRM | Forms handler ready | | |
| SMTP | Sequenced after domain smoke | | |
| IDX | Indexing closed until gate | | |
| WPL | WPilot write_enabled=false | | |
| GIT | Canonical checkpoint | | |

**GO / NO-GO for NS or A-record switch:**  

---

*Template v1.*
