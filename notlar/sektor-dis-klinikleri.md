# Sektör araştırması: özel diş poliklinikleri (12 Kasım 2026)

## Neden bu sektör

| Sektör | Sonuç | Neden |
|---|---|---|
| **Diş poliklinikleri** | **Seçildi** | Çoğunun kendi sitesi ve sitede açık yazan kurumsal e-postası var (info@...). Randevu telefon, WhatsApp ya da "talep formu" ile alınıyor; formda saat seçilse bile klinik arayıp onaylıyor, yani gerçek zamanlı takvim yok. Hazır demo ve mail görselleri var: `demo/randevu-dis`, `assets/mail/randevu-hasta.jpg`, `randevu-panel.jpg`. Kayıp randevu (boş koltuk) maliyeti yüksek, satış mesajı net. |
| Veteriner klinikleri | Elendi | Kadıköy'deki 49 kliniğin listesinden aranan örneklerin hiçbirinde kendi sitesi ya da e-postası bulunamadı; yalnızca telefon. E-posta kampanyasına uygun değil. |
| Güzellik merkezleri | Mevcut liste | `tools/build_leads.py`'de 25 aday var, 15'i e-postasız (B). |
| Fizik tedavi | Not | Siteler ve e-postalar var ama çoğu hastane birimi ya da zincir; ikinci sırada denenebilir. |

## Doğrulama yöntemi

Her klinik için **kendi sitesi** (ana sayfa + iletişim sayfası) indirildi ve otomatik olarak tarandı:
e-posta adresleri, `tel:` numaraları, WhatsApp bağlantıları, "randevu" butonlarının nereye gittiği ve hazır randevu yazılımı izleri (Doktor Takvimi, Calendly, Meddata vb.).
E-postalar sitede yazdığı gibidir; dizin sitelerinden alınan hiçbir bilgi listeye konmadı.

- **A:** Randevu yalnızca telefon / WhatsApp / e-posta / iletişim sayfası ile. En sıcak aday.
- **B:** Sitede bir "randevu talep formu" var ama klinik geri dönüp onaylıyor. Mesaj: "talep yerine müşteri boş saati kendisi seçsin, hatırlatma SMS'i gitsin".
- Kontrol notu olanlarda "online randevu" sayfası var; gerçek zamanlı takvim olup olmadığı otomatik taramayla kesinleşmedi, göndermeden önce sayfaya bir kez bakılmalı.

## A: telefon / WhatsApp ile randevu

| Klinik | Şehir / semt | E-posta (sitede) | Telefon (sitede) | Randevu yolu | Site |
|---|---|---|---|---|---|
| Mithatpaşa Dent | Ankara / Çankaya | info@mithatpasadent.com | 0312 431 10 19 · WA 0552 282 59 11 | İletişim sayfası, WhatsApp | mithatpasadent.com |
| Minedent | Ankara / Kavaklıdere | iletisim@minedent.net | 0312 419 57 25 | İletişim sayfası | minedent.net |
| Dentaplant | Ankara / Kavaklıdere | info@dentaplant.com.tr | 0312 419 91 00 | "E-mail ile randevu alın" | dentaplant.com.tr |
| MDC Diş | İstanbul / Kadıköy (Koşuyolu) | iletisim@mdcdent.com | 0216 546 06 92 | İletişim sayfası | mdcdent.com |
| ÖzbuDent | İstanbul / Üsküdar (Altunizade) | info@ozbudent.com | 0216 648 22 80 · WA 0541 673 22 80 | İletişim bölümü, WhatsApp | ozbudent.com |
| Yenitepe Diş | İstanbul / Kadıköy | yenitepedis@gmail.com | 0216 766 29 38 · 0533 156 33 68 | "Ön değerlendirme" formu | yenitepedis.com |
| Eyrice Diş | Bursa / Nilüfer | info@eyricedis.com | 444 1 496 · WA 0549 929 09 09 | WhatsApp, iletişim | eyricedis.com |

## B: randevu talep formu (klinik geri dönüyor)

| Klinik | Şehir / semt | E-posta (sitede) | Telefon (sitede) | Not | Site |
|---|---|---|---|---|---|
| DentRoyal | Ankara / Çankaya (GOP) | info@dentroyalclinic.com | 0312 467 01 42 · WA 0552 184 02 42 | Form: "talebiniz… arayarak onay" | dentroyalclinic.com |
| DentisLife | Ankara / Çankaya (GOP) | info@dentislife.com | 0312 417 70 60 · WA 0545 449 70 60 | Tarihli talep formu | dentislife.com |
| Dent Oran | Ankara / Çankaya (Oran) | info@dentoran.com | 0312 490 03 00 | İletişimde form | dentoran.com |
| Ersöz Diş | Ankara / Kızılay | info@ersozdis.com | 0312 419 69 69 · WA 0505 422 24 25 | Form sayfası | ersozdis.com |
| Arıdent | İstanbul / Maltepe | info@arident.com.tr | 0216 504 76 00 | /randevu formu | arident.com.tr |
| Dentsahil | İstanbul / Maltepe | iletisim@dentsahil.com | 0216 371 61 60 · WA 0553 777 24 45 | /randevu-al formu | dentsahil.com |
| DentAtaşehir | İstanbul / Ataşehir | info@dentatasehir.com | 0216 456 56 33 · 0533 486 55 41 | Randevu talebi formu | dentatasehir.com |
| İzmir Dental Klinik | İzmir / Bornova | bilgi@izmirdisklinik.com | 0232 502 42 84 · WA 0544 502 42 84 | Form, mesai içinde geri arama | izmirdentalklinik.com |
| Evrensel Diş | Ankara / Kavaklıdere (Tunalı) | info@evrenseldis.com.tr | 0312 466 19 95 | Kontrol: "online randevu" sayfası var | evrenseldis.com.tr |
| DentLeon | İzmir / Bornova, Alsancak | info@dentleon.com | WA 0501 344 35 36 | Kontrol: "online randevu" sayfası var | dentleon.com |
| OPC Klinik | İstanbul / Kozyatağı | info@opcklinik.com | WA 0501 357 70 70 | Kontrol: "randevu oluştur" sayfası; site uzun süredir güncellenmemiş olabilir | opcklinik.com |

## Elenenler

| Klinik | Neden |
|---|---|
| Özkaya Sağlık Grubu | Meddata ile gerçek online randevu sistemi var |
| NilA Diş (Bursa) | Doktor Takvimi kullanıyor |
| Dentoniks (Bursa) | Sitede e-posta yok (yalnızca WhatsApp) |
| Maltepedent, Dentamerkez (Ankara), Diş Doktorum (Ataşehir) | Sitede e-posta yok |
| Senfoni Diş (Ankara), EON Dental (Bursa) | Site açılmadı |
| Medicadent, Beyaz Işık, Sanita, Dent35, Avrupadent | Büyük zincir; çağrı merkezi / online randevu var |

## Sonraki adım

Diş kliniği maili için onaylı güzellik formatı (`mail-sablonu-guzellik.html`) aynı yapıyla diş görselleri ve `demo/randevu-dis?kn=` linkiyle uyarlanmalı; gönderimden önce her klinik için kullanıcı onayı alınmalı.
