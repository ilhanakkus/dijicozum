# dijicozum.com DNS yedeği (Cloudflare'e taşımadan önce, 6 Kasım 2026)

Nameserver: ns1/ns2/ns3.turkticaret.net

| Tür | Ad | Değer |
|---|---|---|
| A | @ | 216.198.79.1 (Vercel) |
| CNAME | www | 91dda51a3d2ea529.vercel-dns-017.com |
| MX | @ | 10 mx.turkticaret.net |
| TXT | @ | v=spf1 include:_spf.turkticaret.net ~all |
| TXT | mail._domainkey | v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCy6CIBbdOXTibfaiIOEPFVvJNTCjp1exXRWwH46CDePpnSD0npZrYCLHispVPdQYdCBBARRGTP8e80Lm3W28QDwIFof71ZczSDVNogDR559rS4Nh7SOeSmWnkeYq13mzVNVLSu8uhPLppjcOKYy5K231vjdROmWaP5tWrvDXc/HwIDAQAB |
| TXT | _dmarc | v=DMARC1; p=none; rua=mailto:merhaba@dijicozum.com |
| CNAME | mail | webmail.turkticaret.net |
| CNAME | autodiscover | autodiscover.turkticaret.net |

Geri dönmek gerekirse: Turkticaret'te nameserver'ları yukarıdakilere geri alın.
