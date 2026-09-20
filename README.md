# DijiÇözüm (dijicozum.com)

Web sitesi, mobil uygulama, sipariş, randevu ve yapay zeka asistanı hizmetlerinin tanıtım sitesi ve canlı demoları.

Saf statik site: derleme adımı yok, bağımlılık yok. Vercel'de olduğu gibi yayınlanır.

## Yapı

```
index.html            Ana sayfa
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
vercel.json           Temiz URL'ler ve güvenlik başlıkları
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

## Yerelde çalıştırma

```bash
python3 -m http.server 4173
# http://localhost:4173
```

## Yayınlama (GitHub → Vercel → dijicozum.com)

1. **GitHub:** repoyu oluşturup `main` dalına gönderin (`git push`).
2. **Vercel:** vercel.com → Add New → Project → GitHub reposunu seçin. Framework: **Other**, Build Command ve Output Directory boş kalsın. Deploy.
3. **Alan adı:** Vercel → Project → Settings → Domains → `dijicozum.com` ve `www.dijicozum.com` ekleyin. Vercel size DNS kayıtlarını gösterir.
4. **DNS (Turkticaret → DNS yönetimi):** mevcut park sayfası kayıtlarını (`A 31.186.11.254` ve www için `CNAME dijicozum.com`) silin, şunları ekleyin:

   | Tür | Ad | Değer |
   |---|---|---|
   | A | `@` (boş) | `216.198.79.1` |
   | CNAME | `www` | `91dda51a3d2ea529.vercel-dns-017.com` |

   Alternatif eski değerler de çalışır: `A 76.76.21.21` ve `CNAME cname.vercel-dns.com`. Güncel değerler için Vercel → Project → Settings → Domains ekranına bakın. `www.dijicozum.com`, kalıcı yönlendirmeyle (308) `dijicozum.com`'a gider. Yayılması dakikalar ile birkaç saat sürebilir.
5. Bundan sonra `main` dalına yapılan her `git push` otomatik yayına alınır. Pull request'ler için önizleme adresi üretilir.

## Yayın öncesi kontrol listesi

- [ ] `merhaba@dijicozum.com` gerçekten çalışıyor mu? (Turkticaret e-posta paketi, Zoho Mail veya Google Workspace ile açın. Adres `assets/config.js` içinde.)
- [ ] Şirket kurulunca `gizlilik.html` 1. maddesine ticari unvan, vergi numarası ve adres eklendi; metin hukuk danışmanınca kontrol edildi.
- [ ] Marka başvurusu (TÜRKPATENT, sınıf 35 ve 42): logolu başvuru önerilir; `assets/logo/png/*-mono-beyaz-zemin.png` dosyaları hazır.
- [ ] Hukuki yapı (şahıs/limited) netleşti; fatura ve unvan bilgisi siteye eklendi.
- [ ] İletişim formu şu an kullanıcının e-posta uygulamasını açar (`mailto`). Gerçek form için Formspree/Resend gibi bir servis bağlanabilir.
- [ ] Google Search Console'a `dijicozum.com` eklenip `sitemap.xml` gönderildi.
- [ ] Fiyat/paket bilgisi eklenecekse ana sayfaya bölüm eklenmeli (şu an "teklif ile" yaklaşımı).
