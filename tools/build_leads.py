"""Türkiye güzellik merkezi aday listesini leads/ klasörüne Excel olarak yazar.

Not: leads/ klasörü .gitignore'dadır, GitHub'a gönderilmez (iş sahiplerinin iletişim bilgileri).
Kullanım: python tools/build_leads.py   (openpyxl gerekir)
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

OUT = Path(__file__).resolve().parent.parent / "leads" / "turkiye-guzellik-adaylar.xlsx"

HEAD = ["Öncelik", "Şehir / ilçe", "İşletme", "Adres", "Telefon", "E-posta", "E-posta durumu", "Instagram",
        "Web sitesi", "Randevu yöntemi (bulgu)", "Zincir mi?", "Doğrulama", "İlk cümle önerisi", "Kaynak",
        "Durum", "İlk temas tarihi", "Not"]

ACIK, GIZLI, YOK = "Sitede açık yazıyor", "Sitede var, gizli (elle kopyalayın)", "Bulunamadı"
DOGRULANDI = "Doğrulandı (işletmenin kendi sayfası)"

# Öncelik: A = e-posta var + online randevu sistemi yok. B = e-posta yok (telefon/Instagram) ya da randevu formu var, kontrol gerekir.
# C = yalnızca isim/site biliniyor, sayfa açılamadı ya da doğrulanmadı.
R = []


def add(o, sehir, isim, adres, tel, mail, mdurum, ig, web, randevu, zincir, dogr, cumle, kaynak, not_=""):
    R.append([o, sehir, isim, adres, tel, mail, mdurum, ig, web, randevu, zincir, dogr, cumle, kaynak, "Yeni", "", not_])


# ---------------- A: e-posta var, online randevu yok
add("A", "Ankara / Çankaya", "New You Güzellik Merkezi", "Tunalı Hilmi Cad. 50/5", "0533 502 38 37", "newyou.guzellik@gmail.com", ACIK,
    "@newyou_guzellik", "newyouguzellik.com", "Telefon ve WhatsApp. Online randevu sistemi yok.", "Tek şube", DOGRULANDI,
    "Randevu için telefon ve WhatsApp'a yönlendiriyorsunuz. Gün içinde çok mesaj demek.", "https://www.newyouguzellik.com/contact/")
add("A", "Antalya / Muratpaşa", "Talin Güzellik Merkezi", "Perge Bulvarı, Süleyman Ekim Sit. B1 Blok No:61", "0543 520 00 77",
    "info@talinguzellikmerkezi.com", ACIK, "@talinguzellikmerkezi", "talinguzellikmerkezi.com",
    "Telefon ve WhatsApp. Sitede online randevu formu yok.", "Tek şube", DOGRULANDI,
    "Sitenizde randevuyu telefon ve WhatsApp'tan alıyorsunuz. Müşteri kendi saatini seçebilse işiniz kolaylaşır.", "https://www.talinguzellikmerkezi.com/")
add("A", "İstanbul / Kadıköy", "Kadıköy Güzellik Merkezi", "Osmanağa Mah. Karadut Sk. No:31 D:4", "0216 347 45 65 / 0552 421 11 40",
    "info@kadikoyguzellikmerkezi.com", ACIK, "@medistbeautycenter", "kadikoyguzellikmerkezi.com.tr",
    "Telefon ve WhatsApp (doğrudan arama/mesaj).", "Tek şube", DOGRULANDI,
    "Randevular doğrudan telefon ve WhatsApp'tan geliyor. Bu, yoğun günlerde karışabiliyor.", "https://www.kadikoyguzellikmerkezi.com.tr/")
add("A", "İstanbul / Beylikdüzü", "Mabel Güzellik", "Barış Mah. E-5 Yan Yolu, Westside No:28/89", "0507 829 40 40",
    "randevu@mabelguzelliksalonu.com", ACIK, "@mabelguzelliksalonuu", "mabelguzelliksalonu.com",
    "WhatsApp ve telefon. Online randevu sistemi yok.", "Tek şube", DOGRULANDI,
    "Randevu için WhatsApp ve telefonu kullanıyorsunuz. Aynı adrese 'randevu@' açmışsınız, mesaj hacmi yüksek olmalı.", "https://mabelguzelliksalonu.com/")
add("A", "Kayseri / Kocasinan", "Sirius Luxe Beauty Saloon", "Erciyesevler Mah. Bozantı Cad. 208/A Onurkent Sitesi altı", "0553 391 23 42 / 0352 445 00 38",
    "info@siriusluxebeauty.com", ACIK, "@siriusluxekayseri", "siriusluxebeauty.com",
    "WhatsApp ve telefon. Sayfada online takvim yok.", "Tek şube", DOGRULANDI,
    "Randevuyu WhatsApp ve telefondan alıyorsunuz. Müşteri online saat seçebilse nasıl olur?", "https://www.siriusluxebeauty.com/")
add("A", "Konya / Meram", "Dermopark VIP Konya Güzellik Merkezi", "Sahibiata, Fevzi Çakmak Sk. No:1 D:1", "0552 397 56 53",
    "info@dermoparkvip.com", ACIK, "@dermoparkvip", "dermoparkvip.com",
    "WhatsApp ve telefon. Online sistem yok.", "3 şubeli küçük zincir (Konya, Niğde, Ereğli)", DOGRULANDI,
    "Birden fazla şubenizde randevu WhatsApp ve telefondan yürüyor. Tek panelde toplanması ilginizi çeker mi?",
    "https://dermoparkvip.com/", "Küçük zincir: karar merkezi tek kişi olabilir, sorun.")
add("A", "Eskişehir / Odunpazarı", "Dore Güzellik Eskişehir", "İstiklal Mah. İki Eylül Cad. Yalbı Sk. Yılmazlar İş Merkezi No:18 K:2 D:3",
    "0222 220 22 52 / 0543 206 78 51", "info@doreguzellikeskisehir.com", ACIK, "@doreguzellikeskisehir", "doreguzellikeskisehir.com",
    "WhatsApp, telefon ve iletişim formu. Randevu takvimi yok.", "Tek şube", DOGRULANDI,
    "Sitenizde randevu için WhatsApp, telefon ve iletişim formu var. Hepsi tek yerde toplanabilir.", "https://www.doreguzellikeskisehir.com/")
add("A", "Adana / Seyhan", "Adana Lazer Salonu ve Güzellik Merkezi (lazersalonu.com)", "Kurtuluş Mah. Atatürk Cad. Saniye Ethem Apt K:1 D:1", "0322 456 24 71 / 0549 456 24 71",
    "", GIZLI, "Instagram profili sitede var", "lazersalonu.com", "WhatsApp ve telefon.", "Tek şube", DOGRULANDI,
    "Randevuyu WhatsApp ve telefondan alıyorsunuz.", "https://lazersalonu.com/", "E-posta adresi sitede var ama gizlenmiş. Siteyi açıp iletişim bölümünden kopyalayın.")
add("A", "Eskişehir / Tepebaşı", "Este Lórien Güzellik Merkezi", "Hoşnudiye Mah. Çiftkurt Sk. No:1 HKS Plaza K:1 D:2", "0222 220 87 11 / 0534 526 80 18",
    "", GIZLI, "@estelorien", "estelorien.com.tr", "Telefon ve WhatsApp üzerinden randevu talebi.", "Tek şube", DOGRULANDI,
    "Randevu talebini telefon ve WhatsApp'tan alıyorsunuz. Hepsini tek panelde toplamak ister misiniz?", "https://www.estelorien.com.tr/",
    "E-posta sitede var ama gizlenmiş. Siteden elle kopyalayın.")

# ---------------- B: e-posta yok (telefon veya Instagram)
add("B", "Bursa / Nilüfer", "Sevil Muradova Güzellik Merkezi", "Nilüfer (tam adres sitede yok)", "WhatsApp 0537 789 19 90", "", YOK, "@sevilmuradovaestetik",
    "sevilmuradova.com", "İletişim formu + WhatsApp.", "Tek şube", DOGRULANDI, "", "https://sevilmuradova.com/iletisim/", "E-posta yok: telefon/WhatsApp veya Instagram.")
add("B", "Bursa / Nilüfer", "Derya Baştuğ Beauty", "Esentepe Mh. Kasap Sk. No:10 D:7 Prestij Aydemir İş Merkezi", "0534 603 46 85", "", YOK, "Bulunamadı",
    "deryabastugbeauty.com", "WhatsApp ve telefon.", "Tek şube", DOGRULANDI, "", "https://deryabastugbeauty.com/hizmetler", "E-posta yok: telefon.")
add("B", "Antalya / Muratpaşa", "Mesa Güzellik", "Altındağ Mah. 100. Yıl Bulvarı Süleyman Kilit Apt. B Blok K:1 D:3", "0536 764 15 27", "", YOK, "Bulunamadı",
    "mesaguzellik.com", "WhatsApp ve telefon.", "Tek şube", DOGRULANDI, "", "https://mesaguzellik.com/", "E-posta yok: telefon.")
add("B", "İstanbul / Beylikdüzü", "Carmine Beauty Center", "Cumhuriyet Mah. Erdemli Cad. Onur Sk. Demir Romance Sitesi Akik-3", "0532 487 18 99", "", YOK, "@beautycarmine",
    "carmineguzellik.com", "WhatsApp ve telefon.", "Tek şube", DOGRULANDI, "", "https://www.carmineguzellik.com/", "E-posta yok: telefon/Instagram.")
add("B", "Konya / Beyhekim", "Derma Lazer Epilasyon Güzellik Merkezi", "Beyhekim Mah. Kazeruni Sk. Ertan İş Hanı K:1-112", "0332 353 19 22 / 0533 515 56 28", "", YOK, "Bulunamadı",
    "dermalazer.com", "Telefon. Online sistem yok.", "Tek şube", DOGRULANDI, "", "https://dermalazer.wordpress.com/iletisim/", "E-posta yok: telefon.")
add("B", "Adana / Çukurova", "Natty Clinical Beauty", "Süleyman Demirel Blv. Göl Vadi Evleri B Blok No:57", "0549 180 01 47", "", YOK, "@nattyclinicalbeauty",
    "nattyclinicalbeauty.com", "WhatsApp.", "Tek şube", DOGRULANDI, "", "https://www.nattyclinicalbeauty.com/", "E-posta yok: WhatsApp/telefon.")
add("B", "Kayseri", "Lima Estetik", "Adres sitede yok", "0545 588 33 38", "", YOK, "@limaestetik",
    "limaestetik.com", "WhatsApp ve telefon. Online sistem yok.", "Tek şube", DOGRULANDI, "", "https://www.limaestetik.com/", "E-posta yok: telefon/Instagram.")
# randevu formu var, ama e-posta var: gerçek bir takvim mi kontrol edin
add("B", "Antalya / Muratpaşa", "Tülay Kalmaz Beauty Center", "Konyaaltı Cad. Nuri Işık Demir Apt K:1 No:2", "0530 425 87 82", "kalmaztulay@gmail.com", ACIK, "Bulunamadı",
    "tulaykalmaz.com", "WhatsApp + online randevu formu (gerçek takvim olup olmadığı kontrol edilmeli).", "Tek şube", DOGRULANDI, "",
    "https://www.tulaykalmaz.com/antalya-diode-buz-lazer/", "Formu deneyin: saat seçimi/takvim var mı?")
add("B", "Kayseri / Kocasinan", "Quvars Beauty Studio", "Erciyesevler, Sivas Cad. Bulvarı 229/A", "0541 118 63 38", "info@quvarsbeauty.com", ACIK, "@quvarsbeauty",
    "quvarsguzellikmerkezi.com.tr", "Online randevu formu + WhatsApp + telefon (gerçek takvim olup olmadığı kontrol edilmeli).", "Tek şube", DOGRULANDI, "",
    "https://www.quvarsguzellikmerkezi.com.tr/", "Formu deneyin: saat seçimi/takvim var mı?")
add("B", "Eskişehir", "Evolusi Güzellik", "Hoşnudiye Mah. Nayman Sk. No:1 Selka Apt. K:5 D:7", "0222 405 16 60 / 0537 771 26 00", "info@evolusiguzellik.com", ACIK,
    "@evolusiguzellik", "evolusiguzellik.com", "Online randevu formu (hizmet seçimi) + WhatsApp.", "Tek şube", DOGRULANDI, "",
    "https://www.evolusiguzellik.com/", "Formu deneyin: saat seçimi/takvim var mı?")

# ---------------- C: doğrulanacak (sayfa açılamadı ya da yalnızca isim)
for sehir, isim, web, kaynak in [
    ("İzmir / Bornova", "Dermaface Estetik", "dermaface.com.tr", "https://www.dermaface.com.tr/"),
    ("İzmir / Bornova", "Muna Güzellik Salonu", "munaguzelliksalonu.com", "https://www.munaguzelliksalonu.com/lazer-epilasyon/"),
    ("İzmir / Alsancak", "Remedica Beauty", "remedicabeauty.com", "https://remedicabeauty.com/Sayfa/318/alsancak-guzellik-merkezi"),
    ("Bursa / Nilüfer", "Bursa Beauty Center", "bursabeautycenter.com", "https://www.bursabeautycenter.com/nilufer-guzellik-merkezi-bursa/"),
    ("Gaziantep / Şahinbey", "Akkent Güzellik Merkezi", "akkentguzellikmerkezi.com", "https://www.akkentguzellikmerkezi.com/"),
    ("Gaziantep / Şehitkamil", "Nurten İshakoğlu Güzellik Estetik", "nurtenishakogluguzellikestetik.com", "https://nurtenishakogluguzellikestetik.com/Sayfa/280/sehitkamil-guzellik-merkezi/"),
    ("Kayseri / Kocasinan", "Taies Güzellik ve SPA Merkezi", "taiesguzellik.com", "https://taiesguzellik.com/"),
    ("Samsun / Atakum", "Pepuza Beauty", "pepuzabeauty.com", "https://pepuzabeauty.com/"),
    ("Samsun / Atakum", "Derma Bella", "atakumlazer.com", "https://atakumlazer.com/"),
    ("Samsun", "Dermasam Güzellik Merkezi", "dermasam.com", "https://www.dermasam.com/"),
    ("Ankara / Çankaya", "Nova Beauty VIP", "", "https://www.sektorlistesi.com.tr/firma/ankara-guzellik-merkezi-ankara-lazer-epilasyon-cilt-bakim-kalici-makyaj-tavsiye-nova-beauty-vip"),
    ("Ankara / Çankaya", "Ankara Lazer", "ankaralazer.com", "https://www.ankaralazer.com/en"),
]:
    add("C", sehir, isim, "", "", "", YOK, "", web, "Sayfa açılamadı veya doğrulanmadı.", "?", "Doğrulanacak", "", kaynak,
        "Siteyi elle açıp e-posta ve randevu yöntemine bakın.")

# ---------------- Başakşehir (önceki tur)
add("A", "İstanbul / Başakşehir", "Mediplast Güzellik Merkezi", "Başakşehir Mah., Bulvar İstanbul Evleri G Blok No:2", "0552 650 6000", "info@mediplast.com.tr", ACIK,
    "@mediplast.guzellik", "mediplast.com.tr", "Telefon, WhatsApp veya Instagram. Online randevu yok.", "Tek şube", DOGRULANDI,
    "Sitenizde 'hızlı fiyat bilgisi için hemen yazın' diyorsunuz. Bu, gün içinde çok WhatsApp mesajı demek.",
    "https://www.mediplast.com.tr/guzellik-merkezi-basaksehir-iletisim/")
add("B", "İstanbul / Başakşehir", "Pınar Bayan Kuaförü ve Güzellik Merkezi", "Güvercintepe Mah. Ahmet Yesevi Cad. Görümlü Sk. 35a", "0532 442 83 89", "", YOK, "Bulunamadı",
    "pinarbayankuaforu.com.tr", "Yalnızca WhatsApp.", "Tek şube", DOGRULANDI, "", "https://pinarbayankuaforu.com.tr/", "E-posta yok: telefon.")
add("B", "İstanbul / Başakşehir", "Sevinç Beauty", "Bahçeşehir 2. Kısım, Avni Akyol Bul. Loca Sitesi A Blok D:18", "0552 922 82 99", "info@sevincbeauty.com", "Arama sonucunda göründü, sayfadan doğrulanmadı",
    "Bulunamadı", "sevincbeauty.com", "Doğrulanmadı.", "Tek şube", "Kısmen", "", "https://sevincbeauty.com/tr/iletisim", "Göndermeden önce siteyi kontrol edin.")
add("B", "İstanbul / Başakşehir", "Başakşehir Beauty", "Kayabaşı Mah. B5 Blok No:29", "0541 547 14 46", "info@basaksehirbeauty.com", ACIK, "Bulunamadı",
    "basaksehirbeauty.com", "WhatsApp'a bağlanan basit form + telefon. Gerçek takvim yok.", "Tek şube", DOGRULANDI, "", "https://basaksehirbeauty.com/", "Form var: orta öncelik.")
add("B", "İstanbul / Bahçeşehir", "Ville Esthetique", "Bahçeşehir 1. Kısım, Ebabil Sk. Defne 3 Villa 12", "0532 111 90 85", "", YOK, "@villeestetik", "villeesthetique.com",
    "Instagram, Facebook veya telefon.", "Tek şube", "Kısmen", "", "https://www.instagram.com/villeestetik/", "E-posta yok: Instagram/telefon.")
add("B", "İstanbul / Başakşehir", "Ayşe Sarı Beauty Center", "Kayaşehir Kuzey yakası", "0541 236 91 62", "", YOK, "@aysesaribeautycenter", "Bulunamadı",
    "Instagram/telefon.", "Tek başına", "Kısmen", "", "https://www.instagram.com/aysesaribeautycenter/", "Web sitesi yok adayı.")

ELENEN = [
    ["Essi Güzellik Merkezi (Konya)", "Sitesinde online randevu formu ve takvim sistemi var.", "https://essikonya.com/sikca-sorulan-sorular/"],
    ["Yasemen Yalım Beauty (Gaziantep)", "Online randevu formu var ve çok şubeli.", "https://www.yasemenyalim.com/"],
    ["Tuğçe Naz Güzellik (Antalya)", "Online randevu formu var, e-posta yok.", "https://tugcenazguzellik.com/en"],
    ["Dilek Gezer Beauty Center (Samsun)", "Online randevu formu var, e-posta yok.", "https://www.dilekgezer.com/"],
    ["Reem Güzellik Merkezi (Başakşehir)", "Kendi online randevu sistemi var.", "https://www.randevu.reemsalon.com/"],
    ["Esse Life (tüm şubeler)", "Franchise/zincir, karar merkezi başka.", "https://beylikduzu.esselife.com.tr/"],
    ["Epilife, Daphne Lazer, De Milano, Neslim Güngen, Kübra Toksoy, Bia Hair Point", "Çok şubeli zincirler.", "https://mekan.com/guzellik/c/istanbul/i/basaksehir"],
    ["Suit Güzellik (franchise)", "Franchise, karar merkezi başka.", "https://bursa.suitguzellik.com/"],
    ["Poliklinik ve estetik klinikleri (Elif Dinçarslan vb.)", "Sağlık verisi (özel nitelikli) işleniyor, hedefimiz dışında.", "https://elifdincarslanpoliklinigi.com/"],
]

KULLANIM = [
    "Bu liste yalnızca işletmelerin kendi sitelerinde yayımladığı veya herkese açık dizinlerde yer alan iletişim bilgilerinden derlendi.",
    "",
    "ÖNCELİK: A = e-posta var + online randevu sistemi yok (ilk gönderim listesi). B = e-posta yok (telefon/Instagram) ya da randevu formu var, kontrol gerekir. C = sayfa açılamadı/doğrulanmadı.",
    "E-POSTA DURUMU 'gizli' ise: adres sitede var ama korumalı. Siteyi açıp iletişim bölümünden elle kopyalayın.",
    "",
    "GÖNDERMEDEN ÖNCE (5 dakika):",
    "  1) Sitede veya Instagram bio'sunda 'randevu al' düğmesi/takvim var mı? Varsa 'Elenenler'e taşıyın.",
    "  2) E-postayı sitenin kendisinden kopyalayın. Tahmin etmeyin.",
    "  3) Şirketiniz kurulup unvan ve adres imzada yazana kadar hiçbir tanıtım e-postası GÖNDERMEYİN.",
    "",
    "YASAL NOTLAR (hukuki teyit alın):",
    "  - Esnaf ve tacire ticari ileti önceden izin olmadan gönderilebilir, ama her mesajda kimliğiniz (unvan, adres) ve kolay bir çıkma seçeneği olmalı.",
    "  - Çıkma isteğinden sonra 3 iş günü içinde göndermeyi bırakın. 'Çıkanlar' sekmesine yazın.",
    "  - Günde en fazla 15-20 e-posta. Bu dosyayı GitHub'a yüklemeyin (leads/ .gitignore'da).",
]


def style(ws, widths, freeze="D2"):
    hf = PatternFill("solid", fgColor="0F172A")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = hf
        c.alignment = Alignment(vertical="center", wrap_text=True)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(vertical="top", wrap_text=True)
    ws.freeze_panes = freeze
    ws.row_dimensions[1].height = 32


wb = Workbook()
ws = wb.active
ws.title = "Adaylar"
ws.append(HEAD)
order = {"A": 0, "B": 1, "C": 2}
for r in sorted(R, key=lambda x: (order[x[0]], x[1])):
    ws.append(r)
style(ws, [8, 22, 34, 36, 22, 30, 24, 22, 26, 44, 20, 22, 50, 50, 10, 14, 34], "D2")
fills = {"A": "DCFCE7", "B": "FEF9C3", "C": "F3F4F6"}
for row in ws.iter_rows(min_row=2):
    row[0].fill = PatternFill("solid", fgColor=fills[row[0].value])
    row[0].font = Font(bold=True)

ws2 = wb.create_sheet("Elenenler")
ws2.append(["İşletme", "Neden elendi", "Kaynak"])
for r in ELENEN:
    ws2.append(r)
style(ws2, [50, 60, 60], "A2")

ws3 = wb.create_sheet("Çıkanlar")
ws3.append(["İşletme / e-posta / telefon", "Çıkma isteği tarihi", "Nasıl geldi (yanıt, telefon...)"])
style(ws3, [44, 22, 40], "A2")

ws4 = wb.create_sheet("Nasıl kullanılır")
ws4.append(["Kullanım notları"])
for line in KULLANIM:
    ws4.append([line])
ws4.column_dimensions["A"].width = 150
for row in ws4.iter_rows(min_row=2):
    row[0].alignment = Alignment(wrap_text=True, vertical="top")
ws4["A1"].font = Font(bold=True)

OUT.parent.mkdir(exist_ok=True)
wb.save(OUT)
from collections import Counter
c = Counter(r[0] for r in R)
mail_acik = sum(1 for r in R if r[0] == "A" and r[6] == ACIK)
mail_gizli = sum(1 for r in R if r[0] == "A" and r[6] == GIZLI)
sehirler = sorted({r[1].split(" / ")[0] for r in R})
print(f"Yazıldı: {OUT}")
print(f"A={c['A']} B={c['B']} C={c['C']} toplam={len(R)} | elenen={len(ELENEN)}")
print(f"A içinde e-posta açık={mail_acik}, gizli={mail_gizli}")
print("İller:", ", ".join(sehirler))
