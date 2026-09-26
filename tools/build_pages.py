"""Ana sayfa ve hizmet sayfalarını, TR (kök) ve EN (/en/) olarak üretir.

Kullanım:  python3 tools/build_pages.py
Metinleri değiştirmek için bu dosyadaki UI / SERVICES / PROBLEMS / DEMOS / INDEX_FAQ
sözlüklerini düzenleyin, sonra çalıştırın.

Yeni bir dil eklemek için (ör. "de"):
  1. LANGS listesine "de" ekleyin, HTML_LANG / OG_LOCALE / LANG_LABEL'e karşılığını yazın.
  2. UI, SERVICES, PROBLEMS, DEMOS, INDEX_FAQ sözlüklerindeki her "tr"/"en" anahtarının
     yanına "de" anahtarıyla çeviriyi ekleyin (yapı birebir aynı kalmalı).
  3. Script'i çalıştırın; /de/ altında otomatik üretilir.
"""
import hashlib
import json
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://dijicozum.com"
BRAND = "DijiÇözüm"
EMAIL = "merhaba@dijicozum.com"
TODAY = "2026-09-20"

LANGS = ["tr", "en"]
DEFAULT_LANG = "tr"
HTML_LANG = {"tr": "tr", "en": "en"}
OG_LOCALE = {"tr": "tr_TR", "en": "en_US"}
LANG_LABEL = {"tr": "TR", "en": "EN"}
# Bu yollar dile göre öneklenmez (paylaşılan / henüz çevrilmemiş sayfalar)
NO_PREFIX = ("/demo/", "/assets/", "/gizlilik", "mailto:", "http")


def L(path, lang):
    """Bir site-içi yolu dile göre önekler (TR = kök, diğerleri /xx/...)."""
    if lang == DEFAULT_LANG or path.startswith(NO_PREFIX) or path.startswith("#"):
        return path
    if path == "/":
        return f"/{lang}/"
    return f"/{lang}{path}"


def _ver(*names):
    h = hashlib.md5()
    for n in names:
        h.update((ROOT / "assets" / n).read_bytes())
    return h.hexdigest()[:8]


V = _ver("style.css", "config.js", "consent.js")  # önbellek kırıcı: dosya değişince adres değişir

ICON_PATHS = {
    "randevu": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/>',
    "siparis": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18M16 10a4 4 0 0 1-8 0"/>',
    "web": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 21h8"/>',
    "asistan": '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
    "uygulama": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    "oneri": '<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.9c.6.4 1 1.1 1 1.9v.2h6v-.2c0-.8.4-1.5 1-1.9A7 7 0 0 0 12 2z"/>',
}


def icon(name, size=26):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON_PATHS[name]}</svg>'


WA_NUMBER = "905451579311"
WA_ICON = (
    '<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.39 1.26 4.81L2 22l5.42-1.36a9.9 9.9 0 0 0 4.62 1.14h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.86 9.86 0 0 0 12.04 2zm5.8 14.02c-.24.68-1.4 1.32-1.93 1.4-.5.08-1.11.11-1.79-.11-.41-.13-.94-.31-1.62-.6-2.85-1.23-4.71-4.1-4.85-4.29-.14-.19-1.16-1.54-1.16-2.94s.73-2.09.99-2.37c.26-.29.56-.36.75-.36l.53.01c.17.01.4-.06.62.48.24.58.81 2 .88 2.14.07.14.12.31.02.5-.09.19-.14.31-.28.48-.14.17-.29.37-.42.5-.14.14-.28.29-.12.57.16.29.71 1.19 1.53 1.93 1.05.95 1.94 1.25 2.22 1.39.28.14.45.12.62-.07.17-.19.71-.83.9-1.12.19-.28.38-.24.63-.14.26.09 1.65.79 1.93.93.28.14.47.21.53.33.07.12.07.68-.17 1.36z"/>'
    '</svg>'
)

# ---------------------------------------------------------------- ortak arayüz metinleri
UI = {
    "tr": dict(
        nav=[("/randevu-sistemi", "Randevu"), ("/siparis-sistemi", "Sipariş"), ("/web-sitesi", "Web sitesi"),
             ("/yapay-zeka-asistani", "Yapay zeka"), ("/#ornekler", "Örnekler")],
        header_cta="Ücretsiz demonu iste", logo_aria=f"{BRAND} ana sayfa", menu_aria="Ana menü", menu_toggle_aria="Menüyü aç",
        footer_tagline="Küçük işletmeler için randevu, sipariş, web sitesi ve yapay zeka çözümleri.",
        footer_services_h="Hizmetler", footer_other_h="Diğer", footer_examples="Canlı örnekler", footer_faq="Sık sorulanlar",
        footer_contact="İletişim", footer_privacy="Gizlilik ve KVKK", footer_cookie="Çerez tercihleri",
        copyright="© 2026 Tüm hakları saklıdır.",
        eyebrow="Küçük işletmeler için", hero_h1='İşletmenizin dijital <em>tek adresi</em>.',
        hero_lead="Online randevu, sipariş, web sitesi ve yapay zeka asistanı. Her biri ayrı ayrı alınır. İsterseniz birlikte de kurarız.",
        hero_cta1="Ücretsiz demonu iste", hero_cta2="Hizmetleri gör",
        hero_points=["Önce örnek, sonra karar", "Ziyaret gerekmez", "İngilizce destek de mümkün"],
        tiles=[
            ("randevu", "/randevu-sistemi", "Randevu sistemi", "Müşteri internetten saat seçer.", "Tek başına alınır"),
            ("siparis", "/siparis-sistemi", "Sipariş sistemi", "QR menü ve online sipariş.", "Tek başına alınır"),
            ("web", "/web-sitesi", "Web sitesi", "Telefonda düzgün açılır, Google'da bulunur.", "Tek başına alınır"),
            ("asistan", "/yapay-zeka-asistani", "Yapay zeka asistanı", "Müşteri sorularını 7/24 cevaplar.", "Tek başına alınır"),
            ("uygulama", "/demo/uygulama", "Mobil uygulama", "Randevu, sipariş ya da özel bir işiniz için telefon uygulaması.", "Talep üzerine"),
            ("oneri", "#iletisim", "Birlikte karar verelim", "İşinizi kısaca anlatın, size en uygun çözümü önerelim.", "Hemen yazın"),
        ],
        hizmetler_h2="Bunlardan biri size tanıdık geliyor mu?", hizmetler_lead="Her biri ayrı bir hizmet. Size lazım olana tıklayın.",
        nasil_h2="Nasıl çalışıyor? Üç adım.",
        steps3=[("Bize yazın", "Aşağıdaki formu doldurun. İşinizi bir iki cümleyle anlatın."),
                ("Örneğinizi hazırlayalım", "Size uygun çalışan bir örnek hazırlayıp gönderiyoruz. Ücretsiz."),
                ("Beğenirseniz başlarız", "Fiyatı ve süreyi yazılı olarak netleştiririz. Beğenmezseniz bir şey ödemezsiniz.")],
        ornekler_h2="Almadan önce deneyin", ornekler_lead="Aşağıdaki örneklerin hepsi çalışıyor. Tıklayıp deneyin. Örnek işletmeler kurgusaldır.",
        demo_try="Dene",
        neden_h2="Neden bizimle çalışmalısınız?",
        neden_cards=[("Sade ve Türkçe", "Teknik kelime kullanmayız. Ne aldığınızı anlarsınız."),
                     ("İster biri, ister hepsi", "Sadece ihtiyacınız olanı alırsınız. Birkaçını isterseniz birlikte kurarız. Muhatabınız hep aynı kişi olur."),
                     ("Önce görürsünüz", "Ödeme yapmadan çalışan örneği denersiniz."),
                     ("Baştan yazılı fiyat", "Ne yapılacağı ve ne kadar tutacağı önceden yazılı olur.")],
        sss_h2="Sık sorulanlar",
        iletisim_h2="Ücretsiz demonu iste", iletisim_lead="Adınızı ve telefonunuzu yazın. Size geri dönelim.",
        iletisim_bullets=["Genellikle bir iş günü içinde dönüş yaparız.", "Demo ücretsizdir, bir şey satın almak zorunda değilsiniz.", "Yazmak isterseniz: "],
        f_ad="Adınız", f_tel="Telefon", f_tel_ph="05xx xxx xx xx", f_email="E-posta (isteğe bağlı)",
        f_legend="Ne istiyorsunuz?", f_legend_hint="(birden fazla seçebilirsiniz)",
        f_opts=["Randevu sistemi", "Sipariş ve QR menü", "Web sitesi", "Yapay zeka asistanı", "Mobil uygulama", "Birlikte karar verelim"],
        f_mesaj="Kısaca işinizi anlatın (isteğe bağlı)", f_mesaj_ph="Örn. Kuaförüm var, randevuları telefonla alıyorum.",
        f_submit="Demomu iste", f_sending="Gönderiliyor…", f_status="Bilgileriniz yalnızca size dönüş yapmak için kullanılır. ",
        f_success_title="Talebiniz bize ulaştı", f_success_text="En kısa sürede size dönüş yapacağız. Teşekkürler!",
        f_fail="Gönderilemedi. Lütfen tekrar deneyin ya da ", f_fail_end=" adresine yazın.",
        err_name="Lütfen adınızı yazın.", err_contact="Size ulaşabilmemiz için telefon veya e-posta yazın.",
        err_phone="Telefon numarası eksik görünüyor. 05xx ile başlayan 11 haneyi yazın.", err_email="E-posta adresi hatalı görünüyor.",
        breadcrumb_home="Ana sayfa", sec_how_h2="Nasıl çalışıyor?", sec_faq_h2="Sık sorulanlar",
        sec_related_h2="Diğer çözümlerimiz", sec_related_lead="Her biri ayrı ayrı alınabilir. İsterseniz birlikte de kurarız.",
        final_cta_h2="Ücretsiz demonuzu hazırlayalım", final_cta_text="Formu doldurun, size özel çalışan bir örnek gönderelim.",
        try_btn="Örneği dene",
        wa_status=f"{BRAND} · genelde hemen yanıtlar", wa_greeting="Merhaba 👋<br>Size nasıl yardımcı olabiliriz?",
        wa_toggle_aria="WhatsApp'tan yazın", wa_close_aria="Kapat", wa_send_aria="Gönder",
        wa_text="Merhaba, web sitenizden yazıyorum.",
    ),
    "en": dict(
        nav=[("/randevu-sistemi", "Booking"), ("/siparis-sistemi", "Ordering"), ("/web-sitesi", "Website"),
             ("/yapay-zeka-asistani", "AI assistant"), ("/#ornekler", "Examples")],
        header_cta="Get your free demo", logo_aria=f"{BRAND} home", menu_aria="Main menu", menu_toggle_aria="Open menu",
        footer_tagline="Booking, ordering, websites and AI tools for small businesses.",
        footer_services_h="Services", footer_other_h="Other", footer_examples="Live examples", footer_faq="FAQ",
        footer_contact="Contact", footer_privacy="Privacy & KVKK (TR)", footer_cookie="Cookie settings",
        copyright="© 2026 All rights reserved.",
        eyebrow="For small businesses", hero_h1="Your business's <em>one digital address</em>.",
        hero_lead="Online booking, ordering, a website and an AI assistant. Each one stands on its own. Want them together? We can do that too.",
        hero_cta1="Get your free demo", hero_cta2="See services",
        hero_points=["See it first, decide later", "No visit required", "English-speaking support"],
        tiles=[
            ("randevu", "/randevu-sistemi", "Booking system", "Customers pick a time online.", "Works on its own"),
            ("siparis", "/siparis-sistemi", "Ordering system", "QR menu and online ordering.", "Works on its own"),
            ("web", "/web-sitesi", "Website", "Looks right on phones, easy to find on Google.", "Works on its own"),
            ("asistan", "/yapay-zeka-asistani", "AI assistant", "Answers customer questions, 24/7.", "Works on its own"),
            ("uygulama", "/demo/uygulama", "Mobile app", "A phone app for booking, ordering, or your own specific need.", "On request"),
            ("oneri", "#iletisim", "Let's decide together", "Tell us briefly about your business, we'll suggest what fits.", "Message us"),
        ],
        hizmetler_h2="Does one of these sound familiar?", hizmetler_lead="Each is a separate service. Click the one you need.",
        nasil_h2="How it works. Three steps.",
        steps3=[("Message us", "Fill out the form below. Tell us about your business in a sentence or two."),
                ("We prepare your example", "We put together a working example made for your business. Free."),
                ("Like it? We start", "We agree on price and timeline in writing. If you don't like it, you pay nothing.")],
        ornekler_h2="Try before you buy", ornekler_lead="Every example below is fully working. Click and try it. The businesses shown are fictional.",
        demo_try="Try it",
        neden_h2="Why work with us?",
        neden_cards=[("Simple, no jargon", "We don't use technical terms. You'll understand exactly what you're getting."),
                     ("One or all of them", "Get only what you need. Want a few together? We'll set those up too. You'll always talk to the same person."),
                     ("See it before you decide", "Try the working example before you pay anything."),
                     ("Price in writing, upfront", "What we'll build and what it costs is agreed in writing beforehand.")],
        sss_h2="Frequently asked questions",
        iletisim_h2="Get your free demo", iletisim_lead="Leave your name and phone number. We'll get back to you.",
        iletisim_bullets=["We usually reply within one business day.", "The demo is free — you're not committing to buy anything.", "Prefer email? "],
        f_ad="Your name", f_tel="Phone", f_tel_ph="05xx xxx xx xx", f_email="Email (optional)",
        f_legend="What do you need?", f_legend_hint="(you can select more than one)",
        f_opts=["Booking system", "Ordering & QR menu", "Website", "AI assistant", "Mobile app", "Let's decide together"],
        f_mesaj="Briefly describe your business (optional)", f_mesaj_ph="E.g. I run a hair salon, I currently take bookings by phone.",
        f_submit="Request my demo", f_sending="Sending…", f_status="Your information is only used to get back to you. ",
        f_success_title="We've got your request", f_success_text="We'll get back to you soon. Thanks!",
        f_fail="Couldn't send. Please try again or email us at ", f_fail_end=".",
        err_name="Please enter your name.", err_contact="Leave a phone number or email so we can reach you.",
        err_phone="The phone number looks incomplete. Enter the 10-11 digit number.", err_email="That email address doesn't look right.",
        breadcrumb_home="Home", sec_how_h2="How it works?", sec_faq_h2="Frequently asked questions",
        sec_related_h2="Our other solutions", sec_related_lead="Each one can be bought on its own. Want them together? We can set those up too.",
        final_cta_h2="Let's prepare your free demo", final_cta_text="Fill out the form, we'll send you a working example made for you.",
        try_btn="Try the example",
        wa_status=f"{BRAND} · usually replies quickly", wa_greeting="Hi 👋<br>How can we help?",
        wa_toggle_aria="Chat on WhatsApp", wa_close_aria="Close", wa_send_aria="Send",
        wa_text="Hello, I'm messaging from your website.",
    ),
}

INDEX_FAQ = {
    "tr": [
        ("Demo gerçekten ücretsiz mi?", "Evet. İşinizi anlattıktan sonra size özel çalışan bir örnek hazırlıyoruz. Beğenmezseniz hiçbir şey ödemezsiniz."),
        ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra, size yazılı ve net bir fiyat veririz."),
        ("Ne kadar sürede hazır olur?", "Basit bir site veya randevu sistemi genellikle birkaç haftada hazır olur. Telefon uygulaması daha uzun sürer. Süreyi teklifte yazarız."),
        ("Bilgisayardan anlamıyorum, kullanabilir miyim?", "Evet. Kurulumu biz yaparız. Nasıl kullanacağınızı kısa bir videoyla ve gerekirse yazılı olarak anlatırız."),
        ("Site ve alan adı kimin olur?", "Sizin adınıza açarız. Bizimle çalışmayı bıraksanız bile sizde kalır."),
        ("Müşteri bilgileri güvende mi?", "Bilgiler KVKK'ya uygun toplanır ve aydınlatma metni eklenir. Yapay zeka asistanı yalnızca sizin verdiğiniz bilgilere göre cevap verir."),
    ],
    "en": [
        ("Is the demo really free?", "Yes. After you tell us about your business, we prepare a working example made for you. If you don't like it, you pay nothing."),
        ("How much does it cost?", "It depends on the scope. Once you've seen the example, we give you a clear price in writing."),
        ("How long does it take?", "A simple site or booking system is usually ready within a few weeks. A phone app takes longer. We put the timeline in the proposal."),
        ("I'm not good with computers, can I still use it?", "Yes. We handle the setup. We'll show you how to use it with a short video and, if needed, written instructions."),
        ("Who owns the site and domain?", "We register everything in your name. It stays yours even if you stop working with us."),
        ("Is customer data safe?", "Data is collected in line with Turkey's KVKK data protection law, with a privacy notice. The AI assistant only answers using the information you provide."),
    ],
}

PROBLEMS = {
    "tr": [
        ("Telefon sürekli çalıyor. Randevu yazmaktan yoruldum.", "Müşteri kendisi internetten randevu alır. Siz sadece takvime bakarsınız.", "/randevu-sistemi", "Online randevu sistemi"),
        ("Yemek sitelerine çok komisyon veriyorum.", "Kendi sipariş sayfanız olur. Siparişler komisyon ödemeden size gelir.", "/siparis-sistemi", "Sipariş ve QR menü"),
        ("Müşteriler hep aynı şeyleri soruyor.", "Asistan fiyat, saat ve adres sorularını 7/24 sizin yerinize cevaplar.", "/yapay-zeka-asistani", "Yapay zeka asistanı"),
        ("İnternette bulunmuyorum.", "Telefonda düzgün açılan, Google'da bulunan bir siteniz olur.", "/web-sitesi", "Web sitesi"),
    ],
    "en": [
        ("The phone won't stop ringing. I'm tired of writing down bookings.", "Customers book online themselves. You just check the calendar.", "/randevu-sistemi", "Online booking system"),
        ("I'm paying too much commission to food delivery apps.", "Get your own ordering page. Orders reach you with no commission.", "/siparis-sistemi", "Ordering & QR menu"),
        ("Customers keep asking the same questions.", "The assistant answers price, hours and location questions for you, 24/7.", "/yapay-zeka-asistani", "AI assistant"),
        ("I'm not online.", "Get a website that works on phones and shows up on Google.", "/web-sitesi", "Website"),
    ],
}

DEMOS = {
    "tr": [
        ("randevu", "Randevu", "Kuaför randevu sistemi", "Müşteri saati seçer. Randevu hemen sizin panelinize düşer.", "/demo/randevu"),
        ("siparis", "Sipariş", "Restoran sipariş sistemi", "Masadan QR okutulur, sipariş mutfak ekranına düşer.", "/demo/siparis"),
        ("asistan", "Yapay zeka", "Müşteri asistanı", "Fiyat ve saat sorularını cevaplar, randevu isteğini toplar.", "/demo/asistan"),
        ("uygulama", "Telefon uygulaması", "Spor salonu uygulaması", "Ders programı, QR kart ve bildirimler.", "/demo/uygulama"),
        ("web", "Web sitesi", "Kurumsal web sitesi", "Telefonda ve bilgisayarda düzgün açılan bir site.", "/demo/kurumsal"),
    ],
    "en": [
        ("randevu", "Booking", "Hairdresser booking system", "Customer picks a time. The booking lands in your panel right away.", "/demo/randevu"),
        ("siparis", "Ordering", "Restaurant ordering system", "Scan the QR code at the table, the order lands on the kitchen screen.", "/demo/siparis"),
        ("asistan", "AI", "Customer assistant", "Answers price and hours questions, collects booking requests.", "/demo/asistan"),
        ("uygulama", "Phone app", "Gym app", "Class schedule, QR card and notifications.", "/demo/uygulama"),
        ("web", "Website", "Corporate website", "A site that looks right on phone and desktop.", "/demo/kurumsal"),
    ],
}


def wa_widget(lang):
    u = UI[lang]
    return f'''<div class="wa-widget">
  <div class="wa-panel" id="wa-panel" hidden>
    <div class="wa-panel-head">
      <img src="/assets/logo/icon.svg" alt="" class="wa-panel-avatar">
      <div><b>İlhan Akkuş</b><span>{u["wa_status"]}</span></div>
      <button type="button" class="wa-panel-close" id="wa-close" aria-label="{u["wa_close_aria"]}">&times;</button>
    </div>
    <div class="wa-panel-body"><div class="wa-bubble">{u["wa_greeting"]}</div></div>
    <form class="wa-panel-form" id="wa-form">
      <textarea id="wa-text" aria-label="{u["wa_send_aria"]}">{u["wa_text"]}</textarea>
      <button type="submit" class="wa-send" aria-label="{u["wa_send_aria"]}">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 20l18-8L3 4v6l12 2-12 2z"/></svg>
      </button>
    </form>
  </div>
  <button type="button" class="wa-float" id="wa-toggle" aria-label="{u["wa_toggle_aria"]}">{WA_ICON}</button>
</div>
<script>(function(){{
  var btn=document.getElementById('wa-toggle'),panel=document.getElementById('wa-panel'),
      closeBtn=document.getElementById('wa-close'),form=document.getElementById('wa-form'),text=document.getElementById('wa-text');
  function open(){{panel.hidden=false;text.focus();text.select();}}
  function close(){{panel.hidden=true;}}
  btn.addEventListener('click',function(){{panel.hidden?open():close();}});
  closeBtn.addEventListener('click',close);
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
  document.addEventListener('click',function(e){{if(!panel.hidden&&!panel.contains(e.target)&&!btn.contains(e.target))close();}});
  text.addEventListener('keydown',function(e){{if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();form.requestSubmit();}}}});
  form.addEventListener('submit',function(e){{
    e.preventDefault();
    var msg=text.value.trim()||{u["wa_text"]!r};
    if(window.dcTrack)dcTrack('whatsapp_click',{{page:location.pathname}});
    var mobil=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
    var url=mobil?'https://wa.me/{WA_NUMBER}?text=':'https://web.whatsapp.com/send?phone={WA_NUMBER}&text=';
    location.href=url+encodeURIComponent(msg);
  }});
}})();</script>'''


def lang_switcher(lang, page_key):
    """page_key: "" (ana sayfa) ya da hizmet slug'ı. Yalnızca çevrilen sayfalarda gösterilir."""
    links = []
    for lg in LANGS:
        path = "/" if page_key == "" else f"/{page_key}"
        href = L(path, lg)
        cls = ' class="on"' if lg == lang else ""
        links.append(f'<a href="{href}"{cls}>{LANG_LABEL[lg]}</a>')
    return f'<div class="lang-switch">{"".join(links)}</div>'


def header(lang, page_key=""):
    u = UI[lang]
    links = "".join(f'<a href="{L(h, lang)}">{t}</a>' for h, t in u["nav"])
    return f'''<header class="nav">
  <div class="wrap nav-in">
    <a href="{L("/", lang)}" class="logo" aria-label="{u["logo_aria"]}"><img src="/assets/logo/logo-a.svg" alt="{BRAND}" width="155" height="34"></a>
    <nav class="nav-links" id="menu" aria-label="{u["menu_aria"]}">{links}</nav>
    {lang_switcher(lang, page_key)}
    <a href="{L("/#iletisim", lang)}" class="btn btn-primary btn-sm">{u["header_cta"]}</a>
    <button class="nav-toggle" aria-label="{u["menu_toggle_aria"]}" onclick="document.getElementById('menu').classList.toggle('open')">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>'''


def footer(lang):
    u = UI[lang]
    return f'''<footer>
  <div class="wrap foot-cols">
    <div>
      <img src="/assets/logo/logo-c.svg" alt="dijiçözüm" width="110" height="31" style="margin-bottom:8px"><br>
      {u["footer_tagline"]}<br>
      <a href="mailto:{EMAIL}" style="text-decoration:underline">{EMAIL}</a><br>
      <span style="display:block;margin-top:8px">{u["copyright"]}</span>
    </div>
    <div><h4>{u["footer_services_h"]}</h4>
      <a href="{L("/randevu-sistemi", lang)}">{SERVICES[lang]["randevu-sistemi"]["crumb"]}</a>
      <a href="{L("/siparis-sistemi", lang)}">{SERVICES[lang]["siparis-sistemi"]["crumb"]}</a>
      <a href="{L("/web-sitesi", lang)}">{SERVICES[lang]["web-sitesi"]["crumb"]}</a>
      <a href="{L("/yapay-zeka-asistani", lang)}">{SERVICES[lang]["yapay-zeka-asistani"]["crumb"]}</a>
    </div>
    <div><h4>{u["footer_other_h"]}</h4>
      <a href="{L("/#ornekler", lang)}">{u["footer_examples"]}</a>
      <a href="{L("/#sss", lang)}">{u["footer_faq"]}</a>
      <a href="{L("/#iletisim", lang)}">{u["footer_contact"]}</a>
      <a href="/gizlilik">{u["footer_privacy"]}</a>
      <a href="#" data-cookie-settings>{u["footer_cookie"]}</a>
    </div>
  </div>
</footer>'''


def faq_html(faqs):
    return "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faqs)


def faq_ld(faqs):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + "/",
    "logo": SITE + "/assets/logo/png/icon-512.png", "email": EMAIL,
    "description": "Küçük işletmeler için online randevu, sipariş, web sitesi ve yapay zeka asistanı çözümleri.",
    "areaServed": {"@type": "Country", "name": "Türkiye"},
}


def head(lang, title, desc, page_key, ld, extra=""):
    """page_key: "" için "/", aksi halde hizmet slug'ı (örn. "randevu-sistemi")."""
    path = "/" if page_key == "" else f"/{page_key}"
    url = SITE + L(path, lang)
    ld_tags = "\n  ".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    alt_tags = "\n  ".join(
        f'<link rel="alternate" hreflang="{HTML_LANG[lg]}" href="{SITE + L(path, lg)}">' for lg in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{SITE + L(path, DEFAULT_LANG)}">'
    return f'''<!DOCTYPE html>
<html lang="{HTML_LANG[lang]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{url}">
  {alt_tags}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="{OG_LOCALE[lang]}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(desc)}">
  <meta name="twitter:image" content="{SITE}/assets/og-image.png">
  <link rel="icon" href="/assets/logo/icon.svg" type="image/svg+xml">
  <link rel="icon" href="/assets/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <meta name="theme-color" content="#ffffff">
  <meta name="google-site-verification" content="fjGLZyssRHF7Xc6WIzQY9lM_7SGIBw8FrjnkJLxSB9w">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap&subset=latin-ext" rel="stylesheet">
  <link rel="stylesheet" href="/assets/style.css?v={V}">
  {ld_tags}
  <script src="/assets/consent.js?v={V}" defer></script>
{extra}</head>
<body>
'''


MENU_JS = "document.querySelectorAll('#menu a').forEach(a=>a.addEventListener('click',()=>document.getElementById('menu').classList.remove('open')));"

# ---------------------------------------------------------------- hizmet sayfaları içeriği
SERVICES = {
    "tr": {
        "randevu-sistemi": {
            "title": "Online Randevu Sistemi Kurulumu | DijiÇözüm",
            "desc": "Kuaför, güzellik merkezi, veteriner ve danışmanlar için online randevu sistemi. Müşteri kendisi randevu alsın, telefon trafiği azalsın. Ücretsiz demo.",
            "crumb": "Online randevu sistemi", "h1": "Online randevu sistemi: müşteriniz kendisi randevu alsın",
            "lead": "Telefonda randevu yazmak zaman alır. Online randevu sistemiyle müşteriniz internetten saati seçer. Siz sadece takvime bakarsınız.",
            "service": "Online randevu sistemi kurulumu", "for_h": "Kimler için uygun?",
            "for": ["Kuaför ve berberler", "Güzellik ve bakım merkezleri", "Veteriner ve diyetisyenler", "Danışmanlar, kurslar ve atölyeler"],
            "ben_h": "Size ne kazandırır?",
            "ben": [("Telefon azalır", "Müşteri randevuyu kendisi alır. Telefona ve mesajlara harcadığınız zaman kısalır."),
                    ("Boş saatler dolar", "Müşteri gece de randevu alabilir. İşletmeniz kapalıyken bile takvim çalışır."),
                    ("Unutan müşteri azalır", "İsterseniz randevudan önce hatırlatma mesajı gider. Mesaj ücreti ayrıca yansıtılır."),
                    ("Personel ve hizmete göre takvim", "Her çalışanın ve her hizmetin süresini ayrı ayrı ayarlarsınız."),
                    ("Kolay yönetim paneli", "Randevuları görürsünüz, iptal edersiniz, gün sonu özetine bakarsınız.")],
            "steps": [("Hizmetlerinizi yazın", "Hizmet adlarını, sürelerini ve çalışma saatlerinizi bize gönderin."),
                      ("Sayfanızı hazırlayalım", "Logo ve renklerinizle randevu sayfanızı hazırlayıp size gösteririz."),
                      ("Yayına alalım", "Beğenirseniz yayına alırız. Bağlantıyı Instagram'a ve Google'a koyarsınız.")],
            "demo": ("/demo/randevu", "Kuaför randevu örneğini deneyin"),
            "demo_note": "Örnekte bir randevu alın, sonra \"İşletme paneli\" sekmesinde randevunuzu görün.",
            "faq": [("Müşterinin üye olması gerekir mi?", "Hayır. Müşterinin adını ve telefonunu yazması yeterlidir."),
                    ("Randevuları nasıl görürüm?", "İşletme panelinden görürsünüz. İsterseniz yeni randevu geldiğinde e-posta ile de haber veririz."),
                    ("Kendi web sitemde kullanabilir miyim?", "Evet. Randevu sayfası kendi sitenize eklenebilir ya da ayrı bir adresle çalışabilir."),
                    ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz.")],
            "related": ["siparis-sistemi", "web-sitesi", "yapay-zeka-asistani"],
        },
        "siparis-sistemi": {
            "title": "Komisyonsuz Online Sipariş ve QR Menü Sistemi | DijiÇözüm",
            "desc": "Restoran ve kafeler için kendi online sipariş sayfanız ve QR menü. Siparişler komisyon ödemeden doğrudan mutfağınıza düşsün. Ücretsiz demo.",
            "crumb": "Sipariş ve QR menü", "h1": "Komisyonsuz online sipariş ve QR menü sistemi",
            "lead": "Yemek sipariş platformlarına her siparişte komisyon ödüyorsanız, kendi sipariş sayfanız bu yükü azaltabilir. Müşteri sizin sayfanızdan sipariş verir, sipariş doğrudan mutfağa düşer.",
            "service": "Online sipariş ve QR menü sistemi", "for_h": "Kimler için uygun?",
            "for": ["Restoran ve lokantalar", "Kafe ve pastaneler", "Kebapçı, büfe ve fast food", "Kendi kuryesi olan işletmeler"],
            "ben_h": "Size ne kazandırır?",
            "ben": [("Komisyon yükü azalır", "Kendi sayfanızdan gelen siparişlere platform komisyonu ödemezsiniz."),
                    ("Müşteri sizin olur", "Sipariş veren müşterinin bilgisi sizde kalır. Kampanyayı kendiniz yaparsınız."),
                    ("QR menü", "Masadaki QR kodu okutan müşteri menüyü görür ve sipariş verir."),
                    ("Mutfak ekranı", "Sipariş anında mutfak ekranına düşer. Durumu tek tuşla değiştirirsiniz."),
                    ("Masada, gel-al veya paket", "Müşteri siparişin nasıl teslim edileceğini seçer.")],
            "steps": [("Menünüzü gönderin", "Ürünleri, fiyatları ve fotoğrafları bize iletin."),
                      ("Sayfanızı hazırlayalım", "Sipariş sayfanızı ve QR kodunuzu hazırlayıp size gösteririz."),
                      ("Yayına alalım", "QR kodu masalara koyarsınız, bağlantıyı Instagram ve Google'a eklersiniz.")],
            "demo": ("/demo/siparis", "Restoran sipariş örneğini deneyin"),
            "demo_note": "Örnekte sepete ürün ekleyip sipariş verin, sonra \"Mutfak ekranı\"ndan siparişi ilerletin.",
            "faq": [("Online ödeme alınabilir mi?", "İsterseniz eklenir. iyzico veya PayTR gibi bir ödeme altyapısına bağlarız. Masada veya kapıda ödeme ile de çalışır."),
                    ("Menüyü kendim değiştirebilir miyim?", "Evet. Ürün, fiyat ve fotoğrafları panelden kendiniz değiştirirsiniz."),
                    ("Platformlardan gelen siparişler bu sisteme düşer mi?", "Bu ayrı bir iştir, işletmenize göre konuşuruz. Kendi sayfanızdan gelen siparişler hemen çalışır."),
                    ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz.")],
            "related": ["randevu-sistemi", "web-sitesi", "yapay-zeka-asistani"],
        },
        "web-sitesi": {
            "title": "Küçük İşletmeler İçin Web Sitesi Yaptırma | DijiÇözüm",
            "desc": "Telefonda düzgün açılan, Google'da bulunmanıza yardımcı olan web sitesi. Kuaför, klinik, atölye ve küçük işletmeler için. Önce çalışan örneği görün.",
            "crumb": "Web sitesi", "h1": "Küçük işletmeler için web sitesi yaptırma",
            "lead": "Müşterileriniz sizi önce internette arar. Telefonda düzgün açılan ve kolay bulunan bir site, işinize güven verir.",
            "service": "Web sitesi tasarımı ve kurulumu", "for_h": "Kimler için uygun?",
            "for": ["Kuaför, güzellik ve bakım merkezleri", "Klinik, atölye ve servisler", "Mühendislik, danışmanlık ve hukuk büroları", "Yeni açılan ve siteye ihtiyacı olan her işletme"],
            "ben_h": "Sitenizde neler olur?",
            "ben": [("Telefonda düzgün açılır", "Site telefon, tablet ve bilgisayarda düzgün görünür ve hızlı açılır."),
                    ("Google için hazırlık", "Doğru başlıklar, açıklamalar, hız ve harita gibi temel ayarlar yapılır."),
                    ("İletişim ve randevu", "Müşteri size form doldurarak, arayarak veya randevu alarak ulaşır."),
                    ("Kendi adınıza alan adı", "Alan adı ve e-posta adresi sizin adınıza açılır."),
                    ("Değişiklik kolay", "Yazı, fiyat ve fotoğraf değişikliklerini sizin için yaparız.")],
            "steps": [("Bilgilerinizi gönderin", "İşletme adınızı, hizmetlerinizi, logonuzu ve fotoğraflarınızı iletin."),
                      ("Taslağı görün", "Siteyi hazırlayıp size gösteririz. İstediğiniz değişiklikleri yaparız."),
                      ("Yayına alalım", "Onaylarsanız sitenizi kendi alan adınızla yayına alırız.")],
            "demo": ("/demo/kurumsal", "Kurumsal site örneğini deneyin"),
            "demo_note": "Örnekte sağ alttaki düğmelerle sitenin telefonda ve tablette nasıl göründüğüne bakın.",
            "faq": [("Google'da ilk sırada çıkar mıyım?", "Hiç kimse ilk sırayı garanti edemez. Sitenizi Google'un sevdiği şekilde hazırlarız. Sıralama zamanla, içeriğe ve rekabete göre oluşur."),
                    ("Alan adı ve hosting kime ait olur?", "Sizin adınıza açarız. Bizimle çalışmayı bıraksanız bile sizde kalır."),
                    ("Kaç sayfa olur?", "İşinize göre karar veririz. Küçük bir işletme için genellikle ana sayfa, hizmetler, hakkımızda ve iletişim yeterlidir."),
                    ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz.")],
            "related": ["randevu-sistemi", "siparis-sistemi", "yapay-zeka-asistani"],
        },
        "yapay-zeka-asistani": {
            "title": "Yapay Zeka Müşteri Asistanı (7/24 Türkçe) | DijiÇözüm",
            "desc": "Fiyat, saat ve adres sorularını 7/24 Türkçe yanıtlayan, randevu isteğini toplayan yapay zeka müşteri asistanı. İşletmenizin bilgisiyle çalışır. Ücretsiz demo.",
            "crumb": "Yapay zeka asistanı", "h1": "Müşteri sorularını 7/24 yanıtlayan yapay zeka asistanı",
            "lead": "Fiyat, çalışma saati, adres. Müşteriler hep aynı şeyleri sorar. Asistan bu soruları sizin verdiğiniz bilgilere göre Türkçe cevaplar, randevu isteklerini toplayıp size iletir.",
            "service": "Yapay zeka müşteri asistanı", "for_h": "Kimler için uygun?",
            "for": ["Müşterilerden çok soru gelen işletmeler", "Klinik, güzellik merkezi ve kurslar", "Mesai dışında da cevap vermek isteyenler", "Sitesi olan ve müşteri kazanmak isteyenler"],
            "ben_h": "Size ne kazandırır?",
            "ben": [("7/24 cevap", "Müşteri gece de sorusuna anında cevap alır."),
                    ("Sadece sizin bilginizden cevap verir", "Fiyatı, saati ve kuralları siz belirlersiniz. Asistan bunların dışına çıkmaz."),
                    ("Bilmediğinde uydurmaz", "Emin olmadığı soruda talebi size iletir."),
                    ("Randevu isteğini toplar", "Müşterinin adını, telefonunu ve isteğini alıp size iletir."),
                    ("Konuşmaları görürsünüz", "Müşterilerin neler sorduğunu panelden takip edersiniz.")],
            "steps": [("Soruları ve cevapları yazın", "Müşterilerin sık sorduğu şeyleri ve cevaplarını bize verin."),
                      ("Asistanı hazırlayalım", "Asistanı hazırlayıp sitenizde deneyeceğiniz şekilde size gösteririz."),
                      ("Yayına alalım", "Onaylarsanız sitenizde yayına alırız. İsterseniz WhatsApp gibi başka kanallar da eklenebilir.")],
            "demo": ("/demo/asistan", "Asistan örneğini deneyin"),
            "demo_note": "Örnekteki cevaplar önceden yazılıdır, nasıl çalıştığını göstermek içindir. Gerçek kurulumda asistan, sizin bilgilerinizle serbest cümlelerle cevap verir.",
            "faq": [("Yanlış bilgi verir mi?", "Sadece sizin onayladığınız bilgilerden cevap verir. Emin olmadığında uydurmak yerine talebi size iletir."),
                    ("Bir insana devredebilir mi?", "Evet. Müşteri isterse ya da asistan cevap veremezse talep size ulaşır."),
                    ("Müşteri bilgileri güvende mi?", "Bilgiler KVKK'ya uygun toplanır. Aydınlatma metni ve gerekli izin alanları eklenir."),
                    ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz.")],
            "related": ["randevu-sistemi", "siparis-sistemi", "web-sitesi"],
        },
    },
    "en": {
        "randevu-sistemi": {
            "title": "Online Booking System Setup | DijiÇözüm",
            "desc": "Online booking system for hairdressers, beauty salons, vets and consultants. Let customers book themselves and cut down phone traffic. Free demo.",
            "crumb": "Online booking system", "h1": "Online booking: let your customers book themselves",
            "lead": "Writing down bookings over the phone takes time. With an online booking system, your customer picks the time online. You just check the calendar.",
            "service": "Online booking system setup", "for_h": "Who is it for?",
            "for": ["Hairdressers and barbers", "Beauty and skincare centres", "Vets and dietitians", "Consultants, courses and workshops"],
            "ben_h": "What does it get you?",
            "ben": [("Fewer phone calls", "Customers book themselves. Less time spent on calls and messages."),
                    ("Empty slots fill up", "Customers can book at night too. The calendar works even when you're closed."),
                    ("Fewer no-shows", "A reminder message can go out before the appointment, if you want. Message cost is billed separately."),
                    ("Calendar by staff and service", "Set the duration for each staff member and each service separately."),
                    ("Easy management panel", "See bookings, cancel them, check your end-of-day summary.")],
            "steps": [("Send us your services", "Send us your service names, durations and working hours."),
                      ("We build your page", "We put together your booking page with your logo and colours and show you."),
                      ("We publish it", "If you like it, we publish it. You add the link to Instagram and Google.")],
            "demo": ("/demo/randevu", "Try the hairdresser booking example"),
            "demo_note": "Book an appointment in the example, then see your booking under the \"Business panel\" tab.",
            "faq": [("Does the customer need to sign up?", "No. It's enough for the customer to enter their name and phone number."),
                    ("How do I see the bookings?", "You see them in the business panel. We can also email you when a new booking comes in."),
                    ("Can I use it on my own website?", "Yes. The booking page can be embedded in your site or run on its own address."),
                    ("How much does it cost?", "It depends on the scope. Once you've seen the example, we give you a clear price in writing.")],
            "related": ["siparis-sistemi", "web-sitesi", "yapay-zeka-asistani"],
        },
        "siparis-sistemi": {
            "title": "Commission-Free Online Ordering & QR Menu | DijiÇözüm",
            "desc": "Your own online ordering page and QR menu for restaurants and cafes. Orders reach your kitchen directly, with no commission. Free demo.",
            "crumb": "Ordering & QR menu", "h1": "Commission-free online ordering and QR menu",
            "lead": "If you're paying commission on every order through food delivery platforms, your own ordering page can cut that cost. Customers order from your page, and it goes straight to the kitchen.",
            "service": "Online ordering & QR menu system", "for_h": "Who is it for?",
            "for": ["Restaurants and diners", "Cafes and bakeries", "Kebab shops, snack bars and fast food", "Businesses with their own delivery riders"],
            "ben_h": "What does it get you?",
            "ben": [("Less commission", "No platform commission on orders from your own page."),
                    ("The customer is yours", "You keep the ordering customer's information. You run your own promotions."),
                    ("QR menu", "Customers scan the QR code on the table to see the menu and order."),
                    ("Kitchen screen", "Orders land on the kitchen screen instantly. Update the status with one tap."),
                    ("Table, pickup or delivery", "Customers choose how the order is delivered.")],
            "steps": [("Send us your menu", "Send us your products, prices and photos."),
                      ("We build your page", "We put together your ordering page and QR code and show you."),
                      ("We publish it", "You place the QR code on tables and add the link to Instagram and Google.")],
            "demo": ("/demo/siparis", "Try the restaurant ordering example"),
            "demo_note": "Add products to the cart and place an order in the example, then move the order along from the \"Kitchen screen\".",
            "faq": [("Can you take online payments?", "Yes, if you want. We can connect a payment provider like iyzico or PayTR. It also works with pay-at-table or pay-on-delivery."),
                    ("Can I change the menu myself?", "Yes. You change products, prices and photos yourself from the panel."),
                    ("Do orders from delivery platforms land here too?", "That's a separate integration — we'd discuss it based on your setup. Orders from your own page work right away."),
                    ("How much does it cost?", "It depends on the scope. Once you've seen the example, we give you a clear price in writing.")],
            "related": ["randevu-sistemi", "web-sitesi", "yapay-zeka-asistani"],
        },
        "web-sitesi": {
            "title": "Website Design for Small Businesses | DijiÇözüm",
            "desc": "A website that looks right on phones and helps people find you on Google. For hairdressers, clinics, workshops and small businesses. See a working example first.",
            "crumb": "Website", "h1": "Websites for small businesses",
            "lead": "Your customers look for you online first. A site that works well on phones and is easy to find builds trust in your business.",
            "service": "Website design and setup", "for_h": "Who is it for?",
            "for": ["Hairdressers, beauty and skincare centres", "Clinics, workshops and service businesses", "Engineering, consulting and law offices", "Any new or existing business that needs a site"],
            "ben_h": "What's on your site?",
            "ben": [("Works right on phones", "The site looks right and loads fast on phone, tablet and desktop."),
                    ("Ready for Google", "The right titles, descriptions, speed and basic map settings are set up."),
                    ("Contact and booking", "Customers reach you through a form, a call, or by booking an appointment."),
                    ("Domain in your name", "The domain and email address are registered in your name."),
                    ("Easy to update", "We make text, price and photo changes for you.")],
            "steps": [("Send us your details", "Send us your business name, services, logo and photos."),
                      ("See the draft", "We build the site and show it to you. We make the changes you want."),
                      ("We publish it", "Once you approve, we publish your site on your own domain.")],
            "demo": ("/demo/kurumsal", "Try the corporate website example"),
            "demo_note": "Use the buttons in the bottom right of the example to see how the site looks on phone and tablet.",
            "faq": [("Will I rank first on Google?", "No one can guarantee the top spot. We build your site the way Google likes. Ranking builds up over time, based on content and competition."),
                    ("Who owns the domain and hosting?", "We register it in your name. It stays yours even if you stop working with us."),
                    ("How many pages will it have?", "We decide based on your business. For a small business, a home page, services, about and contact are usually enough."),
                    ("How much does it cost?", "It depends on the scope. Once you've seen the example, we give you a clear price in writing.")],
            "related": ["randevu-sistemi", "siparis-sistemi", "yapay-zeka-asistani"],
        },
        "yapay-zeka-asistani": {
            "title": "AI Customer Assistant, 24/7 | DijiÇözüm",
            "desc": "An AI customer assistant that answers price, hours and location questions 24/7 and collects booking requests. Works from your own business information. Free demo.",
            "crumb": "AI assistant", "h1": "An AI assistant that answers customer questions, 24/7",
            "lead": "Price, hours, location. Customers ask the same things over and over. The assistant answers these questions based on the information you give it, and passes booking requests on to you.",
            "service": "AI customer assistant", "for_h": "Who is it for?",
            "for": ["Businesses that get a lot of customer questions", "Clinics, beauty centres and courses", "Anyone who wants to answer outside working hours too", "Businesses with a site that want more customers"],
            "ben_h": "What does it get you?",
            "ben": [("Answers around the clock", "Customers get an answer instantly, even at night."),
                    ("Only answers from your information", "You decide the prices, hours and rules. The assistant doesn't go beyond them."),
                    ("Doesn't make things up", "When it's not sure, it passes the question to you instead of guessing."),
                    ("Collects booking requests", "It takes the customer's name, phone number and request, and passes them to you."),
                    ("You see the conversations", "Follow what customers are asking, from the panel.")],
            "steps": [("Send us your Q&A", "Give us the questions customers ask most, and the answers."),
                      ("We build the assistant", "We put it together and show you how it works on your site."),
                      ("We publish it", "Once you approve, we publish it on your site. Other channels like WhatsApp can be added too.")],
            "demo": ("/demo/asistan", "Try the assistant example"),
            "demo_note": "The answers in the example are pre-written, just to show how it works. In a real setup, the assistant answers freely using your own information.",
            "faq": [("Could it give wrong information?", "It only answers from information you've approved. When it's not sure, it passes the request to you instead of making something up."),
                    ("Can it hand off to a person?", "Yes. If the customer asks, or the assistant can't answer, the request reaches you."),
                    ("Is customer data safe?", "Data is collected in line with Turkey's KVKK data protection law. A privacy notice and the necessary consent fields are included."),
                    ("How much does it cost?", "It depends on the scope. Once you've seen the example, we give you a clear price in writing.")],
            "related": ["randevu-sistemi", "siparis-sistemi", "web-sitesi"],
        },
    },
}


def index_page(lang):
    u = UI[lang]
    ld = [ORG_LD, {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE + L("/", lang), "inLanguage": HTML_LANG[lang]},
          faq_ld(INDEX_FAQ[lang])]
    if lang == "tr":
        title = "DijiÇözüm | Online Randevu, Sipariş ve Web Sitesi Kurulumu"
        desc = "Online randevu, sipariş sistemi, web sitesi veya yapay zeka asistanı: ihtiyacınız olanı ayrı ayrı alın. Kuaför, restoran ve küçük işletmeler için."
    else:
        title = "DijiÇözüm | Online Booking, Ordering & Website Setup"
        desc = "Online booking, ordering, a website, or an AI assistant: get exactly what you need. For hairdressers, restaurants and small businesses in Turkey."
    out = head(lang, title, desc, "", ld) + header(lang, "") + "\n<main>\n"

    tiles_html = "".join(
        f'''      <a class="tile-card" href="{L(href, lang)}">
        <span class="icon-box">{icon(ic)}</span>
        <b>{escape(name)}</b><span>{escape(text)}</span><em>{escape(tag)}</em>
      </a>
''' for ic, href, name, text, tag in u["tiles"])

    out += f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">{u["eyebrow"]}</span>
      <h1>{u["hero_h1"]}</h1>
      <p class="lead">{u["hero_lead"]}</p>
      <div class="hero-cta">
        <a href="#iletisim" class="btn btn-primary">{u["hero_cta1"]}</a>
        <a href="#hizmetler" class="btn btn-ghost">{u["hero_cta2"]}</a>
      </div>
      <div class="hero-points">
{"".join(f"        <span>{escape(p)}</span>" + chr(10) for p in u["hero_points"])}      </div>
    </div>
    <div class="hero-tiles">
{tiles_html}    </div>
  </div>
</section>


<section id="hizmetler">
  <div class="wrap">
    <div class="section-head">
      <h2>{u["hizmetler_h2"]}</h2>
      <p class="lead">{u["hizmetler_lead"]}</p>
    </div>
    <div class="grid-2">
'''
    for q, a, href, label in PROBLEMS[lang]:
        out += f'''      <a class="card problem" href="{L(href, lang)}"><span class="q">“{escape(q)}”</span><p>{escape(a)}</p><span class="link-arrow">{escape(label)}</span></a>
'''
    out += f'''    </div>
  </div>
</section>

<section id="nasil" style="padding-top:24px">
  <div class="wrap">
    <div class="section-head">
      <h2>{u["nasil_h2"]}</h2>
    </div>
    <div class="steps three">
'''
    for t, x in u["steps3"]:
        out += f'      <div class="step"><h3>{escape(t)}</h3><p>{escape(x)}</p></div>\n'
    out += f'''    </div>
  </div>
</section>

<section id="ornekler" class="showcase">
  <div class="wrap">
    <div class="section-head">
      <h2>{u["ornekler_h2"]}</h2>
      <p class="lead">{u["ornekler_lead"]}</p>
    </div>
    <div class="demo-grid">
'''
    for ic, tag, title_, text, href in DEMOS[lang]:
        out += f'''      <a class="demo" href="{href}">
        <span class="icon-box">{icon(ic, 22)}</span>
        <span class="demo-tag">{escape(tag)}</span><h3>{escape(title_)}</h3><p>{escape(text)}</p><span class="link-arrow">{u["demo_try"]}</span>
      </a>
'''
    out += f'''    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>{u["neden_h2"]}</h2></div>
    <div class="grid-2">
'''
    for t, x in u["neden_cards"]:
        out += f'      <div class="card"><h3>{escape(t)}</h3><p>{escape(x)}</p></div>\n'
    out += f'''    </div>
  </div>
</section>

<section id="sss" style="padding-top:24px">
  <div class="wrap">
    <div class="section-head"><h2>{u["sss_h2"]}</h2></div>
    <div class="faq">''' + faq_html(INDEX_FAQ[lang]) + '''</div>
  </div>
</section>

<section id="iletisim" style="padding-top:24px">
  <div class="wrap contact-grid">
    <div class="contact-info">
      <h2>''' + u["iletisim_h2"] + '''</h2>
      <p class="lead">''' + u["iletisim_lead"] + '''</p>
      <ul>
        <li>''' + u["iletisim_bullets"][0] + '''</li>
        <li>''' + u["iletisim_bullets"][1] + '''</li>
        <li>''' + u["iletisim_bullets"][2] + '''<strong><a href="mailto:''' + EMAIL + '''" style="color:var(--brand-dark)">''' + EMAIL + '''</a></strong></li>
      </ul>
    </div>
    <form class="contact" id="contact-form" novalidate>
      <div class="field"><label for="ad">''' + u["f_ad"] + '''</label><input id="ad" name="ad" required autocomplete="name"></div>
      <div class="row2">
        <div class="field"><label for="tel">''' + u["f_tel"] + '''</label><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="''' + u["f_tel_ph"] + '''"></div>
        <div class="field"><label for="eposta">''' + u["f_email"] + '''</label><input id="eposta" name="eposta" type="email" autocomplete="email"></div>
      </div>
      <fieldset class="pick">
        <legend>''' + u["f_legend"] + ''' <span>''' + u["f_legend_hint"] + '''</span></legend>
        <div class="opts">
'''
    for opt in u["f_opts"]:
        out += f'          <label class="opt"><input type="checkbox" name="istenen" value="{escape(opt)}"> {escape(opt)}</label>\n'
    out += '''        </div>
      </fieldset>
            <div class="field"><label for="mesaj">''' + u["f_mesaj"] + '''</label><textarea id="mesaj" name="mesaj" placeholder="''' + u["f_mesaj_ph"] + '''"></textarea></div>
      <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
      <button class="btn btn-primary" type="submit" id="send-btn">''' + u["f_submit"] + '''</button>
      <p class="small" id="form-status" role="status">''' + u["f_status"] + '''<a href="/gizlilik" style="text-decoration:underline">''' + u["footer_privacy"] + '''</a></p>
    </form>
  </div>
</section>
</main>
''' + footer(lang) + wa_widget(lang) + '''
<script src="/assets/config.js?v=__V__"></script>
<script>
''' + MENU_JS + '''
const form = document.getElementById('contact-form');
const statusEl = document.getElementById('form-status');
const sendBtn = document.getElementById('send-btn');
const DEFAULT_OPT = ''' + json.dumps(u["f_opts"][-1], ensure_ascii=False) + ''';
function picked(){ const v = [...form.querySelectorAll('input[name=istenen]:checked')].map(x => x.value); return v.length ? v.join(', ') : DEFAULT_OPT; }
function err(m){ statusEl.style.color = '#b42318'; statusEl.textContent = m; }
function mailtoFallback(f) {
  const body = ['''+ json.dumps(u["f_ad"], ensure_ascii=False) +''' + ': ' + f.ad.value, ''' + json.dumps(u["f_tel"], ensure_ascii=False) + ''' + ': ' + (f.tel.value || '-'), ''' + json.dumps(u["f_email"].split(" (")[0], ensure_ascii=False) + ''' + ': ' + (f.eposta.value || '-'),
    picked(), '', f.mesaj.value].join('\\n');
  location.href = 'mailto:' + SITE.email + '?subject=' + encodeURIComponent(picked()) + '&body=' + encodeURIComponent(body);
}
form.addEventListener('submit', async e => {
  e.preventDefault();
  const f = e.target;
  const tel = f.tel.value.replace(/\\D/g, ''), mail = f.eposta.value.trim();
  if (!f.ad.value.trim()) return err(''' + json.dumps(u["err_name"], ensure_ascii=False) + ''');
  if (!tel && !mail) return err(''' + json.dumps(u["err_contact"], ensure_ascii=False) + ''');
  if (tel && tel.length < 10) return err(''' + json.dumps(u["err_phone"], ensure_ascii=False) + ''');
  if (mail && !/^\\S+@\\S+\\.\\S+$/.test(mail)) return err(''' + json.dumps(u["err_email"], ensure_ascii=False) + ''');
  if (!SITE.formKey) return mailtoFallback(f);
  if (f.botcheck.checked) return;
  sendBtn.disabled = true; sendBtn.textContent = ''' + json.dumps(u["f_sending"], ensure_ascii=False) + '''; statusEl.style.color = ''; statusEl.textContent = '';
  try {
    const payload = {
      access_key: SITE.formKey,
      subject: ''' + json.dumps(("Yeni demo talebi" if lang == "tr" else "New demo request"), ensure_ascii=False) + ''' + ': ' + picked() + ' (' + f.ad.value + ')',
      from_name: SITE.brand + ' Website',
      name: f.ad.value, telefon: f.tel.value || '-', istenen: picked(), mesaj: f.mesaj.value || '-'
    };
    if (mail) payload.email = mail;
    const res = await fetch('https://api.web3forms.com/submit', {
      method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (!data.success) throw new Error(data.message || 'failed');
    if (window.dcTrack) dcTrack('generate_lead', { services: picked() });
    form.innerHTML = '<div style="text-align:center;padding:36px 12px"><div style="font-size:44px" aria-hidden="true">✅</div><h3 style="margin:10px 0 6px">''' + u["f_success_title"] + '''</h3><p class="small" style="font-size:16px">''' + u["f_success_text"] + '''</p></div>';
  } catch (x) {
    sendBtn.disabled = false; sendBtn.textContent = ''' + json.dumps(u["f_submit"], ensure_ascii=False) + ''';
    statusEl.style.color = '#b42318';
    statusEl.innerHTML = ''' + json.dumps(u["f_fail"], ensure_ascii=False) + ''' + '<a href="mailto:' + SITE.email + '" style="text-decoration:underline">' + SITE.email + '</a>' + ''' + json.dumps(u["f_fail_end"], ensure_ascii=False) + ''';
  }
});
</script>
</body>
</html>
'''
    return out.replace("__V__", V)


def service_page(lang, slug):
    u = UI[lang]
    s = SERVICES[lang][slug]
    path = "/" + slug
    ld = [
        ORG_LD,
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["breadcrumb_home"], "item": SITE + L("/", lang)},
            {"@type": "ListItem", "position": 2, "name": s["crumb"], "item": SITE + L(path, lang)},
        ]},
        {"@context": "https://schema.org", "@type": "Service", "name": s["service"], "serviceType": s["service"],
         "description": s["desc"], "url": SITE + L(path, lang),
         "provider": {"@type": "Organization", "name": BRAND, "url": SITE + "/"}, "areaServed": {"@type": "Country", "name": "Türkiye"}},
        faq_ld(s["faq"]),
    ]
    out = head(lang, s["title"], s["desc"], slug, ld) + header(lang, slug) + "\n<main>\n"
    out += f'''<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="{u["breadcrumb_home"]}"><a href="{L("/", lang)}">{u["breadcrumb_home"]}</a> › {escape(s["crumb"])}</nav>
    <h1>{escape(s["h1"])}</h1>
    <p class="lead">{escape(s["lead"])}</p>
    <div class="hero-cta">
      <a href="{L("/#iletisim", lang)}" class="btn btn-primary">{u["header_cta"]}</a>
      <a href="{s["demo"][0]}" class="btn btn-ghost">{u["try_btn"]}</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>{escape(s["for_h"])}</h2>
    <ul class="checks">''' + "".join(f"<li>{escape(x)}</li>" for x in s["for"]) + f'''</ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>{escape(s["ben_h"])}</h2>
    <div class="grid-2">''' + "".join(f'<div class="card"><h3>{escape(t)}</h3><p>{escape(x)}</p></div>' for t, x in s["ben"]) + f'''</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>{u["sec_how_h2"]}</h2>
    <div class="steps three">''' + "".join(f'<div class="step"><h3>{escape(t)}</h3><p>{escape(x)}</p></div>' for t, x in s["steps"]) + f'''</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>{escape(s["demo"][1])}</h2><p>{escape(s["demo_note"])}</p></div>
      <a href="{s["demo"][0]}" class="btn btn-primary">{u["try_btn"]}</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>{u["sec_faq_h2"]}</h2>
    <div class="faq">{faq_html(s["faq"])}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>{u["sec_related_h2"]}</h2>
    <p class="lead" style="margin-bottom:18px">{u["sec_related_lead"]}</p>
    <div class="related">''' + "".join(f'<a href="{L("/" + r, lang)}">{escape(SERVICES[lang][r]["crumb"])}</a>' for r in s["related"]) + f'''</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>{u["final_cta_h2"]}</h2><p>{u["final_cta_text"]}</p></div>
      <a href="{L("/#iletisim", lang)}" class="btn btn-primary">{u["header_cta"]}</a>
    </div>
  </div>
</section>
</main>
''' + footer(lang) + wa_widget(lang) + f'''
<script>{MENU_JS}</script>
</body>
</html>
'''
    return out


def sitemap(urls):
    body = "".join(f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n" for p, pr in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


if __name__ == "__main__":
    written = []
    for lang in LANGS:
        outdir = ROOT if lang == DEFAULT_LANG else (ROOT / lang)
        outdir.mkdir(exist_ok=True)
        (outdir / "index.html").write_text(index_page(lang), encoding="utf-8")
        written.append(str((outdir / "index.html").relative_to(ROOT)))
        for slug in SERVICES[lang]:
            (outdir / f"{slug}.html").write_text(service_page(lang, slug), encoding="utf-8")
            written.append(str((outdir / f"{slug}.html").relative_to(ROOT)))

    urls = []
    for lang in LANGS:
        urls.append((L("/", lang), "1.0"))
        urls += [(L(f"/{s}", lang), "0.9") for s in SERVICES[lang]]
    urls += [(d[4], "0.6") for d in DEMOS["tr"]]
    (ROOT / "sitemap.xml").write_text(sitemap(urls), encoding="utf-8")

    import re
    for extra in ("gizlilik.html", "404.html"):
        f = ROOT / extra
        t = f.read_text(encoding="utf-8")
        t = re.sub(r'(?<![\w.])/?assets/style\.css(\?v=[0-9a-f]+)?', f"/assets/style.css?v={V}", t)
        f.write_text(t, encoding="utf-8")

    print("Üretildi:", ", ".join(written), "ve sitemap.xml")
