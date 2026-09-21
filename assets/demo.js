// Tüm demo sayfalarının üstüne "bu bir demodur" şeridini ekler.
(function () {
  const S = window.SITE || { brand: "DijiÇözüm", email: "" };
  const bar = document.createElement("div");
  bar.className = "demo-bar";
  bar.innerHTML =
    '<span><span class="tag">DEMO</span><a class="back" href="../index.html#vitrin">← Tüm demolar</a></span>' +
    '<span class="mid">Bu sayfa ' + S.brand + ' tarafından hazırlanmış örnek bir çalışmadır. Veriler kurgudur.</span>' +
    '<a href="../index.html#iletisim">Bunu kendi işletmem için istiyorum →</a>';
  if (!document.querySelector('link[rel~="icon"]')) {
    const ic = document.createElement("link");
    ic.rel = "icon"; ic.type = "image/svg+xml"; ic.href = "/assets/logo/icon.svg";
    document.head.appendChild(ic);
  }
  if (!document.querySelector('script[src*="consent.js"]')) {
    const c = document.createElement("script");
    c.src = "/assets/consent.js"; c.defer = true;
    document.head.appendChild(c);
  }
  document.body.classList.add("demo-page");
  document.body.prepend(bar);
})();
