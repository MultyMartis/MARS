# DNS SUMMARY — P18A

**NS (system resolver):** Beget set  
`ns1.beget.ru` `ns2.beget.pro` `ns1.beget.com` `ns1.beget.pro` `ns2.beget.com` `ns2.beget.ru`

| Name | Resolver | A |
|------|----------|---|
| shpigovsky.ru | 8.8.8.8 / 1.1.1.1 | `45.130.41.70` |
| shpigovsky.ru | local | `92.255.111.71` (legacy REG.RU website IP, cache/split) |
| www.shpigovsky.ru | 8.8.8.8 | `45.130.41.70` |
| shpigovsky.beget.tech | 8.8.8.8 | `91.106.207.76` |

MX @8.8.8.8: query returned no MX in this intake (treat as **verify mail zone** before any further NS/A experiments).

**Classification:** NS cutover **performed**. Public A **does not** yet point at the WordPress vhost (`91.106.207.76`). Public HTTPS serves **legacy** HTML.

Machine: `DNS-LOOKUPS.json`, `DNS-PUBLIC-RESOLVERS.json`.
