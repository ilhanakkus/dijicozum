# WhatsApp mesaj şablonu (kısa, samimi; onay bekliyor)

```
Merhaba, kolay gelsin 🙂 Ben İlhan.
{İşletme} için küçük bir online randevu sayfası hazırladım, bir bakar mısınız?
https://dijicozum.com/demo/randevu-{demo}?kn={İşletme_URL}&utm_source=whatsapp
Hoşunuza giderse sizin için ücretsiz kurarım.
```

## A/B deneyi: 1. tur (26.11.2026, 14:34–14:47)

Gönderen: 0545 157 93 11 (WhatsApp Business Web). Kuyruğun ilk 20 işletmesi sırayla A/B'ye bölündü.

- **A (link ile):** "Merhaba, kolay gelsin 🙂 Ben İlhan. {İşletme} için küçük bir online randevu sayfası hazırladım, bir bakar mısınız? {demo linki, utm_content=A} Hoşunuza giderse sizin için ücretsiz kurarım."
- **B (soru, link yok):** "Merhaba, kolay gelsin 🙂 Randevuları hâlâ WhatsApp'tan mı alıyorsunuz? Sizin için küçük bir online randevu sayfası hazırladım, incelemek ister misiniz?"
  - İlk 2 B mesajı (Tülay Kalmaz, Mithatpaşa Dent) eski sonla gitti: "göstereyim mi?". Kullanıcı ardından metni "incelemek ister misiniz?" olarak değiştirdi.

| İşletme | Numara | Grup | Durum (26.11 14:50) |
|---|---|---|---|
| New You Güzellik Merkezi | 0533 502 38 37 | A | gönderildi |
| Tülay Kalmaz Beauty Center | 0530 425 87 82 | B | gönderildi (eski son) |
| Ankara Lazer | 0506 484 89 34 | A | gönderildi |
| Mithatpaşa Dent | 0552 282 59 11 | B | gönderildi (eski son) |
| ÖzbuDent | 0541 673 22 80 | A | gönderildi |
| Eyrice Diş | 0505 771 14 96 | B | gönderildi; otomatik karşılama |
| DentRoyal | 0552 184 02 42 | A | iletilmedi (Meta API'li işletme hesabı, mesaj sohbette görünmüyor) |
| DentisLife | 0545 449 70 60 | B | gönderildi; otomatik karşılama |
| Dentsahil | 0553 777 24 45 | A | gönderildi |
| DentAtaşehir | 0533 486 55 41 | B | gönderildi; yanıt: "Teşekkürler" |
| İzmir Dental Klinik | 0544 502 42 84 | A | gönderildi |
| Evrensel Diş | 0530 660 48 86 | B | gönderildi |
| DentLeon | 0501 344 35 36 | A | gönderildi |
| OPC Klinik | 0501 357 70 70 | B | gönderildi |
| Talin Güzellik Merkezi | 0543 520 00 77 | A | gönderildi; otomatik karşılama |
| Mabel Güzellik | 0507 829 40 40 | B | gönderildi; otomatik karşılama |
| Dermopark VIP | 0552 397 56 53 | A | numara WhatsApp kullanmıyor |
| Dore Güzellik | 0545 425 53 98 | B | gönderildi |
| Mediplast Güzellik Merkezi | 0552 650 60 00 | A | gönderildi |
| Başakşehir Beauty | 0541 547 14 46 | B | gönderildi |

İletilen: 18 mesaj (A 8, B 10). Sonuçlar 28.11.2026'da değerlendirilecek; ölçüt, otomatik olmayan yanıtlar ve A linkine gelen tıklamalar.

## A/B deneyi: 2. tur (26.11.2026, 14:49–14:58)

Kuyruğun 21–34. satırları gönderildi (14 mesaj, A 7 / B 7): Sevil Muradova (A), Lima Estetik (B), Evolusi (A), Ata Estetik (B, otomatik karşılama), Clinika Estetik (A), MediDerm (B), Dr. Beauty Laser (A), M Terapi (B), Maltepe Fizik Tedavi (A), Burcu Yanardağ Pilates (B), PiaForm (A), İyi Duy İşitme (B), Başkent Ses İşitme (A), Diyalog İşitme (B, otomatik karşılama). Başakşehir Beauty (1. tur) otomatik karşılama gönderdi.
15:00–15:02'de kalan 6 işletmeye de gönderildi: Kalamış Psikoloji (A), Özne Psikoloji (B), İzmir Şans Psikoloji (A), Yenitepe Diş (B), Ataşehir Fizik Tedavi (A, otomatik karşılama), Ulus Fizyoterapi (B). Kuyruğun ilk 40 satırı bitti. Toplam 38 mesaj iletildi (A 18, B 20).

**İlk olumlu yanıt:** İyi Duy İşitme (B grubu) 14:57'de "olur" yazdı. 14:59'da demo linki gönderildi: randevu-isitme, kn=İyi Duy İşitme, utm_content=B.

## Tıklama takibi

`functions/demo/_middleware.js` (Cloudflare Pages Function) utm_source taşıyan her demo açılışını ntfy.sh/dijicozum-1d976faaf181 konusuna bildirir. Bildirimde işletme adı, demo, cihaz ve kaynak yer alır. Bu sayım çerez onayından bağımsızdır; önizleme botları (WhatsApp, Facebook vb.) sayılmaz.
- Telefonda anlık bildirim: ntfy uygulamasında bu konuya abone olun.
- Geçmiş: `curl -s "https://ntfy.sh/dijicozum-1d976faaf181/json?poll=1&since=12h"`. ntfy kayıtları 12 saat tutar.
- 14:56'daki PiaForm bildirimi, bot filtresinden önce WhatsApp önizlemesinden geldi; tıklama sayılmaz.

## 3. tur (26.11.2026, 15:10–15:30)

Kuyruğun 41–54. satırları: 13 mesaj iletildi (A 7 / B 6). İletilenler: Fizyonef (A), Enerji Tıp Merkezi (B), Fzt. Fatma Aslan (A), Akdeniz Deva (B), Yusuf Onkol Fizik Tedavi (A), Terapilates (B), Zeo Pilates (A), Naura Pilates (B), Gen Pilates (A), Plus Pilates (B), Beşiktaş Stüdyo (A), Aqua Pilates (B), Ankara Pilates (A).
- Aslı Eralp Lazer ve Güzellik: numara WhatsApp kullanmıyor.
- Duyses İşitme gönderilirken WhatsApp Web oturumu kapandı ve QR istedi. Gönderim durduruldu.
- Bekleyen 6 işletme: Duyses İşitme, Sesplus İşitme, Antalya İşitme Cihazları Merkezi, Uzman İşitme Merkezi, Teta Ses, Neva İşitme.

Günün toplamı: 51 mesaj iletildi (A 25, B 26).

## 26.11.2026 akşam: WhatsApp kısıtlaması

Kullanıcının bildirdiğine göre WhatsApp numarayı kısıtladı. Toplu gönderim durduruldu; kısıtlama kalkana kadar yeni soğuk mesaj gönderilmeyecek.

**Olumlu yanıt:** Akdeniz Deva Fizyoterapi (Antalya, 0552 750 71 71, B grubu) "olabilir" yazdı. Yanıtı kullanıcı kendisi gönderecek; demo linki: randevu-fizyoterapi, kn=Akdeniz Deva, utm_content=B.

## 27.11.2026: 4. tur (yavaş tempo, kısıtlama sonrası)

Kullanıcı numarayı yeniden bağladı. Güvenli tempo: günde en fazla 8 mesaj, yalnızca B metni (linksiz), mesajlar arası yaklaşık 90 sn, her gönderimde kısıtlama uyarısı kontrolü.
İletilenler (8, hepsi B): Sesplus İşitme, Antalya İşitme Cihazları Merkezi, Uzman İşitme Merkezi, Teta Ses, Neva İşitme, Ataşehir Psikoloji, Renas Psikoloji, Kilya Psikoloji (otomatik yanıt geldi).
- Duyses İşitme: 26.11'deki mesaj aslında iletilmiş (otomatik yanıt geldi), tekrar gönderilmedi.
- Uyarı ya da kısıtlama görülmedi.
- Sıradaki: kuyruk #64'ten devam.
