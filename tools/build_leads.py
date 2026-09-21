"""Başakşehir güzellik merkezi aday listesini leads/ klasörüne Excel olarak yazar.

Not: leads/ klasörü .gitignore'dadır, GitHub'a gönderilmez (iş sahiplerinin iletişim bilgileri).
Kullanım: python tools/build_leads.py   (openpyxl gerekir)
"""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

OUT = Path(__file__).resolve().parent.parent / "leads" / "basaksehir-guzellik-adaylar.xlsx"

HEAD = ["Öncelik", "İşletme", "Semt / adres", "Telefon", "E-posta", "Instagram", "Web sitesi",
        "Randevu yöntemi (bulgu)", "Doğrulama", "İlk cümle önerisi (kişiselleştirme)", "Kaynak",
        "Durum", "İlk temas tarihi", "Not"]

# Doğrulama: "Doğrulandı" = işletmenin kendi sayfasından kontrol edildi.
# "Kısmen" = dizin/arama sonucu var, işletmenin kendi sayfası kontrol edilmedi. "Doğrulanacak" = yalnızca isim biliniyor.
ROWS = [
    ["A", "Mediplast Güzellik Merkezi", "Başakşehir Mah., Bulvar İstanbul Evleri G Blok No:2", "0552 650 6000",
     "info@mediplast.com.tr", "@mediplast.guzellik", "mediplast.com.tr",
     "Telefon, WhatsApp veya Instagram. Online randevu formu/takvim yok. Tek şube.", "Doğrulandı",
     "Sitenizde 'hızlı fiyat bilgisi için hemen yazın' diyorsunuz. Bu, gün içinde çok WhatsApp mesajı demek.",
     "https://www.mediplast.com.tr/guzellik-merkezi-basaksehir-iletisim/", "Yeni", "", "E-posta var: ilk e-posta buraya."],
    ["A", "Pınar Bayan Kuaförü ve Güzellik Merkezi", "Güvercintepe Mah., Ahmet Yesevi Cad., Görümlü Sk. 35a", "0532 442 83 89",
     "", "", "pinarbayankuaforu.com.tr",
     "Yalnızca WhatsApp ('Randevu almak için WhatsApp tıklayın'). Online form/takvim yok. Tek şube.", "Doğrulandı",
     "Sitenizde randevu için WhatsApp'a yönlendiriyorsunuz. Mesajlar dağılınca randevular karışabiliyor.",
     "https://pinarbayankuaforu.com.tr/", "Yeni", "", "E-posta yok: önce telefon (iş hattınızdan)."],
    ["B", "Ville Esthetique", "Bahçeşehir 1. Kısım Mh., Ebabil Sk., Defne 3 Villa 12", "0532 111 90 85",
     "", "@villeestetik", "villeesthetique.com",
     "Instagram, Facebook veya telefon. Online randevu sistemi bulunamadı.", "Kısmen",
     "Randevuyu Instagram ve telefondan alıyorsunuz. Müşteri kendisi saat seçebilse işiniz kolaylaşır.",
     "https://www.instagram.com/villeestetik/ ; https://www.alo34.com/firma/ville-esthetique-kuafor-guzellik-ve-estetik-merkezi-bahcesehir",
     "Yeni", "", "Sitesini ve Instagram bio'sunu bir kez kontrol edin (randevu bağlantısı var mı?)."],
    ["B", "Sevinç Beauty", "Bahçeşehir 2. Kısım Mh., Avni Akyol Bul., Loca Sitesi A Blok D:18", "0552 922 82 99",
     "info@sevincbeauty.com", "", "sevincbeauty.com",
     "Doğrulanmadı (sitesinde online randevu olup olmadığına bakılmalı).", "Kısmen",
     "(Sitesine bakıp yazın: randevu nasıl alınıyor?)",
     "https://sevincbeauty.com/tr/iletisim", "Yeni", "", "E-posta var. Göndermeden önce siteyi 2 dakika kontrol edin."],
    ["B", "Başakşehir Beauty", "Kayabaşı Mah., B5 Blok No:29", "0541 547 14 46",
     "info@basaksehirbeauty.com", "", "basaksehirbeauty.com",
     "Basit online form (WhatsApp'a bağlanıyor) + telefon. Gerçek takvim/saat seçimi yok. Tek şube.", "Doğrulandı",
     "Sitenizdeki form randevuyu WhatsApp'a düşürüyor. Müşterinin doğrudan boş saati görmesi mümkün olabilir.",
     "https://basaksehirbeauty.com/", "Yeni", "", "Form var: orta öncelik. E-posta var."],
    ["B", "Aynur Kaya Beauty Center (Nova Rezidans)", "Süleyman Çelebi Cd. No:10, Nova Rezidans 1. Etap", "0541 119 29 16",
     "", "@aynurkayabeautycenter", "aynurkayabeauty.com",
     "Arama sonucuna göre sitede online randevu formu var; takvim olup olmadığı doğrulanmadı. Birden çok sayfa/şube olabilir.", "Kısmen",
     "(Önce sitesindeki randevu formuna bakın.)",
     "https://aynurkayabeauty.com/ (site 403 verdi, doğrudan açamadım)", "Yeni", "", "Düşük-orta öncelik."],
    ["B", "Ayşe Sarı Beauty Center", "Kayaşehir (Kuzey yakası)", "0541 236 91 62",
     "", "@aysesaribeautycenter", "(site bulunamadı)",
     "Instagram/telefon. Web sitesi bulunamadı.", "Kısmen",
     "Instagram'da işletmenizi görüyorum. Web sitesi ve online randevu için ücretsiz bir örnek hazırlayabilirim.",
     "https://www.instagram.com/aysesaribeautycenter/", "Yeni", "", "Site yok adayı. E-posta yok: telefon veya Instagram."],
    ["C", "Sky Güzellik Merkezi", "Bahçeşehir 2. Kısım Mh., Şelale Cad. 15-O Terrace Garden", "", "", "", "skyguzellik.com",
     "Doğrulanmadı.", "Doğrulanacak", "", "https://skyguzellik.com/", "Yeni", "", "Siteyi açıp iletişim ve randevu yöntemine bakın."],
    ["C", "Elif Erol Beauty", "Bahçeşehir", "", "", "", "eliferolbeauty.com",
     "Doğrulanmadı.", "Doğrulanacak", "", "https://eliferolbeauty.com/", "Yeni", "", ""],
    ["C", "ZET Güzel Yaşam Merkezi", "Bahçeşehir", "", "", "", "zetguzelyasam.com",
     "Doğrulanmadı.", "Doğrulanacak", "", "https://www.zetguzelyasam.com/", "Yeni", "", ""],
    ["C", "Cevahir Beauty Bahçeşehir", "Bahçeşehir", "", "", "@cevahirbeautybahcesehir", "",
     "Doğrulanmadı.", "Doğrulanacak", "", "https://www.instagram.com/cevahirbeautybahcesehir/", "Yeni", "", ""],
    ["C", "Bahçeşehir Lazer Epilasyon Cilt Bakımı Hydrafacial", "Bahçeşehir 1. Kısım Mh., Aşık Mahsuni Şerif Cad.", "0541 906 02 43", "", "", "",
     "Doğrulanmadı.", "Doğrulanacak", "", "https://yandex.com.tr/maps/org/bahcesehir_lazer_epilasyon_cilt_bakimi_hydrafacial_zayiflama_ve_masaj/88535096148/",
     "Yeni", "", ""],
    ["C", "Movın Beauty", "Bahçeşehir 1. Kısım Mh., Fırat Cad. No:2/1", "", "", "", "",
     "Doğrulanmadı (arama sonucu çıkmadı).", "Doğrulanacak", "", "https://mekan.com/guzellik/c/istanbul/i/basaksehir", "Yeni", "", ""],
]

ELENEN = [
    ["Reem Güzellik Merkezi", "Kendi online randevu sistemi zaten var (randevu.reemsalon.com).", "https://www.randevu.reemsalon.com/"],
    ["Esse Life Başakşehir", "Zincir/franchise, karar merkezi başka.", "https://basaksehir.esselife.com.tr/"],
    ["Epilife Güzellik Salonu", "Çok şubeli görünüyor.", "https://www.epilifeguzellik.com/basaksehir-guzellik-salonu/"],
    ["Kübra Toksoy Güzellik", "Dizinde 3 şube olarak listeleniyor.", "https://mekan.com/guzellik/c/istanbul/i/basaksehir"],
    ["Daphne Lazer", "Birçok şubesi olan zincir.", "https://daphnelazer.com/"],
    ["De Milano Beauty", "De Milano Güzellik Merkezleri Ltd. çatısı, çok şubeli görünüyor.", "https://milanobeauty.com.tr/"],
    ["Neslim Güngen Bahçeşehir", "Franchise/zincir.", "https://www.instagram.com/neslimgungenbahcesehir/"],
    ["DYM Güzellik Merkezi (Kayaşehir AVM)", "KolayRandevu üzerinde online randevu alıyor, AVM içinde.", "https://www.kolayrandevu.com/isletme/dym-guzellik-merkezi-kayasehir-avm"],
    ["Bia Hair Point", "2 şubeli kuaför zinciri.", "https://mekan.com/guzellik/c/istanbul/i/basaksehir"],
]

KULLANIM = [
    "Bu liste, yalnızca işletmelerin kendi yayımladığı veya herkese açık dizinlerde yer alan iletişim bilgilerinden derlendi.",
    "",
    "ÖNCELİK: A = doğrulandı, online randevu sistemi yok. B = kısmen doğrulandı, göndermeden önce 2-5 dakika kontrol edin. C = yalnızca isim, doğrulanmadı.",
    "DOĞRULAMA: 'Doğrulandı' işletmenin kendi sayfasından bakıldığı anlamına gelir. Diğerlerinde bilgi eksik olabilir.",
    "",
    "GÖNDERMEDEN ÖNCE (5 dakika kontrol):",
    "  1) Web sitesi veya Instagram bio'sunda 'randevu al' düğmesi/takvim bağlantısı var mı? Varsa satırı 'Elenen' yapın.",
    "  2) Zincir mi? Birden fazla şubesi varsa kararı tek kişi vermeyebilir.",
    "  3) E-posta adresi işletmenin kendi sayfasında mı yazıyor? Yoksa e-posta göndermeyin, telefon veya Instagram'ı deneyin.",
    "",
    "YASAL NOTLAR (hukuki teyit alın):",
    "  - Esnaf ve tacire ticari ileti önceden izin olmadan gönderilebilir, ama her mesajda kimliğiniz (unvan, adres) ve kolay bir çıkma seçeneği olmalı.",
    "  - Çıkma isteğinden sonra 3 iş günü içinde göndermeyi bırakın. Çıkanları 'Çıkanlar' sekmesine yazın ve bir daha yazmayın.",
    "  - Şirket unvanınız hazır olmadan toplu e-posta göndermeyin.",
    "  - Günde en fazla 15-20 e-posta gönderin, ilk gönderilerde daha az.",
    "  - Bu dosyayı GitHub'a yüklemeyin. leads/ klasörü bu yüzden .gitignore'da.",
]


def style(ws, widths):
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
    ws.freeze_panes = "C2"
    ws.row_dimensions[1].height = 32


wb = Workbook()
ws = wb.active
ws.title = "Adaylar"
ws.append(HEAD)
for r in ROWS:
    ws.append(r)
style(ws, [8, 30, 34, 16, 26, 24, 22, 44, 14, 50, 50, 10, 14, 34])
fills = {"A": "DCFCE7", "B": "FEF9C3", "C": "F3F4F6"}
for row in ws.iter_rows(min_row=2):
    row[0].fill = PatternFill("solid", fgColor=fills[row[0].value])
    row[0].font = Font(bold=True)

ws2 = wb.create_sheet("Elenenler")
ws2.append(["İşletme", "Neden elendi", "Kaynak"])
for r in ELENEN:
    ws2.append(r)
style(ws2, [38, 60, 60])
ws2.freeze_panes = "A2"

ws3 = wb.create_sheet("Çıkanlar")
ws3.append(["İşletme / e-posta / telefon", "Çıkma isteği tarihi", "Nasıl geldi (yanıt, telefon...)"])
style(ws3, [44, 22, 40])
ws3.freeze_panes = "A2"

ws4 = wb.create_sheet("Nasıl kullanılır")
ws4.append(["Kullanım notları"])
for line in KULLANIM:
    ws4.append([line])
ws4.column_dimensions["A"].width = 140
for row in ws4.iter_rows(min_row=2):
    row[0].alignment = Alignment(wrap_text=True, vertical="top")
ws4["A1"].font = Font(bold=True)

OUT.parent.mkdir(exist_ok=True)
wb.save(OUT)
a = sum(r[0] == "A" for r in ROWS); b = sum(r[0] == "B" for r in ROWS); c = sum(r[0] == "C" for r in ROWS)
print(f"Yazıldı: {OUT}\nA={a}  B={b}  C={c}  toplam={len(ROWS)}  elenen={len(ELENEN)}")
print("E-postası olan aday:", sum(1 for r in ROWS if r[4]))
