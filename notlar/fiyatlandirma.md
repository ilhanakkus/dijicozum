# Fiyatlandırma: bir işletme ararsa ne diyeceğiz? (12 Kasım 2026)

## 1. Piyasa: rakiplerin kendi fiyat sayfaları (12 Kasım 2026'da kontrol edildi)

| Ürün | Kime | Fiyat (sayfada yazdığı gibi) | Vergi | Not |
|---|---|---|---|---|
| Doktor Takvimi (pro.doktortakvimi.com/fiyatlandirma) | Diş, fizyo, diyetisyen, psikolog | Starter **5.399 ₺/ay**, Plus 6.199 ₺/ay, VIP 7.499 ₺/ay | KDV hariç | Online takvim, SMS hatırlatma, profil sitesi. Şikâyetvar'da yıllık taahhüt ve cayma cezası şikâyetleri çok (bir kullanıcı ~11.000 ₺ + 40.000 ₺ ceza yazmış). |
| SalonRandevu (salonrandevu.com) | Kuaför, güzellik | Silver **779 ₺/ay** (3 kişi), Gold 1.590, Platinum 2.400, Full Diamond **3.480 ₺/ay** (10 kişi) | Dahil | Online randevu sitesi Diamond hariç +225 ₺/ay ek. Yıllıkta 1 ay bedava. |
| Fresha (fresha.com/tr/pricing) | Güzellik | Tek kişi **415 ₺/ay**, ekip **275 ₺/kişi/ay** | Hariç | 20 mesaj/kişi dahil, sonrası WhatsApp 1,30–2,40 ₺, pazarlama SMS 5,43 ₺/adet; Fresha pazar yerinden gelen yeni müşteriden komisyon. |
| KolayRandevu (kolayrandevu.com/randevu-programi) | Güzellik | "Tek Üyelik" **1.699 TL**, "12 aylık faturalandırılır" | Dahil | Sayfada ayın mı yılın mı fiyatı olduğu açık değil; diğer paketlerin (Başlangıç/Standart/Full) fiyatı sayfada yok. **Kesin değil.** |
| Piyzi (blog, Ekim 2026 fiyatları) | Güzellik | Pro 1.399 ₺/ay, Pro Plus 1.899, Mega 2.490 | – | Satıcının kendi yazısı. Genel "temel paket" bandını 700–1.200 ₺/ay veriyor. |

**Web sitesi yaptırma (diş kliniği, satıcı ve blog kaynakları, resmî liste yok):** hazır tema 2.000–15.000 ₺, özel tasarım 15.000–50.000 ₺, ajans 40.000 ₺+. Aylık bakım teklifleri 2.000–5.000 ₺. Bu aralık kaynaktan kaynağa çok değişiyor; kesin değil, yalnızca yön gösterir.

## 2. Bizim maliyetimiz

| Kalem | Maliyet | Kaynak |
|---|---|---|
| Barındırma (Cloudflare Pages) | 0 ₺ | Mevcut kurulum |
| SMS (Netgsm, vergiler dahil) | 1.000 SMS 370 ₺ (0,37 ₺/adet); 10.000 SMS 1.699 ₺ (0,17 ₺/adet); yeni aboneye 10.000 SMS 899 ₺ (0,09 ₺/adet) | netgsm.com.tr/fiyatlar/toplu-sms |
| Örnek SMS gideri | 300 randevu/ay × 2 hatırlatma = 600 SMS ≈ **100–220 ₺/ay** | Yukarıdan hesap |

SMS başlığı (gönderici adı) kaydı ve İYS yükümlülükleri ayrıca kontrol edilmeli; burada fiyatlanmadı.

## 3. Önerilen fiyatlar (KDV hariç)

| Paket | Kurulum (tek sefer) | Aylık | Dahil olanlar |
|---|---|---|---|
| **Güzellik / kuaför** | 4.900 ₺ | **990 ₺** | Salona özel online randevu sayfası, panel, 300 SMS/ay, en fazla 5 uzman |
| **Diş / fizyoterapi / klinik** | 7.900 ₺ | **1.990 ₺** | Kliniğe özel randevu sayfası, hekim/terapist takvimi, panel, 1.000 SMS/ay, sınırsız hekim |
| Ek SMS | – | 0,50 ₺/adet | Netgsm maliyetinin üstünde |
| Tek sayfalık web sitesi (isteğe bağlı) | 9.900 ₺ | – | Randevu sayfasıyla bağlı, alan adı bağlantısı dahil |
| Yıllık ödeme | – | 10 ay öde, 12 ay kullan | |

**Konumlama:**
- Klinik paketi Doktor Takvimi Starter'ın (5.399 ₺ + KDV) yaklaşık **üçte biri**; üstüne "taahhüt yok, cayma cezası yok, istediğiniz ay bırakın" denebilir. Doktor Takvimi şikâyetlerinin çoğu tam bu noktada.
- Güzellik paketi SalonRandevu Silver (779 ₺, vergi dahil) ile Gold (1.590 ₺) arasında; ama online randevu sayfası ve SMS bizde baştan dahil (onlarda Diamond'a kadar +225 ₺ ek).
- **İlk ay ücretsiz deneme**: kurulum ücreti ilk aydan sonra, sistem kullanılıyorsa alınır. Soğuk mailde "ücretsiz örnek" sözü verildiği için tutarlı.

**Pazarlık payı:** Kurulum ücretinden vazgeçilebilir (yıllık ödeme karşılığında). Aylık ücretin altına inilmemeli: klinikte 1.000 SMS'in maliyeti ~170–370 ₺, geri kalanı destek ve bakım.

## 4. Telefonda kısa cevap

> "İlk ay ücretsiz deniyorsunuz. Beğenirseniz kurulum bir kereye mahsus 7.900 lira, sonrası aylık 1.990 lira artı KDV; içinde ayda 1.000 SMS hatırlatma var. Taahhüt yok, istediğiniz ay bırakabilirsiniz."

(Güzellik için: 4.900 ₺ kurulum, 990 ₺/ay, 300 SMS.)

## Emin olmadığımız noktalar

- KolayRandevu'nun 1.699 TL'si aylık mı yıllık mı, sayfadan kesinleşmedi.
- Web sitesi fiyat aralıkları satıcı bloglarından; resmî ya da bağımsız bir liste bulunamadı.
- Netgsm'in "yeni abone" fiyatları kampanya; kalıcı maliyet için standart paket (0,17–0,37 ₺/adet) esas alındı.
- Önerilen fiyatlar bir öneridir; ilk 3–5 görüşmeden sonra gelen tepkiye göre gözden geçirilmeli.
