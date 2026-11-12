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
