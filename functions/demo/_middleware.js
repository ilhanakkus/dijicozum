// Kampanya linklerinden gelen demo açılışlarını sayar (çerez onayından bağımsız).
// Linkte utm_source varsa işletme adı (kn) ve kaynak ntfy.sh konusuna bildirim olarak gider.
// Ziyaretçiye ait kişisel veri (IP, cihaz vb.) gönderilmez.
const TOPIC = "dijicozum-1d976faaf181";

export async function onRequest(context) {
  const res = await context.next();
  try {
    const url = new URL(context.request.url);
    const src = url.searchParams.get("utm_source");
    const isPage = context.request.method === "GET" && !/\.(js|css|png|jpe?g|svg|ico|webp|woff2?)$/i.test(url.pathname);
    const ua = context.request.headers.get("user-agent") || "";
    const bot = !ua || /whatsapp|facebookexternalhit|facebot|meta-externalagent|telegrambot|twitterbot|slackbot|discordbot|linkedinbot|googlebot|bingbot|bot\b|crawler|spider|preview|curl|python|wget|headless/i.test(ua);
    if (src && isPage && !bot && !url.searchParams.has("internal")) {
      const kn = url.searchParams.get("kn") || "(isimsiz)";
      const demo = url.pathname.replace(/^\/demo\//, "");
      const dev = /mobile|android|iphone/i.test(ua) ? "mobil" : "masaüstü";
      const meta = [dev, src, url.searchParams.get("utm_medium"), url.searchParams.get("utm_content")].filter(Boolean).join(" / ");
      context.waitUntil(
        fetch("https://ntfy.sh/" + TOPIC, {
          method: "POST",
          headers: { Tags: "eyes", "Content-Type": "text/plain; charset=utf-8" },
          body: "Demo açıldı: " + kn + " | " + demo + " | " + meta,
        })
      );
    }
  } catch (e) {}
  return res;
}
