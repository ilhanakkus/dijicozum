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


# ======================= 2. ve 3. TUR (genişletilmiş tarama) =======================
CUM_WA = "Randevuları WhatsApp ve telefondan alıyorsunuz. Gün içinde çok mesaj ve arama demek."
CUM_FORM = "Sitenizde iletişim formu var ama müşteri boş saati göremiyor. Kendi saatini seçebilse işiniz kolaylaşır."
CUM_TEL = "Randevuyu telefon ve e-postayla alıyorsunuz. Müşteri online saat seçebilse nasıl olur?"
KAYNAK_NOT = "Web sitesinden doğrulandı."

def A(sehir, isim, adres, tel, mail, ig, web, randevu, zincir, cumle, kaynak, not_="", gizli=False):
    add("A", sehir, isim, adres, tel, mail, GIZLI if gizli else ACIK, ig, web, randevu, zincir, DOGRULANDI, cumle, kaynak, not_ or ("E-posta sitede var ama gizlenmiş: siteden elle kopyalayın." if gizli else ""))

def B(sehir, isim, adres, tel, mail, mdurum, ig, web, randevu, zincir, kaynak, not_):
    add("B", sehir, isim, adres, tel, mail, mdurum, ig, web, randevu, zincir, DOGRULANDI, "", kaynak, not_)

# ---------- A: e-posta var + online randevu yok
A("İstanbul / Bakırköy", "Bakırköy Lazer Epilasyon Estetik ve Güzellik Merkezi", "Zeytinlik, Fişekhane Cd. No:34", "0212 571 44 61 / 0533 378 38 90", "info@bakirkoylazer.com", "@bakirkoylazer", "bakirkoylazer.com", "Yalnızca iletişim formu + telefon. Takvim yok.", "Tek merkez", CUM_FORM, "https://www.bakirkoylazer.com/iletisim/")
A("İstanbul / Bakırköy", "Mayl's Beauty", "Nivo Ataköy AVM -1. Kat, E-5 Yan Yol No:12K A Blok 187", "0507 939 10 12", "info@maylsbeauty.com", "@maylsbeautyatakoy", "maylsbeauty.com", "WhatsApp veya telefon.", "Tek şube", CUM_WA, "https://maylsbeauty.com/hizmetler/lazer-epilasyon")
A("İstanbul / Beşiktaş", "Arzu Bulut Güzellik", "Gayrettepe, Barbaros Blv. Dr. Orhan Birman İş Merkezi No:149/1", "0212 275 29 85 / 0507 259 42 56", "info@arzubulutguzellik.com", "@arzubulutguzellik", "arzubulutguzellik.com", "WhatsApp ve telefon.", "Tek merkez", CUM_WA, "https://www.arzubulutguzellik.com/bakirkoy-guzellik-merkezi/")
A("İstanbul / Maltepe", "Dore Estetica", "Bağlarbaşı Mah. Bağdat Cad. No:415/59", "0553 946 89 06", "info@doreestetica.com", "@doreesteticaguzellik", "doreestetica.com", "WhatsApp/telefon. Online form yok.", "Tek şube", CUM_WA, "https://www.doreestetica.com/")
A("İstanbul / Maltepe", "Pina Maltepe Güzellik Salonu", "Maltepe (tam adres sitede yok)", "0539 342 34 87", "info@pinaguzellik.com", "@pina_beauty_house", "pinaguzelliksalonu.com", "Telefon/WhatsApp.", "Tek konum", CUM_WA, "https://pinaguzelliksalonu.com/en/")
A("İstanbul / Kartal", "Estecosmo", "Kartal (tam adres sitede yok)", "0541 397 64 63", "bilgi@estecosmo.com", "@estecosmotr", "estecosmo.com", "WhatsApp ve telefon.", "Tek konum", CUM_WA, "https://www.estecosmo.com/")
A("İstanbul / Sarıyer", "Epika Lazer Epilasyon Merkezi", "Yeniköy, Köybaşı Cd. No:74", "0212 299 70 84 / 0212 266 10 00", "info@epika.com", "Bulunamadı", "epikalazer.com", "Yalnızca telefon.", "Tek merkez", CUM_TEL, "https://epikalazer.com/", "E-posta alan adı (epika.com) site adresinden (epikalazer.com) farklı: göndermeden önce doğrulayın.")
A("İstanbul / Bağcılar", "Volans Güzellik Salonu", "İstanbul Cd. No:20 K:3 D:3", "0554 505 56 56", "info@volansguzellik.com", "@volansguzellik", "volansguzellik.com", "Yalnızca WhatsApp ve telefon.", "Tek şube", CUM_WA, "https://www.volansguzellik.com/")
A("İstanbul / Kağıthane", "Medicamine Beauty", "Hamidiye Mah. Cendere Cad. 103/2/19 Porta Vadi T3 Blok K:2", "0552 000 00 20", "info@medicamine.com", "@medicaminekafamasaji", "medicamine.com", "WhatsApp ve telefon (sitede /randevu sayfası referansı var, takvim görülmedi).", "Tek şube", CUM_WA, "https://medicamine.com/")
A("İstanbul / Eyüpsultan", "Lin Güzellik Merkezi", "Yeşilpınar Mah. Özlem Cad. No:19 K:1", "0212 535 25 45 / 0506 174 58 04", "info@linguzellikmerkezi.com.tr", "@LinGüzellik", "linguzellikmerkezi.com.tr", "İletişim formu, WhatsApp, telefon (takvim yok).", "Tek konum", CUM_FORM, "https://linguzellikmerkezi.com.tr/kagithane-guzellik-merkezi/")
A("Ankara / Etimesgut", "Filiz Karslıoğlu Cilt Atölyesi", "Yeni Bağlıca Mah. 1065. Sk. No:5", "0312 284 43 33 / 0552 740 33 43", "info@filizkarslioglu.com", "@ciltatolyesi", "filizkarslioglu.com", "Telefon ve WhatsApp.", "Tek şube", CUM_WA, "https://www.filizkarslioglu.com/umitkoy-buz-lazer-merkezi/")
A("Ankara / Etimesgut", "BK Beauty Lounge", "Ser Tower (tam adres sitede yok)", "0546 401 58 14", "info@eryamanguzellikmerkezi.com", "Bulunamadı", "etimesgutguzellikmerkezi.com", "Telefon ('Hemen Ara').", "Tek konum", CUM_TEL, "https://etimesgutguzellikmerkezi.com/", "E-posta alan adı site adresinden farklı: göndermeden önce doğrulayın.")
A("Ankara / Kızılay", "Nurhan's Beauty Center", "Kızılay", "0542 428 20 42", "info@nurhansbeautycenter.com.tr", "@nurhans_beauty", "nurhansbeautycenter.com.tr", "WhatsApp + iletişim formu (takvim yok).", "Tek konum", CUM_FORM, "https://nurhansbeautycenter.com.tr/")
A("Ankara / Sincan", "Yenikent Güzellik Salonu", "Mustafa Kemal Mah. Mehmet Akif Cd. Üslü Apt. No:27/B", "0533 479 66 81", "info@yenikentguzelliksalonu.com", "@pinargulkuafor", "yenikentguzelliksalonu.com", "WhatsApp.", "Tek konum", CUM_WA, "https://yenikentguzelliksalonu.com/", "Google'da 250'den fazla 5 yıldızlı yorumu var.")
A("İzmir / Bayraklı", "Laita Güzellik Merkezi", "Adalet Mah. 1593/1. Sk. No:39 A", "0544 632 77 99", "info@laita.com.tr", "Sitede link var", "laita.com.tr", "Telefon ve e-posta. Online form gözlenmedi.", "Tek merkez", CUM_TEL, "https://www.laita.com.tr/")
A("Bursa / Nilüfer", "Leon Güzellik Merkezi", "Odunluk Mah. Akpınar Cad. Şentürkler Plaza No:7/20", "0542 285 74 16", "info@leonguzellik.com", "Boş link", "leonguzellik.com", "Yalnızca WhatsApp ve telefon.", "Tek konum", CUM_WA, "https://www.leonguzellik.com/")
A("Mersin / Mezitli", "Anita Güzellik Merkezi", "Akdeniz Mah. 39713 Sk. No:13", "0542 125 01 33", "haticesoyak79@gmail.com", "Bulunamadı", "anitaguzellik.com.tr", "Telefon ve WhatsApp.", "Tek şube", CUM_WA, "https://anitaguzellik.com.tr/")
A("Muğla / Fethiye", "Fethiye Lazer Epilasyon (FT Vip Beauty Center)", "Tuzla Mah. Mustafa Kemal Bulvarı No:23/B", "0501 202 34 44", "info@fethiyelazerepilasyon.com", "@ftvipbeautycenter", "fethiyelazerepilasyon.com", "Telefon ve WhatsApp.", "4 bağlı işletme (küçük grup)", CUM_WA, "https://www.fethiyelazerepilasyon.com/")
A("Konya / Meram", "Selvera Beauty", "Yenişehir Mah. Gazze Cad. No:13/210 Çarşı Meram B Giriş K:2", "0551 631 68 92", "iletisim@selverabeauty.com.tr", "@selveraabeauty", "selverabeauty.com.tr", "WhatsApp ve telefon.", "Tek şube", CUM_WA, "https://selverabeauty.com.tr/")
A("Gaziantep / Şehitkamil", "Simurg Güzellik ve Ayşe Ay", "Değirmiçem Mah. Mareşal Fevzi Çakmak Blv. No:28", "0342 335 76 00", "bilgi@simurgguzelliksalonu.com", "@ayseay.simurg", "simurgguzelliksalonu.com", "WhatsApp ve telefon.", "Tek şube", CUM_WA, "https://www.simurgguzelliksalonu.com/")
A("Gaziantep / Şehitkamil", "Selenyum Güzellik Merkezi", "Batıkent Mah. Ali İhsan Göğüş Cad. Kaya Apt No:111/A", "0342 909 97 17 / 0532 054 34 49", "info@selenyumguzellik.com", "Bulunamadı", "selenyumguzellik.com", "Telefon veya e-posta. Online form yok.", "Tek şube", CUM_TEL, "https://www.selenyumguzellik.com/")
A("Gaziantep / Şehitkamil", "Alya Plus Güzellik Merkezi", "İncilipınar, Gazi Muhtar Paşa Blv. Tekerekoğlu İş Merkezi altı 16/23", "0546 805 11 11", "info@alyaplus.com", "Bulunamadı", "alyaplus.com", "WhatsApp ve telefon.", "Tek lokasyon", CUM_WA, "https://alyaplus.com/")
A("Tekirdağ / Çorlu", "Figen Estetik ve Güzellik Salonu", "Omurtak Cad. Manolya Apt. A Blok No:176 K:3 D:6", "0282 651 40 01 / 0282 651 15 69", "randevu@figenestetik.com.tr", "Bulunamadı", "figenestetik.com.tr", "Telefon ve e-posta ile randevu. Online form yok.", "Tek şube", CUM_TEL, "https://www.figenestetik.com.tr/bizi-taniyin.html")
A("Tekirdağ", "Yelsa Estetik ve Güzellik", "Hürriyet, Gül Park 59 Sitesi, Öğretmenler Cd. C Blok No:23", "0536 475 70 59", "info@yelsatekirdag.com", "@yelsaguzellik", "yelsatekirdag.com", "WhatsApp ve telefon.", "4 şube (Tekirdağ, Beylikdüzü, Ataköy, Samsun)", CUM_WA, "https://yelsatekirdag.com/", "Küçük zincir: karar merkezi sorulmalı.")
A("Çanakkale", "On7 Estetik Güzellik", "İsmetpaşa Mah. Aynalı Çeşme Sk. No:14 D:2", "0286 214 17 17 / WhatsApp 0552 314 17 17", "on7lazerepilasyon@gmail.com", "@on7estetikguzellik", "on7lazerepilasyon.com", "WhatsApp ve telefon.", "Tek şube", CUM_WA, "https://www.on7lazerepilasyon.com/")
A("Elazığ", "Belinda Güzellik Merkezi", "Yeni Mah. Gazi Cad. No:28 Durak Han Apt K:3-4", "0506 132 39 28 / 0424 238 18 19", "belindaguzellik23@gmail.com", "@belinda_guzellik_merkezi", "belindaguzellik.com", "WhatsApp ve telefon.", "Tek şube", CUM_WA, "https://www.belindaguzellik.com/")
A("Manisa / Şehzadeler", "Ivory Güzellik Merkezi", "1. Anafartalar, Hükümet Cd. No:65/A", "0505 031 27 32", "ivorybeautycenter@gmail.com", "@ivorybeautycenter", "ivorybeautycenter.com", "'Randevu Al' bağlantısı var, gerçek takvim yok.", "Tek şube", CUM_FORM, "https://www.ivorybeautycenter.com/")
# e-posta sitede var ama gizli
A("Bursa / Mudanya", "Gülnur Yürek Güzellik Merkezi", "Kırca Hasanbey Mah. Bostan Sk. No:8 K:1 D:3", "0542 784 98 58", "", "@gulnuryurekbeautycenter", "gulnuryurekguzellikmerkezi.com.tr", "Telefon, WhatsApp. Online takvim yok.", "Tek konum", CUM_WA, "https://gulnuryurekguzellikmerkezi.com.tr/", gizli=True)
A("Muğla / Fethiye", "Likya Güzellik Salonu", "Cumhuriyet Mah. 502 Sk. No:1/5", "0555 013 37 19", "", "@likyaguzellikfethiye", "likyaguzelliksalonu.com", "Telefon/iletişim. Online form görünmüyor.", "Tek şube", CUM_TEL, "https://www.likyaguzelliksalonu.com/", gizli=True)

# ---------- B: e-posta yok/gizli (telefon), ya da randevu formu var
B("İstanbul / Bakırköy", "Glitz Beauty Exclusive", "", "0534 386 31 72", "", YOK, "Bulunamadı", "glitzbeautyexclusive.com", "Yalnızca WhatsApp.", "Tek", "https://glitzbeautyexclusive.com/", "E-posta gizli: siteden kontrol edin.")
B("Ankara / Etimesgut", "SN Güzellik ve Bakım Merkezi", "Atakent Mah. 1477. Sk. No:1/8 Elvankent", "0312 260 0 777", "", YOK, "@sn_guzellik", "snguzellikmerkezi.com", "WhatsApp ve telefon.", "2 şube (Etimesgut, Eryaman)", "https://www.snguzellikmerkezi.com/", "E-posta gizli.")
B("Ankara / Etimesgut", "Meltem Yılmaz Bağlıca Güzellik Merkezi", "Bağlıca Bulvarı 1343 Sk. No:2B/6", "0501 350 54 06", "", YOK, "@meltemyilmazbeauty", "baglicaguzellik.com", "Telefon, online form, sosyal medya.", "Tek", "https://baglicaguzellik.com/", "E-posta gizli. Formu deneyin.")
B("Ankara / Çankaya", "Selda Gençer Beauty Center", "Konutkent, 3028 Cd. 8A No:A1", "0533 039 00 76", "", YOK, "Bulunamadı", "seldagencerbeauty.com", "Yalnızca WhatsApp ve telefon.", "Tek", "https://seldagencerbeauty.com/guzellik-merkezi", "E-posta yok/gizli.")
B("Ankara / Çankaya", "Marigold Güzellik Merkezi", "Alacaatlı Mah. 3407. Cad. YaşamKule No:6-A/138", "0533 393 57 18", "marigoldguzellik@gmail.com", ACIK, "@marigoldguzellikmerkezi", "marigoldbeauty.com.tr", "Online randevu formu var (takvim olup olmadığı kontrol edilmeli).", "Tek", "https://marigoldbeauty.com.tr/", "Formu deneyin.")
B("İstanbul / Şişli", "Hilal Beauty Salonu", "Mecidiyeköy Mah. Şehit Ahmet Sk. 28/B Selvi Apt", "0532 660 44 37", "info@hilalbeuatysisli.com", "Adres yazımı şüpheli (beuaty)", "Bulunamadı", "hilalbeautysisli.com", "'Online Randevu' butonu var (takvim olup olmadığı kontrol edilmeli).", "Tek", "https://www.hilalbeautysisli.com/", "E-posta yazımını doğrulayın.")
B("Bursa / Nilüfer", "Kübra Yavuz Güzellik", "Plaza İpek K:3", "0224 453 10 16", "", YOK, "@kubrayavuzguzellik", "bursaciltbakimi.com", "Yalnızca WhatsApp.", "Tek", "https://bursaciltbakimi.com/hakkimizda/", "E-posta gizli.")
B("Bursa", "Azalea Beauty and Aesthetics", "Ahmet Yesevi Mah. Piknik Cad. Neo Flats No:6E Balat", "0224 503 00 04 / 0533 139 59 16", "info@azalea.com.tr", ACIK, "@azaleaesthetic", "azalea.com.tr", "WhatsApp. Randevu yöntemi sitede net değil.", "Tek", "https://azalea.com.tr/", "Göndermeden önce randevu yöntemini kontrol edin.")
B("Antalya / Kepez", "Popüler Kuaför ve Güzellik Salonu", "Çankaya Mah. Barış Manço Bulvarı 217D Masadağı", "0242 237 10 15", "", YOK, "@populer_antalya_guzellik", "populerantalyaguzellik.com.tr", "Telefon.", "Tek", "https://www.populerantalyaguzellik.com.tr/", "E-posta gizli.")
B("Mersin / Yenişehir", "Havva Öztürk Güzellik Merkezi", "Güvenevler Mah. 1932 Sk. Şih Müslüm Apt. No:12/5", "0542 122 34 45", "", YOK, "@havvaozturkguzellikmersin", "mersinbeauty.center", "Telefon ve Instagram.", "Tek", "https://mersinbeauty.center/", "E-posta gizli.")
B("Mersin", "Merlin Premium", "", "0505 343 33 03", "", YOK, "@merlinpremium", "merlinpremium.com", "Yalnızca telefon.", "Tek", "https://www.merlinpremium.com/", "Sitede işletmeye ait e-posta yok.")
B("Diyarbakır", "İrem Güzellik Salonu", "Kayapınar / Bağlar", "0507 580 47 23", "", YOK, "@iremmakeupacademy", "iremguzellik.com.tr", "WhatsApp ve telefon.", "5 şube", "https://iremguzellik.com.tr/hizmetagi/87/baglar.html", "Zincir (5 şube).")
B("Diyarbakır / Bağlar", "Güzellik Atölyesi", "Urfa Yolu, Çeysa-Centropol Plaza B Blok K:4 No:10", "0532 120 31 86", "", YOK, "@ozcanykcguzellikatolyesi", "guzellikatolyesi.net", "WhatsApp ve telefon.", "Tek", "https://guzellikatolyesi.net/", "E-posta gizli.")
B("Diyarbakır / Kayapınar", "Zümrüt Tomak Güzellik Merkezi", "Medya Mah. 176. Sk. Altınsoy 8 Apt altı, Diclekent", "0533 679 77 51", "", YOK, "@zumrut_tomak_guzellik_merkezi", "zumruttomakguzellikmerkezi.com", "WhatsApp ve telefon.", "2 şube", "https://zumruttomakguzellikmerkezi.com/", "E-posta gizli.")
B("Şanlıurfa / Haliliye", "Lila Life Şanlıurfa", "Aldo karşısı, Şair Şevket, 121. Sk.", "0552 456 86 63", "", YOK, "Bulunamadı", "urfalilalife.com", "WhatsApp ve telefon.", "Tek", "https://urfalilalife.com/", "E-posta yok.")
B("Şanlıurfa", "Şanlıurfa Lazer Epilasyon Merkezi", "Merkez", "0542 299 09 83", "", YOK, "@inyaweb", "sanliurfalazerepilasyon.com.tr", "WhatsApp/telefon.", "Tek", "https://www.sanliurfalazerepilasyon.com.tr/", "E-posta gizli.")
B("Denizli / Merkezefendi", "Rena Estetik ve Güzellik Merkezi", "Saltak Cad. Sırakapılar Mah. Yurtiçi Kargo Üzeri No:73", "0552 920 00 08", "", YOK, "@renaguzellik", "renaguzellik.com", "WhatsApp, telefon ve basit iletişim formu.", "Tek", "https://www.renaguzellik.com/", "E-posta gizli.")
B("Muğla / Fethiye", "Gül Estetik ve Güzellik Salonu", "Sadi Pekin Cad. No:4 K:1 D:5", "0252 612 22 18 / WhatsApp 0536 219 73 62", "", YOK, "@gulestetikfethiye", "gulestetikfethiye.com", "WhatsApp ve telefon.", "Tek", "https://www.gulestetikfethiye.com/", "E-posta gizli.")
B("Balıkesir / Burhaniye", "Aysun Bilici Kişisel Bakım Merkezi", "Mahkeme Mah. Katipzade Osmanbey Sk. 9A", "0552 546 36 50", "", YOK, "@aysunbilici_", "aysunbilici.com", "WhatsApp ve telefon.", "Tek", "https://aysunbilici.com/", "E-posta gizli.")
B("Tekirdağ / Çorlu", "Bahar Kayalar Güzellik Merkezi", "Kazımiye Mah. Salih Omurtak Cad. No:130/4", "0543 833 10 70", "", YOK, "@baharkayalarguzellik", "baharkayalar.com", "WhatsApp ve telefon.", "Tek", "https://www.baharkayalar.com/index.html", "E-posta gizli.")
B("Kırıkkale", "TK Güzellik Merkezi", "Ovacık Mah. İzmir Cad. Danacıoğlu İş Merkezi No:6-A", "0555 024 70 71", "", YOK, "@tugbakartn", "tkguzellikmerkezi.com", "WhatsApp ve telefon.", "Tek", "https://tkguzellikmerkezi.com/", "E-posta gizli.")
B("İstanbul / Sancaktepe", "Zümrüt Güzellik Salonu", "", "0530 938 64 49", "", YOK, "@guzellikzumrut", "zumrutguzelliksalonu.com", "Yalnızca WhatsApp/telefon.", "Tek", "https://zumrutguzelliksalonu.com/", "E-posta gizli.")
B("İstanbul / Beylikdüzü", "Şebnem Beauty Studio", "Adnan Kahveci, Alya Residence, Büyükdere Cd. No:2 D:6", "0531 699 44 65", "", YOK, "@sebnembeautystudio", "sebnembeautystudio.com", "WhatsApp ve telefon.", "Tek", "https://sebnembeautystudio.com/hakkimizda", "E-posta gizli.")
B("İstanbul / Esenyurt", "Neslihan Geçmen Kuaför ve Güzellik", "Barbaros Hayrettin Paşa Mah. Newista Rezidans D:17", "0553 861 13 61", "", YOK, "@neslihangecmen_guzellikmerkezi", "neslihangecmenguzellikmerkezi.com", "WhatsApp ve telefon.", "Tek", "https://neslihangecmenguzellikmerkezi.com/", "E-posta gizli.")
B("Ankara", "Dila Sayan Güzellik", "Çankaya / Batıkent / Etlik", "0312 870 04 04", "", YOK, "@dilasayanguzellik", "dilasayan.com", "Telefon.", "3 şube", "https://www.dilasayan.com/", "Küçük zincir. E-posta gizli.")
B("İzmir / Bornova", "Ege Plus Estetik", "Kazım Dirik Mah. Fevzi Çakmak Cd. No:10 K:1", "0533 405 99 06", "", YOK, "@egeplusguzellik", "egeplusguzellik.com", "Telefon/WhatsApp (iletişim formu var).", "Tek", "https://www.egeplusguzellik.com/iletisim/", "E-posta gizli.")
B("Adana / Çukurova", "Güzellik Dünyası", "Turgut Özal Blv. PTT Cad. Ali Yıldırım Apt zemin kat", "0322 213 13 12 / 0530 265 18 85", "", YOK, "@guzellikdunyasiadana", "guzellikdunyasi.com.tr", "İletişim formu; online takvim görülmedi.", "Tek", "https://www.guzellikdunyasi.com.tr/iletisim", "E-posta gizli.")
B("İstanbul / Sultanbeyli", "Şahika Beauty", "", "0530 434 83 49", "", YOK, "Bulunamadı", "sultanbeyliguzellikmerkezi.com.tr", "WhatsApp + online randevu formu (takvim olup olmadığı kontrol edilmeli).", "Tek", "https://sultanbeyliguzellikmerkezi.com.tr/", "E-posta gizli.")
B("İstanbul / Pendik", "Kurtköy Güzellik Merkezi", "Kurtköy Mah. Ankara Cad. No:371 K:1 D:3", "0531 436 93 34", "info@kurtkoyguzellikmerkezi.com", ACIK, "@kurtkoyguzellikmerkezi", "kurtkoyguzellikmerkezi.com", "WhatsApp, telefon ve 'Online Randevu Al' bağlantısı (takvim olup olmadığı kontrol edilmeli).", "Tek", "https://www.kurtkoyguzellikmerkezi.com/hizmet/16/kalici-makyaj", "Formu deneyin.")
B("İstanbul / Pendik", "Pendik Güzellik Merkezi", "Batı Mah. Ankara Cad. No:152", "0850 840 11 41", "info@pendikguzellikmerkezi.com", ACIK, "@pendikguzellikmerkezi", "pendikguzellikmerkezi.com", "Online form, telefon, WhatsApp (takvim olup olmadığı kontrol edilmeli).", "Tek", "https://www.pendikguzellikmerkezi.com/", "Formu deneyin.")
B("Antalya / Muratpaşa", "Tülay Kalmaz Beauty Center", "", "", "", YOK, "", "", "", "", "", "")  # yer tutucu silinecek
R.pop()
B("İstanbul / Beylikdüzü", "Carmine Beauty Center", "", "", "", YOK, "", "", "", "", "", "")
R.pop()

# ---------- C: sayfa açılamadı / doğrulanacak
for sehir, isim, web in [
    ("İstanbul / Avcılar", "Ahenk Güzellik Merkezi", "ahenkguzellikavcilar.com"),
    ("İstanbul / Bakırköy", "Bakırköy Güzellik Merkezi", "bakirkoyguzellik.com.tr"),
    ("İstanbul / Zeytinburnu", "Zeytinburnu Güzellik Merkezi", "zeytinburnuguzellikmerkezi.com"),
    ("İstanbul / Üsküdar", "Esteemar Güzellik Merkezi", "esteemar.com"),
    ("İstanbul / Çekmeköy", "Aysun's Güzellik Salonu", "aysunsguzellikmerkezi.com"),
    ("İstanbul / Ataşehir", "Anik Beauty Center", "anikbeautycenter.net"),
    ("İstanbul / Pendik", "Esthe Novella Pendik", "esthenovella.com"),
    ("İstanbul / Bağcılar", "Gardenya Beauty", "bagcilarguzellikmerkezi.com"),
    ("İstanbul / Fatih", "İFG Güzellik Salonu (site askıda)", "ifgsalon.com"),
    ("İzmir / Buca", "Anatolium VIP Güzellik Merkezi", "anatoliumvip.com"),
    ("İzmir / Konak", "Aymira Koçaklı Konak Yaşam Merkezi", "aymirakocaklikonak.com"),
    ("Antalya / Lara", "Kamer Beauty Center", "kamerbeauty.com"),
    ("Antalya / Lara", "Monoi Beauty", "monoibeauty.com"),
    ("Mersin / Yenişehir", "Mersin Essi Güzellik Merkezi", "mersinessi.com"),
    ("Mersin", "Semiha Aydar Beauty Master", "mersinciltbakimi.com"),
    ("Şanlıurfa / Haliliye", "Deluxe VIP Şanlıurfa", "deluxevipurfa.com"),
    ("Denizli / Pamukkale", "Glory Güzellik Merkezi", "gloryguzellik.com"),
    ("Balıkesir", "Clinix Güzellik Merkezi", "clinix.web.tr"),
    ("Tekirdağ / Çorlu", "Lanour Beauty Center", "lanourbeautycenter.com"),
    ("Hatay / Antakya", "Zerya Masaj ve Spa", "zeryaspa.com"),
    ("Kırıkkale", "Derman Estetik ve Güzellik", "dermanestetik.com"),
    ("Afyonkarahisar", "NK Güzellik Salonu", "nkguzelliksalonu.com"),
    ("Afyonkarahisar", "Peos Güzellik Merkezi", "peosguzellik.com"),
    ("Konya / Karatay", "Özlem Beauty", "ozlembeauty.com.tr"),
    ("Konya / Meram", "Işıl Keçe Güzellik Salonu", "isilkeceguzelliksalonu.com"),
    ("Gaziantep", "Gaziantep Güzellik Merkezi", "gaziantepguzellikmerkezi.com"),
    ("Kayseri", "Siya Beauty", "siyabeauty.com.tr"),
    ("Gaziantep", "Mahinur's Beauty Center (@mahinursbeauty, 0538 593 67 27)", ""),
]:
    add("C", sehir, isim, "", "", "", YOK, "", web, "Sayfa açılamadı (sertifika/bağlantı hatası).", "?", "Doğrulanacak", "", "https://" + web, "Siteyi tarayıcıda elle açıp e-posta ve randevu yöntemine bakın.")

ELENEN = [
    ["ES Viaderm (Avcılar)", "Sitesinde 'Randevu Al' online formu var, e-posta görünmüyor.", "https://esviaderm.com/"],
    ["Derya Akdeniz Güzellik (Çekmeköy)", "Kendi online randevu sistemi var.", "https://www.deryaakdeniz.com/"],
    ["Servet Çetin / Bakırköy Güzellik Merkezi", "Online randevu formu var.", "https://servetcetin.com/"],
    ["Wiens Güzellik Merkezi (Trabzon)", "Online randevu formu var.", "https://wiens.com.tr/"],
    ["Tuğçe Düzsöz Güzellik (Denizli)", "SalonRandevu üzerinden online randevu alıyor.", "https://www.tugceduzsoz.com/"],
    ["EVAPLUS İzmit", "Online randevu formu var.", "https://www.izmitlazerepilasyon.com.tr/"],
    ["Beauty Garden Sakarya", "Online randevu formu var.", "https://www.beautygardensakarya.com/"],
    ["Nouvelle Vie Estetik", "7 şubeli zincir ve online randevu var.", "https://www.nouvellevieestetik.com/"],
    ["Eva Plus Çorlu", "Zincir ve online randevu var.", "https://evapluscorlu.com/"],
    ["Esin Orhan Güzellik (Isparta)", "7 şubeli zincir.", "https://esinorhan.com/"],
    ["His Beauty (Pendik)", "9 şubeli zincir.", "https://hisbeauty.com.tr/"],
    ["Loresima Beauty (Tuzla)", "KolayRandevu üzerinden online randevu alıyor.", "https://www.loresimabeauty.com.tr/"],
    ["Adana Güzellik Merkezi (Seyhan)", "Online randevu formu var.", "https://adanaguzellikmerkezi.com/"],
    ["Tuğçe Naz Güzellik, Dilek Gezer Beauty, Essi Konya", "Online randevu formu veya takvimi var.", "https://tugcenazguzellik.com/en"],
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
