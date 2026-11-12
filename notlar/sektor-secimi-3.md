# Sıradaki sektör: fizik tedavi / fizyoterapi merkezleri (12 Kasım 2026)

Diş ve güzellikten sonra üç aday sektör, örnek sitelerin kendileri taranarak karşılaştırıldı (e-posta, randevu yöntemi, hazır randevu yazılımı izi). Yöntem diş listesindekiyle aynı.

| Sektör | Taranan site | Sitede e-posta | Hazır online randevu (Doktor Takvimi vb.) | Değerlendirme |
|---|---|---|---|---|
| **Fizyoterapi / fizik tedavi** | 9 | 9/9, çoğu kurumsal (info@, bilgi@) | 2 Doktor Takvimi, 3 "online randevu" sayfası | **Seçildi** |
| Diyetisyen | 7 (1 açılmadı) | 6/6 ama 3'ü gmail | 3/6 Doktor Takvimi | Tek kişilik muayenehaneler, bütçe düşük, çoğu zaten platformda |
| Psikolog / psikolojik danışmanlık | 6 (1 açılmadı) | 4/5 | belirgin değil | Randevu WhatsApp/telefonla; ama sağlık verisi hassas (KVKK özel nitelikli veri), mesaj tonu riskli, sonraya bırakıldı |

## Neden fizyoterapi

- **Tekrarlayan randevu:** Bir hasta genelde 10–20 seanslık bir kür alır. Her seans bir randevu; unutulan seans hem gelir kaybı hem tedavi aksaması. Otomatik SMS hatırlatma burada en çok değer üretiyor.
- **Kurumsal siteler ve e-postalar:** Taranan 9 merkezin hepsinde sitede e-posta var.
- **Bütçe:** Merkezler (birden çok fizyoterapist, cihaz, SGK anlaşması) tek kişilik muayenehanelerden daha büyük; aylık ücret ödeme gücü daha yüksek.
- **Boşluk:** Merkezlerin yaklaşık yarısında hâlâ gerçek bir randevu sistemi yok (telefon, WhatsApp, iletişim formu).

## Örnek taramada temiz çıkanlar (tam liste ayrıca doğrulanacak)

| Merkez | Şehir | E-posta | Randevu yolu |
|---|---|---|---|
| Fzt. Fatma Aslan | Ankara / Çankaya | info@fizyoterapistfatmaaslan.com | WhatsApp, iletişim sayfası |
| Enerji Tıp Merkezi | Ankara / Balgat | bilgi@enerjitipmerkezi.com | WhatsApp, telefon |
| Atafiz Tıp Merkezi | İstanbul / Ataşehir | info@atafiz.com | WhatsApp, /randevu sayfası (kontrol edilecek) |
| Fizyonef (Nefizyoterapi) | İstanbul / Bakırköy | info@nefizyoterapi.com | WhatsApp, iletişim |

Elenen örnekler: Fzt. Emre Can Kara ve Merve Sinem Çelik (Doktor Takvimi), Fizitek, Dr. Fizyo, Fiziktedavim (online randevu sayfası var; gerçek takvim olup olmadığı ayrıca bakılmalı).

## Başlamadan önce gerekenler

1. **Fizyoterapi demosu:** `demo/randevu-fizyoterapi` (seans paketi, terapist seçimi, kalan seans sayısı, her seans öncesi SMS). Şu an yok.
2. **Mail görselleri:** demodan iki ekran görüntüsü (`assets/mail/fizyo-*.jpg`).
3. **Şablon:** onaylı formatın fizyoterapi uyarlaması (`notlar/mail-sablonu-fizyo.html`).
4. **Aday listesi:** 15–20 merkez, İstanbul/Ankara/İzmir, siteden doğrulanmış.
