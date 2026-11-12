# Sıradaki sektör: veteriner klinikleri (kendi sitesi olanlar) (12 Kasım 2026)

Pilatesten sonra dört aday sektör, örnek sitelerin kendileri taranarak karşılaştırıldı (aynı yöntem).

| Sektör | Taranan | Sitede e-posta | Hazır online randevu | Değerlendirme |
|---|---|---|---|---|
| **Veteriner (kendi sitesi olan)** | 8 (2 açılmadı/eksik) | 7/8; çoğu kurumsal (info@, bilgi@) | 1/8 (Fresha) | **Seçildi** |
| Dövme stüdyoları | 4 | 3/4, ikisi gmail | 0 | Havuz küçük, e-postalar kişisel |
| Pet kuaför | 7 | 2/7, ikisi de gmail | Wix "book online" vb. var | Zayıf |
| Yoga stüdyoları | 7 (1 açılmadı) | 4/6 | Bir kısmı uygulama/ders programı sayfası kullanıyor | Orta; pilatesle aynı mesaj, ama gelir düşük |

İlk taramada (diş araştırması sırasında) küçük mahalle veterinerlerinin çoğunun sitesi/e-postası yoktu; bu yüzden hedef **kendi sitesi olan klinik ve hayvan hastaneleri**.

## Neden veteriner

- **Hazır demo:** `demo/randevu-veteriner` zaten var (aşı/kontrol hatırlatması, hayvan adı, hekim seçimi). Yeni demo gerekmiyor; yalnızca mail görselleri ve şablon.
- **Tekrarlayan ziyaret:** Yıllık aşı, iç/dış parazit, kontrol. "Aşı zamanı yaklaşıyor" SMS'i doğrudan gelir getiriyor; klinikler bunu çoğu zaman hiç yapmıyor ya da elle yapıyor.
- **Temiz siteler:** Örnekte 8 sitenin 7'sinde e-posta var, yalnızca 1'inde hazır randevu (Fresha).

## Örnek taramada temiz çıkanlar (tam liste ayrıca doğrulanacak)

| Klinik | Şehir | E-posta | Randevu yolu |
|---|---|---|---|
| İstanbulVet | İstanbul / Kadıköy (Koşuyolu) | info@istvetklinik.com | WhatsApp |
| Kadıköy Veteriner | İstanbul / Kadıköy | bilgi@kadikoyveteriner.net | Telefon |
| Anatolia Hayvan Hastanesi | İstanbul / Kadıköy | anatolia@anatoliapet.com | Talep formu + WhatsApp |
| Vetrium Hayvan Hastanesi | Ankara / Beytepe | info@ankaravetrium.com | WhatsApp |
| Vetes Veteriner | Ankara / Çankaya | hi@vetesveteriner.com | WhatsApp |
| Vetlinya | Ankara / Çankaya | iletisim@vetlinya.com | Telefon (site kısmen açıldı, tekrar kontrol) |

Elenen örnek: Vetrials (Fresha ile online randevu).

## Başlamadan önce gerekenler

1. Mevcut veteriner demosundan iki ekran görüntüsü (`assets/mail/veteriner-*.jpg`).
2. Onaylı formatın veteriner uyarlaması (`notlar/mail-sablonu-veteriner.html`); ana mesaj: "aşı zamanı gelen hastayı kaçırmayın".
3. Kendi sitesi olan 15–20 klinik/hayvan hastanesi, siteden doğrulanmış.
