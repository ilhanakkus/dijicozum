# Tanıtım maili: onaylı format ve gönderim yöntemi

**Onaylı format (12 Kasım 2026):** [mail-sablonu-guzellik.html](mail-sablonu-guzellik.html)
Demo olarak ilhanakkus@gmail.com'a gönderildi ve beğenildi. Bu formatı değiştirmeden kullanın.

- Konu: `{{SALON}} için küçük bir fikir: randevular kendiliğinden gelsin`
- Gönderen: `merhaba@dijicozum.com` (Gmail'de "Kimden" olarak tanımlı)
- İçerik: samimi giriş → 2 ekran görüntüsü (müşteri ekranı, salon paneli) → SMS hatırlatma → turuncu "örneği deneyin" düğmesi → ücretsiz özel örnek teklifi → imza → "çıkar" satırı
- Görseller: `https://dijicozum.com/assets/mail/guzellik-hasta.jpg` ve `guzellik-panel.jpg` (maile gömülü değil, siteden yüklenir; site yayında olmalı)
- Demo linki: `https://dijicozum.com/demo/randevu-guzellik?kn={{SALON_URL}}&utm_source=eposta&utm_medium=soguk3&utm_campaign=guzellik` (demo başlığında salonun adı görünür)

**Diş klinikleri uyarlaması:** [mail-sablonu-dis.html](mail-sablonu-dis.html). Yapı aynı; görseller `randevu-hasta.jpg` / `randevu-panel.jpg` (diş demosu), link `demo/randevu-dis?kn=...&utm_campaign=dis-klinikleri`, konu `{{KLINIK}} için küçük bir fikir: boş kalan koltuklar azalsın`. Aday listesi: [sektor-dis-klinikleri.md](sektor-dis-klinikleri.md). A ve B grubu için gözlem cümlesi şablonun başında yazıyor.

## Doldururken

- `{{SALON}}` = salon adı, `{{SALON_URL}}` = URL kodlanmış hali (boşluk `%20`).
- Türkçe eki her salon için elle kontrol edin: "Talin Güzellik Merkezi'nin", ama "Mabel Güzellik'in".
- Aday listesi: `tools/build_leads.py` (A önceliği: e-postası var, online randevusu yok).

## Nasıl gönderilir

- **Gmail web arayüzünden (Chrome)** gönderin: yeni ileti → Kimden `merhaba@dijicozum.com` → HTML gövdeyi yapıştırın. Görseller ve düğme korunur.
- Gmail API/bağlayıcı aracıyla göndermeyin: `<img>` etiketlerini ve düğme arka planını siler.
- Turkticaret webmail'den de HTML olarak gönderilebilir (30 Ekim diş maili böyle gitti).

## Gönderim kaydı

| Tarih | Alıcı | Not |
|---|---|---|
| 28 Eyl 2026 | Filiz Karslıoğlu Cilt Atölyesi | Eski, görselsiz metin. Yanıt yok. |
| 12 Kas 2026 | ilhanakkus@gmail.com | Onaylı formatın demosu. |
| 12 Kas 2026 | ilhanakkus@gmail.com | Diş şablonunun demosu (Mithatpaşa Dent örneğiyle, A grubu cümlesi). |

### Diş klinikleri kampanyası: 12 Kasım 2026, 10:47–10:51 (TSİ)

Gönderen: `merhaba@dijicozum.com` (Gmail web). Konu: `{Klinik} için küçük bir fikir: boş kalan koltuklar azalsın`. 18 mail, her biri tek alıcılı; gönderilmiş klasöründe doğrulandı.

| # | Klinik | Alıcı | Grup | Yanıt |
|---|---|---|---|---|
| 1 | Mithatpaşa Dent | info@mithatpasadent.com | A | – |
| 2 | Minedent | iletisim@minedent.net | A | – |
| 3 | Dentaplant | info@dentaplant.com.tr | A | – |
| 4 | MDC Diş | iletisim@mdcdent.com | A | – |
| 5 | ÖzbuDent | info@ozbudent.com | A | – |
| 6 | Yenitepe Diş | yenitepedis@gmail.com | A | – |
| 7 | Eyrice Diş | info@eyricedis.com | A | – |
| 8 | DentRoyal | info@dentroyalclinic.com | B | – |
| 9 | DentisLife | info@dentislife.com | B | – |
| 10 | Dent Oran | info@dentoran.com | B | – |
| 11 | Ersöz Diş | info@ersozdis.com | B | – |
| 12 | Arıdent | info@arident.com.tr | B | – |
| 13 | Dentsahil | iletisim@dentsahil.com | B | – |
| 14 | DentAtaşehir | info@dentatasehir.com | B | – |
| 15 | İzmir Dental Klinik | bilgi@izmirdisklinik.com | B | – |
| 16 | Evrensel Diş | info@evrenseldis.com.tr | B | – |
| 17 | DentLeon | info@dentleon.com | B | – |
| 18 | OPC Klinik | info@opcklinik.com | B | – |

Yanıt takibi: Gmail'de `to:merhaba@dijicozum.com` + bu alan adlarından gelen mailler ve "boş kalan koltuklar" konulu yanıtlar; ayrıca geri dönen (bounce) mailler.

Fizyoterapi şablonunun demosu: 12 Kas 2026, ilhanakkus@gmail.com (Ataşehir Fizik Tedavi örneğiyle, A grubu cümlesi).

Pilates şablonunun demosu: 12 Kas 2026, ilhanakkus@gmail.com (Zeo Pilates örneğiyle, A grubu cümlesi).

Veteriner şablonunun demosu: 12 Kas 2026, ilhanakkus@gmail.com (İstanbulVet örneğiyle, A grubu cümlesi).

Lazer şablonunun demosu: 12 Kas 2026, ilhanakkus@gmail.com (Ata Estetik örneğiyle, A grubu cümlesi).

### Güzellik merkezleri kampanyası: 12 Kasım 2026, 11:03–11:06 (TSİ)

Gönderen: `merhaba@dijicozum.com` (Gmail web). Konu: `{Salon} için küçük bir fikir: randevular kendiliğinden gelsin`. Onaylı güzellik şablonu; B grubunda açılış cümlesi "randevu taleplerini formla alıp sonra arayarak onayladığınızı gördüm." 14 mail, her biri tek alıcılı; gönderilmiş klasöründe doğrulandı. Liste: [sektor-guzellik-merkezleri.md](sektor-guzellik-merkezleri.md).

| # | Salon | Alıcı | Grup | Yanıt |
|---|---|---|---|---|
| 1 | New You Güzellik Merkezi | newyou.guzellik@gmail.com | A | – |
| 2 | Talin Güzellik Merkezi | info@talinguzellikmerkezi.com | A | – |
| 3 | Kadıköy Güzellik Merkezi | info@kadikoyguzellikmerkezi.com | A | – |
| 4 | Mabel Güzellik | randevu@mabelguzelliksalonu.com | A | – |
| 5 | Dermopark VIP | info@dermoparkvip.com | A | – |
| 6 | Dore Güzellik | info@doreguzellikeskisehir.com | A | – |
| 7 | Este Lórien | info@estelorien.com.tr | A | – |
| 8 | Mediplast Güzellik Merkezi | info@mediplast.com.tr | A | – |
| 9 | Derma Lazer | info@dermalazer.com | A | – |
| 10 | Başakşehir Beauty | info@basaksehirbeauty.com | A | – |
| 11 | Tülay Kalmaz Beauty Center | kalmaztulay@gmail.com | A | – |
| 12 | Sevil Muradova Güzellik Merkezi | info@sevilmuradova.com | B | – |
| 13 | Lima Estetik | info@limaestetik.com | B | – |
| 14 | Evolusi Güzellik | info@evolusiguzellik.com | B | – |

### Fizyoterapi merkezleri kampanyası: 12 Kasım 2026, 12:22–12:24 (TSİ)

Gönderen: `merhaba@dijicozum.com` (Gmail web). Konu: `{Merkez} için küçük bir fikir: yarıda kalan seanslar azalsın`. Şablon: [mail-sablonu-fizyo.html](mail-sablonu-fizyo.html). 16 mail, her biri tek alıcılı; gönderilmiş klasöründe doğrulandı. Liste: [sektor-fizyoterapi.md](sektor-fizyoterapi.md).

| # | Merkez | Alıcı | Grup | Yanıt |
|---|---|---|---|---|
| 1 | Ataşehir Fizik Tedavi | info@atasehirfiziktedavi.com | A | – |
| 2 | M Terapi | mterapi@outlook.com | A | – |
| 3 | Ulus Fizyoterapi | info@ulusfizyoterapi.com | A | – |
| 4 | Fizyonef | info@nefizyoterapi.com | A | – |
| 5 | Diafiz | info@diafiz.com | A | – |
| 6 | Borfiz | bilgi@borfiz.com.tr | A | – |
| 7 | Nilüfer Fizyoterapi | info@niluferfizyoterapi.com | A | – |
| 8 | Fizyovela | info@fizyovela.com | A | 12 Kas: Geri döndü (adres yok). Sitede ayrıca fizyovela@gmail.com yazıyor. |
| 9 | FizyoSuite | bilgi@fizyosuite.com | A | – |
| 10 | Maltepe Fizik Tedavi | maltepefiziktedavi06@gmail.com | A | – |
| 11 | Enerji Tıp Merkezi | bilgi@enerjitipmerkezi.com | A | – |
| 12 | Fzt. Fatma Aslan | info@fizyoterapistfatmaaslan.com | A | – |
| 13 | Atafiz | info@atafiz.com | B | – |
| 14 | Akdeniz Deva | info@akdenizdeva.com | B | – |
| 15 | FizyoNatural | fizyonatural@gmail.com | B | – |
| 16 | Yusuf Onkol Fizik Tedavi | info@yusufonkol.com | B | – |

### Pilates stüdyoları kampanyası: 12 Kasım 2026, 13:05–13:09 (TSİ)

Gönderen: `merhaba@dijicozum.com` (Gmail web). Konu: `{Stüdyo} için küçük bir fikir: ders programı WhatsApp'tan çıksın`. Şablon: [mail-sablonu-pilates.html](mail-sablonu-pilates.html). B grubunda açılış cümlesi "rezervasyonları telefon, WhatsApp ya da form üzerinden aldığınızı gördüm." 19 mail, her biri tek alıcılı; gönderilmiş klasöründe doğrulandı. Liste: [sektor-pilates.md](sektor-pilates.md).

| # | Stüdyo | Alıcı | Grup | Yanıt |
|---|---|---|---|---|
| 1 | Terapilates | info@terapilates.com.tr | A | – |
| 2 | Zeo Pilates | info@zeopilates.com | A | – |
| 3 | Naura Pilates Studio | info@naurapilates.com.tr | A | – |
| 4 | RiseUp Pilates | iletisim@riseuppilates.com | A | 12 Kas: Geri döndü (adres yok; e-posta alan adı sitenin riseup-pilates.com adresinden farklı) |
| 5 | Burcu Yanardağ Pilates | yanardag.burcu@hotmail.com | A | – |
| 6 | Gen Pilates | bilgi@genpilates.com | A | – |
| 7 | Plus Pilates | info@pluspilatespt.com | A | – |
| 8 | Beşiktaş Stüdyo | bilgi@besiktasstudyo.com.tr | A | – |
| 9 | The Cove Pilates | info@thecovepilates.com | A | – |
| 10 | Slimlife Studio | info@slimlifestudio.com.tr | A | – |
| 11 | Joya Studio | info@joyastudio.net | A | – |
| 12 | Aqua Pilates | info@aquapilates.com.tr | A | – |
| 13 | Ankara Pilates | info@ankarapilates.net | A | – |
| 14 | Fizyofiplus | info@fizyofiplus.com | B | – |
| 15 | Reformer İstanbul | bilgi@reformeristanbul.com | B | – |
| 16 | Sun Reformer Pilates | sunreformerpilates@gmail.com | B | – |
| 17 | Pera Pilates | perapilates@gmail.com | B | – |
| 18 | Studio Love Pilates | info@studiolovepilates.com | B | – |
| 19 | PiaForm | piaform@hotmail.com | B | – |

### Veteriner klinikleri kampanyası: 12 Kasım 2026, 13:37–13:41 (TSİ)

Gönderen: `merhaba@dijicozum.com` (Gmail web). Konu: `{Klinik} için küçük bir fikir: aşı zamanı gelen hastalar kaçmasın`. Şablon: [mail-sablonu-veteriner.html](mail-sablonu-veteriner.html). B grubunda açılış cümlesi "randevuları telefon, WhatsApp ya da form üzerinden aldığınızı gördüm." 17 mail, her biri tek alıcılı; gönderilmiş klasöründe doğrulandı. Liste: [sektor-veteriner.md](sektor-veteriner.md).

| # | Klinik | Alıcı | Grup | Yanıt |
|---|---|---|---|---|
| 1 | Ataşehir Veteriner Kliniği | info@atasehirveteriner.com | A | – |
| 2 | Vet34 | iletisim@vet34.com | A | – |
| 3 | Leylek Vet | info@leylekvet.com | A | – |
| 4 | Papyon Veteriner | papyonveteriner@gmail.com | A | – |
| 5 | Vetasgon Kartal Veteriner | info@vetasgonkartalveteriner.com | A | – |
| 6 | Anemon Veteriner Kliniği | info@anemonveteriner.com | A | – |
| 7 | Heka Veteriner Kliniği | hekavet@gmail.com | A | – |
| 8 | İstanbulVet | info@istvetklinik.com | A | – |
| 9 | Kadıköy Veteriner | bilgi@kadikoyveteriner.net | A | – |
| 10 | Apex Veteriner Kliniği | info@apexvet.com.tr | A | – |
| 11 | Ortivet | info@ortivet.com | A | – |
| 12 | Borvet | info@borvet.com | A | – |
| 13 | Rönesans Veteriner | ronesansvet35@gmail.com | A | – |
| 14 | Vetes Veteriner | hi@vetesveteriner.com | A | – |
| 15 | Vetrium Hayvan Hastanesi | info@ankaravetrium.com | A | – |
| 16 | Anatolia Hayvan Hastanesi | anatolia@anatoliapet.com | B | – |
| 17 | Vega Veteriner Kliniği | bilgi@vegaveterinerklinigi.com | B | – |

### Lazer epilasyon ve medikal estetik kampanyası: 12 Kasım 2026, 13:53–13:56 (TSİ)

Gönderen: `merhaba@dijicozum.com` (Gmail web). Konu: `{Merkez} için küçük bir fikir: seans paketleri yarıda kalmasın`. Şablon: [mail-sablonu-lazer.html](mail-sablonu-lazer.html). B grubunda açılış cümlesi "randevuları telefon, WhatsApp ya da form üzerinden aldığınızı gördüm." 11 mail, her biri tek alıcılı; gönderilmiş klasöründe doğrulandı. Liste: [sektor-lazer.md](sektor-lazer.md).

| # | Merkez | Alıcı | Grup | Yanıt |
|---|---|---|---|---|
| 1 | Ata Estetik | info@ataestetik.com | A | – |
| 2 | Ankara Lazer | ankaralazer@gmail.com | A | – |
| 3 | Laserlab | iletisim@laserlab.tr | A | – |
| 4 | Million Hair Clinic | info@millionhairclinic.com | A | – |
| 5 | Clinika Estetik | info@clinikaestetik.com | A | – |
| 6 | Bakırköy Lazer | info@bakirkoylazer.com | A | – |
| 7 | MediDerm | info@mediderm.com.tr | A | – |
| 8 | Novar Poliklinik | info@novarpoliklinik.com | A | – |
| 9 | Dr. Beauty Laser | info@drbeautylaser.com | A | – |
| 10 | Aslı Eralp Lazer ve Güzellik | doktoraslieralp@gmail.com | B | – |
| 11 | Kent Güzellik Merkezi | kentguzellikbursa@hotmail.com | B | – |
