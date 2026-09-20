// Tüm demo sayfalarının üstüne "bu bir demodur" şeridini ekler.
(function () {
  const S = window.SITE || { brand: "DijiÇözüm", email: "" };
  const bar = document.createElement("div");
  bar.className = "demo-bar";
  bar.innerHTML =
    '<span><span class="tag">DEMO</span><a class="back" href="../index.html#vitrin">← Tüm demolar</a></span>' +
    '<span class="mid">Bu sayfa ' + S.brand + ' tarafından hazırlanmış örnek bir çalışmadır. Veriler kurgudur.</span>' +
    '<a href="../index.html#iletisim">Bunu kendi işletmem için istiyorum →</a>';
  document.body.classList.add("demo-page");
  document.body.prepend(bar);
})();
