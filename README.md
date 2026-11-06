# DijiÇözüm (dijicozum.com)

Web sitesi, mobil uygulama, sipariş, randevu ve yapay zeka asistanı hizmetlerinin tanıtım sitesi ve canlı demoları.

Saf statik site: derleme adımı yok, bağımlılık yok. Cloudflare Pages'te olduğu gibi yayınlanır.

## Yapı

```
index.html            Ana sayfa (tools/build_pages.py ile üretilir)
randevu-sistemi.html, siparis-sistemi.html, web-sitesi.html, yapay-zeka-asistani.html   Hizmet sayfaları (aynı betikle üretilir)
gizlilik.html         Gizlilik ve KVKK aydınlatma metni (yayın öncesi doldurulacak)
404.html              Bulunamadı sayfası
demo/
  randevu.html        Kuaför/klinik randevu sistemi (müşteri + işletme paneli)
  siparis.html        QR menü ve sipariş (müşteri + mutfak ekranı)
  asistan.html        Yapay zeka asistanı (sohbet + bilgi tabanı + toplanan talepler)
  uygulama.html       Mobil uygulama (telefon çerçevesinde)
  kurumsal.html       Kurumsal web sitesi (masaüstü/tablet/telefon geçişli)
assets/
  config.js           Marka adı, e-posta, alan adı: tek yerden yönetilir
  style.css           Ana site stilleri
  demo.css / demo.js  Demo sayfalarındaki "DEMO" üst şeridi
_redirects, _headers  Cloudflare Pages: kısa bağlantılar, güvenlik ve önbellek başlıkları
vercel.json           Eski Vercel ayarları (geçiş bitince silinebilir)
tools/                Logo üretim betikleri (aşağıya bakın)
```

## Logo ve marka dosyaları

`assets/logo/` içinde, yazıları eğrilere çevrilmiş (yazı tipi gerektirmeyen) dosyalar:

| Dosya | Kullanım |
|---|---|
| `logo-a.svg` / `-dark` / `-mono` | **Ana logo** (ikon + yazı). Açık zemin / koyu zemin / siyah-beyaz |
| `logo-c.svg` / `-dark` / `-mono` | **İkincil logo** (yalnızca yazı: `dijiçözüm.`) |
| `icon.svg` | Tek başına simge |
| `png/` | Şeffaf PNG'ler ve beyaz zeminli siyah-beyaz sürümler (marka başvurusu için) |
| `../og-image.png` | Sosyal medya paylaşım görseli (1200×630) |

Renkler: turuncu `#e8590c`, lacivert `#0f172a`. Yazı tipi: Plus Jakarta Sans ExtraBold (SIL Open Font License).

Yeniden üretmek için (yazı tipi dosyası gerekir):

```bash
python3 -m venv .venv && .venv/bin/pip install fonttools
.venv/bin/python tools/build_logos.py PlusJakartaSans-ExtraBold.ttf
bash tools/export_pngs.sh PlusJakartaSans-ExtraBold.ttf
```

Her demo kendi içinde tamamdır; demo verileri yalnızca ziyaretçinin tarayıcısında (localStorage) tutulur, sunucuya bir şey gönderilmez.

## Sayfaları düzenleme

Ana sayfa ve dört hizmet sayfası `tools/build_pages.py` ile üretilir. Metni, SSS'yi veya menüyü değiştirmek için o dosyayı düzenleyip çalıştırın (menü, alt bilgi, SEO etiketleri, JSON-LD ve `sitemap.xml` otomatik güncellenir):

```bash
python3 tools/build_pages.py
```

## Ziyaret istatistikleri (Google Analytics 4)

Ölçüm kimliği `assets/consent.js` içinde (`GA_ID`). KVKK gereği etiket **yalnızca ziyaretçi "Kabul et" derse** yüklenir. Reddedenler için hiçbir çerez yerleştirilmez, Google'a istek gitmez. Kararı sayfa altındaki "Çerez tercihleri" bağlantısıyla değiştirilebilir.

Gönderilen özel olaylar: `generate_lead` (form gönderimi, sadece seçilen hizmetler), `demo_open`, `cta_click`, `email_click`. Ad, telefon ve e-posta hiçbir olayda gönderilmez.

## Yerelde çalıştırma

```bash
python3 -m http.server 4173
# http://localhost:4173
```

## Yayınlama (GitHub → Cloudflare Pages → dijicozum.com)

1. **GitHub:** değişiklikleri `main` dalına gönderin (`git push`).
2. **Cloudflare Pages:** dash.cloudflare.com → Workers & Pages → Create → Pages → Connect to Git → bu repoyu seçin. Framework preset: **None**, Build command boş, Build output directory: `/`. Save and Deploy.
3. **Analiz:** Pages projesi → Metrics → Web Analytics → Enable. Cloudflare, çerezsiz sayım betiğini sayfalara kendisi ekler; kodda bir şey yapmaya gerek yok.
4. **Alan adı:** Pages projesi → Custom domains → `dijicozum.com` ve `www.dijicozum.com` ekleyin. En kolayı alan adının DNS'ini Cloudflare'e taşımak: Cloudflare'e site olarak ekleyin, verdiği iki nameserver'ı Turkticaret → alan adı yönetimi → nameserver ayarına yazın. **Taşımadan önce** `merhaba@dijicozum.com` için MX, SPF (TXT) ve DKIM (`mail._domainkey`) kayıtlarının Cloudflare DNS'e aktarıldığını kontrol edin, yoksa e-posta durur.
5. `www` → `dijicozum.com` yönlendirmesi için Cloudflare → Rules → Redirect Rules ile 301 kuralı ekleyin.
6. Bundan sonra `main` dalına yapılan her `git push` otomatik yayına alınır. Diğer dallar için önizleme adresi üretilir.

Cloudflare'e özgü ayar dosyaları: `_redirects` (`/r/...` kampanya kısa bağlantıları) ve `_headers` (güvenlik ve önbellek başlıkları). `.html` uzantısız temiz adresler Cloudflare Pages'te varsayılan olarak çalışır. `vercel.json` Vercel'den tamamen çıkılana kadar duruyor; Cloudflare onu yok sayar.

## Yayın öncesi kontrol listesi

- [ ] `merhaba@dijicozum.com` gerçekten çalışıyor mu? (Turkticaret e-posta paketi, Zoho Mail veya Google Workspace ile açın. Adres `assets/config.js` içinde.)
- [ ] Şirket kurulunca `gizlilik.html` 1. maddesine ticari unvan, vergi numarası ve adres eklendi; metin hukuk danışmanınca kontrol edildi.
- [ ] Marka başvurusu (TÜRKPATENT, sınıf 35 ve 42): logolu başvuru önerilir; `assets/logo/png/*-mono-beyaz-zemin.png` dosyaları hazır.
- [ ] Hukuki yapı (şahıs/limited) netleşti; fatura ve unvan bilgisi siteye eklendi.
- [ ] İletişim formu şu an kullanıcının e-posta uygulamasını açar (`mailto`). Gerçek form için Formspree/Resend gibi bir servis bağlanabilir.
- [ ] Google Search Console'a `dijicozum.com` eklenip `sitemap.xml` gönderildi.
- [ ] Fiyat/paket bilgisi eklenecekse ana sayfaya bölüm eklenmeli (şu an "teklif ile" yaklaşımı).
