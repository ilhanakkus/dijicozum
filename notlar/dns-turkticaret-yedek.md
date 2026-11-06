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

## Geçiş durumu (6 Kasım 2026)

- Nameserver'lar Cloudflare'e geçti: aron.ns.cloudflare.com, damiete.ns.cloudflare.com.
- dijicozum.com ve www.dijicozum.com, Cloudflare Pages projesi `dijicozum`'a bağlı (CNAME → dijicozum.pages.dev, proxied).
- www → dijicozum.com yönlendirmesi: Cloudflare Redirect Rule, 301, sorgu dizesi korunuyor.
- E-posta kayıtları (MX, SPF, DKIM, DMARC, mail/autodiscover/autoconfig) Turkticaret'e işaret ediyor, "DNS only".
- Cloudflare Web Analytics açık (Pages → Metrics).
- Vercel artık kullanılmıyor; geçiş öncesinde Vercel hesabı "DEPLOYMENT_DISABLED / Payment required" veriyordu.
