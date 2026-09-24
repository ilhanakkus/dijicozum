/* Çerez onayı ve Google Analytics (GA4).
 * KVKK: Analytics etiketi YALNIZCA ziyaretçi "Kabul et" derse yüklenir.
 * Reddederse Google'a hiçbir istek gitmez, çerez yerleştirilmez.
 */
(function () {
  var GA_ID = "G-XBCWL4LQS2";
  var KEY = "dc_consent";
  var MAX_AGE = 365 * 24 * 3600 * 1000; // 12 ay sonra yeniden sorulur

  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY));
      if (v && (v.choice === "granted" || v.choice === "denied") && Date.now() - v.t < MAX_AGE) return v.choice;
    } catch (e) {}
    return null;
  }
  function save(choice) {
    try { localStorage.setItem(KEY, JSON.stringify({ choice: choice, t: Date.now() })); } catch (e) {}
  }

  // Kendi ziyaretlerinizi ölçümden çıkarmak için: siteyi bir kez ?internal=1 ile açın.
  try {
    var q = new URLSearchParams(location.search).get("internal");
    if (q === "1") localStorage.setItem("dc_internal", "1");
    if (q === "0") localStorage.removeItem("dc_internal");
  } catch (e) {}
  function isInternal() {
    try { return localStorage.getItem("dc_internal") === "1"; } catch (e) { return false; }
  }

  var loaded = false;
  function loadGA() {
    if (loaded) return;
    loaded = true;
    window["ga-disable-" + GA_ID] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    gtag("consent", "default", {
      analytics_storage: "granted", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied"
    });
    gtag("js", new Date());
    var cfg = { allow_google_signals: false, allow_ad_personalization_signals: false, transport_type: "beacon" };
    if (isInternal()) cfg.traffic_type = "internal"; // Analytics'te "Internal Traffic" filtresi bunu dışlar
    gtag("config", GA_ID, cfg);
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
  }

  function clearCookies() {
    var host = location.hostname, parts = host.split("."), root = parts.length > 2 ? parts.slice(-2).join(".") : host;
    document.cookie.split(";").forEach(function (c) {
      var name = c.split("=")[0].trim();
      if (name === "_ga" || name.indexOf("_ga_") === 0 || name === "_gid") {
        [host, "." + host, "." + root].forEach(function (d) {
          document.cookie = name + "=; Max-Age=0; path=/; domain=" + d;
        });
        document.cookie = name + "=; Max-Age=0; path=/";
      }
    });
  }

  // Sayfa içinden olay gönderimi (ad, telefon gibi kişisel veri GÖNDERİLMEZ)
  window.dcTrack = function (name, params) {
    if (loaded && window.gtag) window.gtag("event", name, params || {});
  };

  function css() {
    if (document.getElementById("dc-consent-css")) return;
    var st = document.createElement("style");
    st.id = "dc-consent-css";
    st.textContent =
      ".dc-consent{position:fixed;left:16px;right:16px;bottom:16px;z-index:1500;max-width:720px;margin:0 auto;background:#fff;color:#0f172a;" +
      "border:1px solid #e7e1d6;border-radius:16px;box-shadow:0 12px 40px -8px rgba(15,23,42,.35);padding:18px 20px;" +
      "font:15px/1.5 'Plus Jakarta Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}" +
      ".dc-consent b{display:block;font-size:16px;margin-bottom:4px}" +
      ".dc-consent p{margin:0 0 14px;color:#3a4557}" +
      ".dc-consent a{color:#b8430a;text-decoration:underline}" +
      ".dc-consent .dc-row{display:flex;gap:10px}" +
      ".dc-consent button{flex:1;padding:12px 16px;border-radius:999px;border:2px solid #0f172a;background:#fff;color:#0f172a;" +
      "font:700 15px 'Plus Jakarta Sans',system-ui,sans-serif;cursor:pointer}" +
      ".dc-consent button:hover{background:#0f172a;color:#fff}" +
      "@media(max-width:480px){.dc-consent{left:10px;right:10px;bottom:10px;padding:16px}}";
    document.head.appendChild(st);
  }

  var box = null;
  function close() { if (box) { box.remove(); box = null; } }
  function decide(choice) {
    save(choice);
    close();
    if (choice === "granted") loadGA();
    else { window["ga-disable-" + GA_ID] = true; clearCookies(); }
  }
  function open() {
    css();
    close();
    box = document.createElement("div");
    box.className = "dc-consent";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-label", "Çerez tercihi");
    box.innerHTML =
      "<b>Çerez tercihiniz</b>" +
      "<p>Siteyi geliştirmek için kaç kişinin ziyaret ettiğini ölçmek istiyoruz. Bunun için Google Analytics çerezleri kullanılır ve verileriniz yurt dışına (ABD) aktarılabilir. " +
      "Reddederseniz site aynen çalışır. <a href=\"/gizlilik#cerezler\">Ayrıntılar</a></p>" +
      "<div class=\"dc-row\"><button type=\"button\" data-c=\"denied\">Reddet</button><button type=\"button\" data-c=\"granted\">Kabul et</button></div>";
    box.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-c]");
      if (b) decide(b.getAttribute("data-c"));
    });
    document.body.appendChild(box);
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest ? e.target : e.target.parentElement;
    if (!t || !t.closest) return;
    if (t.closest("[data-cookie-settings]")) { e.preventDefault(); open(); return; }
    var a = t.closest("a");
    if (!a) return;
    var h = a.getAttribute("href") || "";
    if (h.indexOf("/demo/") > -1) window.dcTrack("demo_open", { demo: h.split("/demo/")[1].split(/[?#]/)[0] });
    else if (h.indexOf("#iletisim") > -1) window.dcTrack("cta_click", { page: location.pathname });
    else if (h.indexOf("mailto:") === 0) window.dcTrack("email_click", { page: location.pathname });
    else if (h.indexOf("wa.me/") > -1) window.dcTrack("whatsapp_click", { page: location.pathname });
  });

  function start() {
    var c = read();
    if (c === "granted") loadGA();
    else if (c === "denied") window["ga-disable-" + GA_ID] = true;
    else open();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
