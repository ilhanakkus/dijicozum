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
4. **DNS (Turkticaret):** alan adı panelinde DNS yönetimine girin, Vercel'in gösterdiği kayıtları ekleyin (genellikle kök alan için `A 76.76.21.21`, `www` için `CNAME cname.vercel-dns.com`; Vercel'in ekranındaki değerler geçerlidir). Yayılması dakikalar ile birkaç saat sürebilir.
5. Bundan sonra `main` dalına yapılan her `git push` otomatik yayına alınır. Pull request'ler için önizleme adresi üretilir.

## Yayın öncesi kontrol listesi

- [ ] `merhaba@dijicozum.com` gerçekten çalışıyor mu? (Turkticaret e-posta paketi, Zoho Mail veya Google Workspace ile açın. Adres `assets/config.js` içinde.)
- [ ] `gizlilik.html` içindeki `[Ad Soyad / Şirket Unvanı]` ve `[Adres]` alanları dolduruldu, metin hukuk danışmanınca kontrol edildi.
- [ ] Hukuki yapı (şahıs/limited) netleşti; fatura ve unvan bilgisi siteye eklendi.
- [ ] İletişim formu şu an kullanıcının e-posta uygulamasını açar (`mailto`). Gerçek form için Formspree/Resend gibi bir servis bağlanabilir.
- [ ] Google Search Console'a `dijicozum.com` eklenip `sitemap.xml` gönderildi.
- [ ] Fiyat/paket bilgisi eklenecekse ana sayfaya bölüm eklenmeli (şu an "teklif ile" yaklaşımı).
