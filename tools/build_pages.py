"""Ana sayfa ve hizmet sayfalarını üretir (menü, alt bilgi, SEO etiketleri ve JSON-LD ortak).

Kullanım:  python3 tools/build_pages.py
Sayfa metinlerini değiştirmek için bu dosyadaki PAGES sözlüğünü düzenleyin, sonra çalıştırın.
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


def _ver(*names):
    h = hashlib.md5()
    for n in names:
        h.update((ROOT / "assets" / n).read_bytes())
    return h.hexdigest()[:8]


V = _ver("style.css", "config.js", "consent.js")  # önbellek kırıcı: dosya değişince adres değişir

ICON_CHECK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'

ICON_PATHS = {
    "randevu": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/>',
    "siparis": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18M16 10a4 4 0 0 1-8 0"/>',
    "web": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 21h8"/>',
    "asistan": '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
    "uygulama": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
}


def icon(name, size=26):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON_PATHS[name]}</svg>'

# ---------------------------------------------------------------- ortak parçalar
NAV = [
    ("/randevu-sistemi", "Randevu"),
    ("/siparis-sistemi", "Sipariş"),
    ("/web-sitesi", "Web sitesi"),
    ("/yapay-zeka-asistani", "Yapay zeka"),
    ("/#ornekler", "Örnekler"),
]


WA_NUMBER = "905451579311"
WA_TEXT = "Merhaba, web sitenizden yazıyorum."


WA_ICON = (
    '<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.39 1.26 4.81L2 22l5.42-1.36a9.9 9.9 0 0 0 4.62 1.14h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.86 9.86 0 0 0 12.04 2zm5.8 14.02c-.24.68-1.4 1.32-1.93 1.4-.5.08-1.11.11-1.79-.11-.41-.13-.94-.31-1.62-.6-2.85-1.23-4.71-4.1-4.85-4.29-.14-.19-1.16-1.54-1.16-2.94s.73-2.09.99-2.37c.26-.29.56-.36.75-.36l.53.01c.17.01.4-.06.62.48.24.58.81 2 .88 2.14.07.14.12.31.02.5-.09.19-.14.31-.28.48-.14.17-.29.37-.42.5-.14.14-.28.29-.12.57.16.29.71 1.19 1.53 1.93 1.05.95 1.94 1.25 2.22 1.39.28.14.45.12.62-.07.17-.19.71-.83.9-1.12.19-.28.38-.24.63-.14.26.09 1.65.79 1.93.93.28.14.47.21.53.33.07.12.07.68-.17 1.36z"/>'
    '</svg>'
)


def wa_widget():
    """Site içinde açılan sohbet paneli. Gönderince aynı sekmede wa.me'ye gider (yeni sekme açmaz)."""
    return f'''<div class="wa-widget">
  <div class="wa-panel" id="wa-panel" hidden>
    <div class="wa-panel-head">
      <img src="/assets/logo/icon.svg" alt="" class="wa-panel-avatar">
      <div><b>İlhan Akkuş</b><span>DijiÇözüm · genelde hemen yanıtlar</span></div>
      <button type="button" class="wa-panel-close" id="wa-close" aria-label="Kapat">&times;</button>
    </div>
    <div class="wa-panel-body"><div class="wa-bubble">Merhaba 👋<br>Size nasıl yardımcı olabiliriz?</div></div>
    <form class="wa-panel-form" id="wa-form">
      <textarea id="wa-text" aria-label="Mesajınız">{WA_TEXT}</textarea>
      <button type="submit" class="wa-send" aria-label="Gönder">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 20l18-8L3 4v6l12 2-12 2z"/></svg>
      </button>
    </form>
  </div>
  <button type="button" class="wa-float" id="wa-toggle" aria-label="WhatsApp'tan yazın">{WA_ICON}</button>
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
    var msg=text.value.trim()||{WA_TEXT!r};
    if(window.dcTrack)dcTrack('whatsapp_click',{{page:location.pathname}});
    location.href='https://wa.me/{WA_NUMBER}?text='+encodeURIComponent(msg);
  }});
}})();</script>'''


def header():
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<header class="nav">
  <div class="wrap nav-in">
    <a href="/" class="logo" aria-label="{BRAND} ana sayfa"><img src="/assets/logo/logo-a.svg" alt="{BRAND}" width="155" height="34"></a>
    <nav class="nav-links" id="menu" aria-label="Ana menü">{links}</nav>
    <a href="/#iletisim" class="btn btn-primary btn-sm">Ücretsiz demonu iste</a>
    <button class="nav-toggle" aria-label="Menüyü aç" onclick="document.getElementById('menu').classList.toggle('open')">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>'''


def footer():
    return f'''<footer>
  <div class="wrap foot-cols">
    <div>
      <img src="/assets/logo/logo-c.svg" alt="dijiçözüm" width="110" height="31" style="margin-bottom:8px"><br>
      Küçük işletmeler için randevu, sipariş,<br>web sitesi ve yapay zeka çözümleri.<br>
      <a href="mailto:{EMAIL}" style="text-decoration:underline">{EMAIL}</a><br>
      <span style="display:block;margin-top:8px">© 2026 Tüm hakları saklıdır.</span>
    </div>
    <div><h4>Hizmetler</h4>
      <a href="/randevu-sistemi">Online randevu sistemi</a>
      <a href="/siparis-sistemi">Sipariş ve QR menü</a>
      <a href="/web-sitesi">Web sitesi</a>
      <a href="/yapay-zeka-asistani">Yapay zeka asistanı</a>
    </div>
    <div><h4>Diğer</h4>
      <a href="/#ornekler">Canlı örnekler</a>
      <a href="/#sss">Sık sorulanlar</a>
      <a href="/#iletisim">İletişim</a>
      <a href="/gizlilik">Gizlilik ve KVKK</a>
      <a href="#" data-cookie-settings>Çerez tercihleri</a>
    </div>
  </div>
</footer>'''


def faq_html(faqs):
    return "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faqs)


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
        ],
    }


ORG_LD = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": BRAND,
    "url": SITE + "/",
    "logo": SITE + "/assets/logo/png/icon-512.png",
    "email": EMAIL,
    "description": "Küçük işletmeler için online randevu, sipariş, web sitesi ve yapay zeka asistanı çözümleri.",
    "areaServed": {"@type": "Country", "name": "Türkiye"},
}


def head(title, desc, path, ld, extra=""):
    url = SITE + path
    ld_tags = "\n  ".join(
        f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld
    )
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="tr_TR">
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

# ---------------------------------------------------------------- ana sayfa
INDEX_FAQ = [
    ("Demo gerçekten ücretsiz mi?", "Evet. İşinizi anlattıktan sonra size özel çalışan bir örnek hazırlıyoruz. Beğenmezseniz hiçbir şey ödemezsiniz."),
    ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra, size yazılı ve net bir fiyat veririz."),
    ("Ne kadar sürede hazır olur?", "Basit bir site veya randevu sistemi genellikle birkaç haftada hazır olur. Telefon uygulaması daha uzun sürer. Süreyi teklifte yazarız."),
    ("Bilgisayardan anlamıyorum, kullanabilir miyim?", "Evet. Kurulumu biz yaparız. Nasıl kullanacağınızı kısa bir videoyla ve gerekirse yazılı olarak anlatırız."),
    ("Site ve alan adı kimin olur?", "Sizin adınıza açarız. Bizimle çalışmayı bıraksanız bile sizde kalır."),
    ("Müşteri bilgileri güvende mi?", "Bilgiler KVKK'ya uygun toplanır ve aydınlatma metni eklenir. Yapay zeka asistanı yalnızca sizin verdiğiniz bilgilere göre cevap verir."),
]

PROBLEMS = [
    ("Telefon sürekli çalıyor. Randevu yazmaktan yoruldum.", "Müşteri kendisi internetten randevu alır. Siz sadece takvime bakarsınız.", "/randevu-sistemi", "Online randevu sistemi"),
    ("Yemek sitelerine çok komisyon veriyorum.", "Kendi sipariş sayfanız olur. Siparişler komisyon ödemeden size gelir.", "/siparis-sistemi", "Sipariş ve QR menü"),
    ("Müşteriler hep aynı şeyleri soruyor.", "Asistan fiyat, saat ve adres sorularını 7/24 sizin yerinize cevaplar.", "/yapay-zeka-asistani", "Yapay zeka asistanı"),
    ("İnternette bulunmuyorum.", "Telefonda düzgün açılan, Google'da bulunan bir siteniz olur.", "/web-sitesi", "Web sitesi"),
]

DEMOS = [
    ("randevu", "Randevu", "Kuaför randevu sistemi", "Müşteri saati seçer. Randevu hemen sizin panelinize düşer.", "/demo/randevu"),
    ("siparis", "Sipariş", "Restoran sipariş sistemi", "Masadan QR okutulur, sipariş mutfak ekranına düşer.", "/demo/siparis"),
    ("asistan", "Yapay zeka", "Müşteri asistanı", "Fiyat ve saat sorularını cevaplar, randevu isteğini toplar.", "/demo/asistan"),
    ("uygulama", "Telefon uygulaması", "Spor salonu uygulaması", "Ders programı, QR kart ve bildirimler.", "/demo/uygulama"),
    ("web", "Web sitesi", "Kurumsal web sitesi", "Telefonda ve bilgisayarda düzgün açılan bir site.", "/demo/kurumsal"),
]


def index_page():
    ld = [
        ORG_LD,
        {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE + "/", "inLanguage": "tr-TR"},
        faq_ld(INDEX_FAQ),
    ]
    title = "DijiÇözüm | Online Randevu, Sipariş ve Web Sitesi Kurulumu"
    desc = "Online randevu, sipariş sistemi, web sitesi veya yapay zeka asistanı: ihtiyacınız olanı ayrı ayrı alın. Kuaför, restoran ve küçük işletmeler için."
    out = head(title, desc, "/", ld) + header() + "\n<main>\n"

    out += f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Küçük işletmeler için</span>
      <h1>İşletmenizin dijital <em>tek adresi</em>.</h1>
      <p class="lead">Online randevu, sipariş, web sitesi ve yapay zeka asistanı. Her biri ayrı ayrı alınır. İsterseniz birlikte de kurarız.</p>
      <div class="hero-cta">
        <a href="#iletisim" class="btn btn-primary">Ücretsiz demonu iste</a>
        <a href="#hizmetler" class="btn btn-ghost">Hizmetleri gör</a>
      </div>
      <div class="hero-points">
        <span>Önce örnek, sonra karar</span>
        <span>Ziyaret gerekmez</span>
        <span>Türkçe destek</span>
      </div>
    </div>
    <div class="hero-tiles">
      <a class="tile-card" href="/randevu-sistemi">
        <span class="icon-box">{icon("randevu")}</span>
        <b>Randevu sistemi</b><span>Müşteri internetten saat seçer.</span><em>Tek başına alınır</em>
      </a>
      <a class="tile-card" href="/siparis-sistemi">
        <span class="icon-box">{icon("siparis")}</span>
        <b>Sipariş sistemi</b><span>QR menü ve online sipariş.</span><em>Tek başına alınır</em>
      </a>
      <a class="tile-card" href="/web-sitesi">
        <span class="icon-box">{icon("web")}</span>
        <b>Web sitesi</b><span>Telefonda düzgün açılır, Google'da bulunur.</span><em>Tek başına alınır</em>
      </a>
      <a class="tile-card" href="/yapay-zeka-asistani">
        <span class="icon-box">{icon("asistan")}</span>
        <b>Yapay zeka asistanı</b><span>Müşteri sorularını 7/24 cevaplar.</span><em>Tek başına alınır</em>
      </a>
    </div>
  </div>
</section>


<section id="hizmetler">
  <div class="wrap">
    <div class="section-head">
      <h2>Bunlardan biri size tanıdık geliyor mu?</h2>
      <p class="lead">Her biri ayrı bir hizmet. Size lazım olana tıklayın.</p>
    </div>
    <div class="grid-2">
'''
    for q, a, href, label in PROBLEMS:
        out += f'''      <a class="card problem" href="{href}"><span class="q">“{escape(q)}”</span><p>{escape(a)}</p><span class="link-arrow">{escape(label)}</span></a>
'''
    out += '''    </div>
  </div>
</section>

<section id="nasil" style="padding-top:24px">
  <div class="wrap">
    <div class="section-head">
      <h2>Nasıl çalışıyor? Üç adım.</h2>
    </div>
    <div class="steps three">
      <div class="step"><h3>Bize yazın</h3><p>Aşağıdaki formu doldurun. İşinizi bir iki cümleyle anlatın.</p></div>
      <div class="step"><h3>Örneğinizi hazırlayalım</h3><p>Size uygun çalışan bir örnek hazırlayıp gönderiyoruz. Ücretsiz.</p></div>
      <div class="step"><h3>Beğenirseniz başlarız</h3><p>Fiyatı ve süreyi yazılı olarak netleştiririz. Beğenmezseniz bir şey ödemezsiniz.</p></div>
    </div>
  </div>
</section>

<section id="ornekler" class="showcase">
  <div class="wrap">
    <div class="section-head">
      <h2>Almadan önce deneyin</h2>
      <p class="lead">Aşağıdaki örneklerin hepsi çalışıyor. Tıklayıp deneyin. Örnek işletmeler kurgusaldır.</p>
    </div>
    <div class="demo-grid">
'''
    for ic, tag, title_, text, href in DEMOS:
        out += f'''      <a class="demo" href="{href}">
        <span class="icon-box">{icon(ic, 22)}</span>
        <span class="demo-tag">{escape(tag)}</span><h3>{escape(title_)}</h3><p>{escape(text)}</p><span class="link-arrow">Dene</span>
      </a>
'''
    out += '''    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>Neden bizimle çalışmalısınız?</h2></div>
    <div class="grid-2">
      <div class="card"><h3>Sade ve Türkçe</h3><p>Teknik kelime kullanmayız. Ne aldığınızı anlarsınız.</p></div>
      <div class="card"><h3>İster biri, ister hepsi</h3><p>Sadece ihtiyacınız olanı alırsınız. Birkaçını isterseniz birlikte kurarız. Muhatabınız hep aynı kişi olur.</p></div>
      <div class="card"><h3>Önce görürsünüz</h3><p>Ödeme yapmadan çalışan örneği denersiniz.</p></div>
      <div class="card"><h3>Baştan yazılı fiyat</h3><p>Ne yapılacağı ve ne kadar tutacağı önceden yazılı olur.</p></div>
    </div>
  </div>
</section>

<section id="sss" style="padding-top:24px">
  <div class="wrap">
    <div class="section-head"><h2>Sık sorulanlar</h2></div>
    <div class="faq">''' + faq_html(INDEX_FAQ) + '''</div>
  </div>
</section>

<section id="iletisim" style="padding-top:24px">
  <div class="wrap contact-grid">
    <div class="contact-info">
      <h2>Ücretsiz demonu iste</h2>
      <p class="lead">Adınızı ve telefonunuzu yazın. Size geri dönelim.</p>
      <ul>
        <li>Genellikle bir iş günü içinde dönüş yaparız.</li>
        <li>Demo ücretsizdir, bir şey satın almak zorunda değilsiniz.</li>
        <li>Yazmak isterseniz: <strong><a href="mailto:''' + EMAIL + '''" style="color:var(--brand-dark)">''' + EMAIL + '''</a></strong></li>
      </ul>
    </div>
    <form class="contact" id="contact-form" novalidate>
      <div class="field"><label for="ad">Adınız</label><input id="ad" name="ad" required autocomplete="name"></div>
      <div class="row2">
        <div class="field"><label for="tel">Telefon</label><input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="05xx xxx xx xx"></div>
        <div class="field"><label for="eposta">E-posta (isteğe bağlı)</label><input id="eposta" name="eposta" type="email" autocomplete="email"></div>
      </div>
      <fieldset class="pick">
        <legend>Ne istiyorsunuz? <span>(birden fazla seçebilirsiniz)</span></legend>
        <div class="opts">
          <label class="opt"><input type="checkbox" name="istenen" value="Online randevu sistemi"> Randevu sistemi</label>
          <label class="opt"><input type="checkbox" name="istenen" value="Sipariş ve QR menü"> Sipariş ve QR menü</label>
          <label class="opt"><input type="checkbox" name="istenen" value="Web sitesi"> Web sitesi</label>
          <label class="opt"><input type="checkbox" name="istenen" value="Yapay zeka asistanı"> Yapay zeka asistanı</label>
          <label class="opt"><input type="checkbox" name="istenen" value="Telefon uygulaması"> Telefon uygulaması</label>
          <label class="opt"><input type="checkbox" name="istenen" value="Bilmiyorum, önerin"> Bilmiyorum, önerin</label>
        </div>
      </fieldset>
            <div class="field"><label for="mesaj">Kısaca işinizi anlatın (isteğe bağlı)</label><textarea id="mesaj" name="mesaj" placeholder="Örn. Kuaförüm var, randevuları telefonla alıyorum."></textarea></div>
      <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
      <button class="btn btn-primary" type="submit" id="send-btn">Demomu iste</button>
      <p class="small" id="form-status" role="status">Bilgileriniz yalnızca size dönüş yapmak için kullanılır. <a href="/gizlilik" style="text-decoration:underline">Gizlilik ve KVKK</a></p>
    </form>
  </div>
</section>
</main>
''' + footer() + wa_widget() + '''
<script src="/assets/config.js?v=__V__"></script>
<script>
''' + MENU_JS + '''
const form = document.getElementById('contact-form');
const statusEl = document.getElementById('form-status');
const sendBtn = document.getElementById('send-btn');
function picked(){ const v = [...form.querySelectorAll('input[name=istenen]:checked')].map(x => x.value); return v.length ? v.join(', ') : 'Bilmiyorum, önerin'; }
function err(m){ statusEl.style.color = '#b42318'; statusEl.textContent = m; }
function mailtoFallback(f) {
  const body = ['Ad: ' + f.ad.value, 'Telefon: ' + (f.tel.value || '-'), 'E-posta: ' + (f.eposta.value || '-'),
    'İstenen: ' + picked(), '', f.mesaj.value].join('\\n');
  location.href = 'mailto:' + SITE.email + '?subject=' + encodeURIComponent('Demo talebi: ' + picked()) + '&body=' + encodeURIComponent(body);
}
form.addEventListener('submit', async e => {
  e.preventDefault();
  const f = e.target;
  const tel = f.tel.value.replace(/\\D/g, ''), mail = f.eposta.value.trim();
  if (!f.ad.value.trim()) return err('Lütfen adınızı yazın.');
  if (!tel && !mail) return err('Size ulaşabilmemiz için telefon veya e-posta yazın.');
  if (tel && tel.length < 10) return err('Telefon numarası eksik görünüyor. 05xx ile başlayan 11 haneyi yazın.');
  if (mail && !/^\\S+@\\S+\\.\\S+$/.test(mail)) return err('E-posta adresi hatalı görünüyor.');
  if (!SITE.formKey) return mailtoFallback(f);
  if (f.botcheck.checked) return;
  sendBtn.disabled = true; sendBtn.textContent = 'Gönderiliyor…'; statusEl.style.color = ''; statusEl.textContent = '';
  try {
    const payload = {
      access_key: SITE.formKey,
      subject: 'Yeni demo talebi: ' + picked() + ' (' + f.ad.value + ')',
      from_name: SITE.brand + ' Web Sitesi',
      name: f.ad.value, telefon: f.tel.value || '-', istenen: picked(), mesaj: f.mesaj.value || '-'
    };
    if (mail) payload.email = mail;
    const res = await fetch('https://api.web3forms.com/submit', {
      method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (!data.success) throw new Error(data.message || 'gönderilemedi');
    if (window.dcTrack) dcTrack('generate_lead', { services: picked() });
    form.innerHTML = '<div style="text-align:center;padding:36px 12px"><div style="font-size:44px" aria-hidden="true">✅</div><h3 style="margin:10px 0 6px">Talebiniz bize ulaştı</h3><p class="small" style="font-size:16px">En kısa sürede size dönüş yapacağız. Teşekkürler!</p></div>';
  } catch (x) {
    sendBtn.disabled = false; sendBtn.textContent = 'Demomu iste';
    statusEl.style.color = '#b42318';
    statusEl.innerHTML = 'Gönderilemedi. Lütfen tekrar deneyin ya da <a href="mailto:' + SITE.email + '" style="text-decoration:underline">' + SITE.email + '</a> adresine yazın.';
  }
});
</script>
</body>
</html>
'''
    return out.replace("__V__", V)


# ---------------------------------------------------------------- hizmet sayfaları
SERVICES = {
    "randevu-sistemi": {
        "title": "Online Randevu Sistemi Kurulumu | DijiÇözüm",
        "desc": "Kuaför, güzellik merkezi, veteriner ve danışmanlar için online randevu sistemi. Müşteri kendisi randevu alsın, telefon trafiği azalsın. Ücretsiz demo.",
        "crumb": "Online randevu sistemi",
        "h1": "Online randevu sistemi: müşteriniz kendisi randevu alsın",
        "lead": "Telefonda randevu yazmak zaman alır. Online randevu sistemiyle müşteriniz internetten saati seçer. Siz sadece takvime bakarsınız.",
        "service": "Online randevu sistemi kurulumu",
        "for_h": "Kimler için uygun?",
        "for": ["Kuaför ve berberler", "Güzellik ve bakım merkezleri", "Veteriner ve diyetisyenler", "Danışmanlar, kurslar ve atölyeler"],
        "ben_h": "Size ne kazandırır?",
        "ben": [
            ("Telefon azalır", "Müşteri randevuyu kendisi alır. Telefona ve mesajlara harcadığınız zaman kısalır."),
            ("Boş saatler dolar", "Müşteri gece de randevu alabilir. İşletmeniz kapalıyken bile takvim çalışır."),
            ("Unutan müşteri azalır", "İsterseniz randevudan önce hatırlatma mesajı gider. Mesaj ücreti ayrıca yansıtılır."),
            ("Personel ve hizmete göre takvim", "Her çalışanın ve her hizmetin süresini ayrı ayrı ayarlarsınız."),
            ("Kolay yönetim paneli", "Randevuları görürsünüz, iptal edersiniz, gün sonu özetine bakarsınız."),
        ],
        "steps": [
            ("Hizmetlerinizi yazın", "Hizmet adlarını, sürelerini ve çalışma saatlerinizi bize gönderin."),
            ("Sayfanızı hazırlayalım", "Logo ve renklerinizle randevu sayfanızı hazırlayıp size gösteririz."),
            ("Yayına alalım", "Beğenirseniz yayına alırız. Bağlantıyı Instagram'a ve Google'a koyarsınız."),
        ],
        "demo": ("/demo/randevu", "Kuaför randevu örneğini deneyin"),
        "demo_note": "Örnekte bir randevu alın, sonra \"İşletme paneli\" sekmesinde randevunuzu görün.",
        "faq": [
            ("Müşterinin üye olması gerekir mi?", "Hayır. Müşterinin adını ve telefonunu yazması yeterlidir."),
            ("Randevuları nasıl görürüm?", "İşletme panelinden görürsünüz. İsterseniz yeni randevu geldiğinde e-posta ile de haber veririz."),
            ("Kendi web sitemde kullanabilir miyim?", "Evet. Randevu sayfası kendi sitenize eklenebilir ya da ayrı bir adresle çalışabilir."),
            ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz."),
        ],
        "related": ["siparis-sistemi", "web-sitesi", "yapay-zeka-asistani"],
    },
    "siparis-sistemi": {
        "title": "Komisyonsuz Online Sipariş ve QR Menü Sistemi | DijiÇözüm",
        "desc": "Restoran ve kafeler için kendi online sipariş sayfanız ve QR menü. Siparişler komisyon ödemeden doğrudan mutfağınıza düşsün. Ücretsiz demo.",
        "crumb": "Sipariş ve QR menü",
        "h1": "Komisyonsuz online sipariş ve QR menü sistemi",
        "lead": "Yemek sipariş platformlarına her siparişte komisyon ödüyorsanız, kendi sipariş sayfanız bu yükü azaltabilir. Müşteri sizin sayfanızdan sipariş verir, sipariş doğrudan mutfağa düşer.",
        "service": "Online sipariş ve QR menü sistemi",
        "for_h": "Kimler için uygun?",
        "for": ["Restoran ve lokantalar", "Kafe ve pastaneler", "Kebapçı, büfe ve fast food", "Kendi kuryesi olan işletmeler"],
        "ben_h": "Size ne kazandırır?",
        "ben": [
            ("Komisyon yükü azalır", "Kendi sayfanızdan gelen siparişlere platform komisyonu ödemezsiniz."),
            ("Müşteri sizin olur", "Sipariş veren müşterinin bilgisi sizde kalır. Kampanyayı kendiniz yaparsınız."),
            ("QR menü", "Masadaki QR kodu okutan müşteri menüyü görür ve sipariş verir."),
            ("Mutfak ekranı", "Sipariş anında mutfak ekranına düşer. Durumu tek tuşla değiştirirsiniz."),
            ("Masada, gel-al veya paket", "Müşteri siparişin nasıl teslim edileceğini seçer."),
        ],
        "steps": [
            ("Menünüzü gönderin", "Ürünleri, fiyatları ve fotoğrafları bize iletin."),
            ("Sayfanızı hazırlayalım", "Sipariş sayfanızı ve QR kodunuzu hazırlayıp size gösteririz."),
            ("Yayına alalım", "QR kodu masalara koyarsınız, bağlantıyı Instagram ve Google'a eklersiniz."),
        ],
        "demo": ("/demo/siparis", "Restoran sipariş örneğini deneyin"),
        "demo_note": "Örnekte sepete ürün ekleyip sipariş verin, sonra \"Mutfak ekranı\"ndan siparişi ilerletin.",
        "faq": [
            ("Online ödeme alınabilir mi?", "İsterseniz eklenir. iyzico veya PayTR gibi bir ödeme altyapısına bağlarız. Masada veya kapıda ödeme ile de çalışır."),
            ("Menüyü kendim değiştirebilir miyim?", "Evet. Ürün, fiyat ve fotoğrafları panelden kendiniz değiştirirsiniz."),
            ("Platformlardan gelen siparişler bu sisteme düşer mi?", "Bu ayrı bir iştir, işletmenize göre konuşuruz. Kendi sayfanızdan gelen siparişler hemen çalışır."),
            ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz."),
        ],
        "related": ["randevu-sistemi", "web-sitesi", "yapay-zeka-asistani"],
    },
    "web-sitesi": {
        "title": "Küçük İşletmeler İçin Web Sitesi Yaptırma | DijiÇözüm",
        "desc": "Telefonda düzgün açılan, Google'da bulunmanıza yardımcı olan web sitesi. Kuaför, klinik, atölye ve küçük işletmeler için. Önce çalışan örneği görün.",
        "crumb": "Web sitesi",
        "h1": "Küçük işletmeler için web sitesi yaptırma",
        "lead": "Müşterileriniz sizi önce internette arar. Telefonda düzgün açılan ve kolay bulunan bir site, işinize güven verir.",
        "service": "Web sitesi tasarımı ve kurulumu",
        "for_h": "Kimler için uygun?",
        "for": ["Kuaför, güzellik ve bakım merkezleri", "Klinik, atölye ve servisler", "Mühendislik, danışmanlık ve hukuk büroları", "Yeni açılan ve siteye ihtiyacı olan her işletme"],
        "ben_h": "Sitenizde neler olur?",
        "ben": [
            ("Telefonda düzgün açılır", "Site telefon, tablet ve bilgisayarda düzgün görünür ve hızlı açılır."),
            ("Google için hazırlık", "Doğru başlıklar, açıklamalar, hız ve harita gibi temel ayarlar yapılır."),
            ("İletişim ve randevu", "Müşteri size form doldurarak, arayarak veya randevu alarak ulaşır."),
            ("Kendi adınıza alan adı", "Alan adı ve e-posta adresi sizin adınıza açılır."),
            ("Değişiklik kolay", "Yazı, fiyat ve fotoğraf değişikliklerini sizin için yaparız."),
        ],
        "steps": [
            ("Bilgilerinizi gönderin", "İşletme adınızı, hizmetlerinizi, logonuzu ve fotoğraflarınızı iletin."),
            ("Taslağı görün", "Siteyi hazırlayıp size gösteririz. İstediğiniz değişiklikleri yaparız."),
            ("Yayına alalım", "Onaylarsanız sitenizi kendi alan adınızla yayına alırız."),
        ],
        "demo": ("/demo/kurumsal", "Kurumsal site örneğini deneyin"),
        "demo_note": "Örnekte sağ alttaki düğmelerle sitenin telefonda ve tablette nasıl göründüğüne bakın.",
        "faq": [
            ("Google'da ilk sırada çıkar mıyım?", "Hiç kimse ilk sırayı garanti edemez. Sitenizi Google'un sevdiği şekilde hazırlarız. Sıralama zamanla, içeriğe ve rekabete göre oluşur."),
            ("Alan adı ve hosting kime ait olur?", "Sizin adınıza açarız. Bizimle çalışmayı bıraksanız bile sizde kalır."),
            ("Kaç sayfa olur?", "İşinize göre karar veririz. Küçük bir işletme için genellikle ana sayfa, hizmetler, hakkımızda ve iletişim yeterlidir."),
            ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz."),
        ],
        "related": ["randevu-sistemi", "siparis-sistemi", "yapay-zeka-asistani"],
    },
    "yapay-zeka-asistani": {
        "title": "Yapay Zeka Müşteri Asistanı (7/24 Türkçe) | DijiÇözüm",
        "desc": "Fiyat, saat ve adres sorularını 7/24 Türkçe yanıtlayan, randevu isteğini toplayan yapay zeka müşteri asistanı. İşletmenizin bilgisiyle çalışır. Ücretsiz demo.",
        "crumb": "Yapay zeka asistanı",
        "h1": "Müşteri sorularını 7/24 yanıtlayan yapay zeka asistanı",
        "lead": "Fiyat, çalışma saati, adres. Müşteriler hep aynı şeyleri sorar. Asistan bu soruları sizin verdiğiniz bilgilere göre Türkçe cevaplar, randevu isteklerini toplayıp size iletir.",
        "service": "Yapay zeka müşteri asistanı",
        "for_h": "Kimler için uygun?",
        "for": ["Müşterilerden çok soru gelen işletmeler", "Klinik, güzellik merkezi ve kurslar", "Mesai dışında da cevap vermek isteyenler", "Sitesi olan ve müşteri kazanmak isteyenler"],
        "ben_h": "Size ne kazandırır?",
        "ben": [
            ("7/24 cevap", "Müşteri gece de sorusuna anında cevap alır."),
            ("Sadece sizin bilginizden cevap verir", "Fiyatı, saati ve kuralları siz belirlersiniz. Asistan bunların dışına çıkmaz."),
            ("Bilmediğinde uydurmaz", "Emin olmadığı soruda talebi size iletir."),
            ("Randevu isteğini toplar", "Müşterinin adını, telefonunu ve isteğini alıp size iletir."),
            ("Konuşmaları görürsünüz", "Müşterilerin neler sorduğunu panelden takip edersiniz."),
        ],
        "steps": [
            ("Soruları ve cevapları yazın", "Müşterilerin sık sorduğu şeyleri ve cevaplarını bize verin."),
            ("Asistanı hazırlayalım", "Asistanı hazırlayıp sitenizde deneyeceğiniz şekilde size gösteririz."),
            ("Yayına alalım", "Onaylarsanız sitenizde yayına alırız. İsterseniz WhatsApp gibi başka kanallar da eklenebilir."),
        ],
        "demo": ("/demo/asistan", "Asistan örneğini deneyin"),
        "demo_note": "Örnekteki cevaplar önceden yazılıdır, nasıl çalıştığını göstermek içindir. Gerçek kurulumda asistan, sizin bilgilerinizle serbest cümlelerle cevap verir.",
        "faq": [
            ("Yanlış bilgi verir mi?", "Sadece sizin onayladığınız bilgilerden cevap verir. Emin olmadığında uydurmak yerine talebi size iletir."),
            ("Bir insana devredebilir mi?", "Evet. Müşteri isterse ya da asistan cevap veremezse talep size ulaşır."),
            ("Müşteri bilgileri güvende mi?", "Bilgiler KVKK'ya uygun toplanır. Aydınlatma metni ve gerekli izin alanları eklenir."),
            ("Ne kadar tutar?", "İşin kapsamına göre değişir. Örneği gördükten sonra yazılı ve net bir fiyat veririz."),
        ],
        "related": ["randevu-sistemi", "siparis-sistemi", "web-sitesi"],
    },
}


def service_page(slug):
    s = SERVICES[slug]
    path = "/" + slug
    ld = [
        ORG_LD,
        {
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": s["crumb"], "item": SITE + path},
            ],
        },
        {
            "@context": "https://schema.org", "@type": "Service", "name": s["service"],
            "serviceType": s["service"], "description": s["desc"], "url": SITE + path,
            "provider": {"@type": "Organization", "name": BRAND, "url": SITE + "/"},
            "areaServed": {"@type": "Country", "name": "Türkiye"},
        },
        faq_ld(s["faq"]),
    ]
    out = head(s["title"], s["desc"], path, ld) + header() + "\n<main>\n"
    out += f'''<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Sayfa yolu"><a href="/">Ana sayfa</a> › {escape(s["crumb"])}</nav>
    <h1>{escape(s["h1"])}</h1>
    <p class="lead">{escape(s["lead"])}</p>
    <div class="hero-cta">
      <a href="/#iletisim" class="btn btn-primary">Ücretsiz demonu iste</a>
      <a href="{s["demo"][0]}" class="btn btn-ghost">Örneği dene</a>
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
    <h2>Nasıl çalışıyor?</h2>
    <div class="steps three">''' + "".join(f'<div class="step"><h3>{escape(t)}</h3><p>{escape(x)}</p></div>' for t, x in s["steps"]) + f'''</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>{escape(s["demo"][1])}</h2><p>{escape(s["demo_note"])}</p></div>
      <a href="{s["demo"][0]}" class="btn btn-primary">Örneği dene</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>Sık sorulanlar</h2>
    <div class="faq">{faq_html(s["faq"])}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2>Diğer çözümlerimiz</h2>
    <p class="lead" style="margin-bottom:18px">Her biri ayrı ayrı alınabilir. İsterseniz birlikte de kurarız.</p>
    <div class="related">''' + "".join(f'<a href="/{r}">{escape(SERVICES[r]["crumb"])}</a>' for r in s["related"]) + f'''</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-band">
      <div><h2>Ücretsiz demonuzu hazırlayalım</h2><p>Formu doldurun, size özel çalışan bir örnek gönderelim.</p></div>
      <a href="/#iletisim" class="btn btn-primary">Ücretsiz demonu iste</a>
    </div>
  </div>
</section>
</main>
''' + footer() + wa_widget() + f'''
<script>{MENU_JS}</script>
</body>
</html>
'''
    return out


def sitemap(urls):
    body = "".join(
        f"  <url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n" for p, pr in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


if __name__ == "__main__":
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")
    for slug in SERVICES:
        (ROOT / f"{slug}.html").write_text(service_page(slug), encoding="utf-8")
    urls = [("/", "1.0")] + [(f"/{s}", "0.9") for s in SERVICES] + [
        (d[4], "0.6") for d in DEMOS
    ]
    (ROOT / "sitemap.xml").write_text(sitemap(urls), encoding="utf-8")
    import re
    for extra in ("gizlilik.html", "404.html"):
        f = ROOT / extra
        t = f.read_text(encoding="utf-8")
        t = re.sub(r'(?<![\w.])/?assets/style\.css(\?v=[0-9a-f]+)?', f"/assets/style.css?v={V}", t)
        f.write_text(t, encoding="utf-8")
    print("Üretildi: index.html,", ", ".join(f"{s}.html" for s in SERVICES), "ve sitemap.xml")
