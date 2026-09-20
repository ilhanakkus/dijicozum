#!/bin/bash
# Logo SVG'lerinden PNG, sekme simgesi ve paylaşım görseli (og-image) üretir.
# Gerekli: Google Chrome. Kullanım: bash tools/export_pngs.sh path/to/PlusJakartaSans-ExtraBold.ttf
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FONT="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
L="$ROOT/assets/logo"
mkdir -p "$L/png"
TMP="$(mktemp -d)"

# shot <html-icerik> <genişlik> <yükseklik> <çıktı.png> [arka plan]
shot() {
  printf '%s' "<html><body style='margin:0;overflow:hidden'>$1</body></html>" > "$TMP/p.html"
  "$CH" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files \
    --default-background-color="${5:-00000000}" --window-size="$2,$3" \
    --screenshot="$4" "file://$TMP/p.html" >/dev/null 2>&1
}
img() { echo "<img src='file://$L/$1' style='display:block;width:${2}px;height:${3}px'>"; }

# Şeffaf logolar (4x)
shot "$(img logo-a.svg 800 176)"      800 176 "$L/png/logo-a.png"
shot "$(img logo-a-dark.svg 800 176)" 800 176 "$L/png/logo-a-dark.png"
shot "$(img logo-c.svg 800 224)"      800 224 "$L/png/logo-c.png"     # yükseklik oranı 1.4
shot "$(img logo-c-dark.svg 800 224)" 800 224 "$L/png/logo-c-dark.png"

# Marka başvurusu için beyaz zeminli, siyah-beyaz sürümler
shot "$(img logo-a-mono.svg 1200 264)" 1200 264 "$L/png/logo-a-mono-beyaz-zemin.png" ffffffff
shot "$(img logo-c-mono.svg 1200 336)" 1200 336 "$L/png/logo-c-mono-beyaz-zemin.png" ffffffff

# Simgeler
shot "$(img icon.svg 512 512)" 512 512 "$L/png/icon-512.png"
shot "$(img icon.svg 32 32)"   32  32  "$ROOT/assets/favicon-32.png"
shot "$(img icon.svg 192 192)" 192 192 "$ROOT/assets/icon-192.png"
# iOS ana ekran simgesi: köşesiz, dolu kare
shot "<div style='width:180px;height:180px;background:#e8590c;display:grid;place-items:center'><svg width='96' height='96' viewBox='0 0 44 44'><circle cx='22' cy='19' r='7' fill='none' stroke='#fff' stroke-width='3.4'/><path d='M22 27v9' stroke='#fff' stroke-width='3.4' stroke-linecap='round'/></svg></div>" \
  180 180 "$ROOT/assets/apple-touch-icon.png" e8590cff

# Paylaşım görseli 1200x630
shot "<style>@font-face{font-family:PJS;font-weight:800;src:url('file://$FONT')}
body{font-family:PJS,system-ui}</style>
<div style='width:1200px;height:630px;background:#fbf8f3;display:flex;flex-direction:column;justify-content:center;padding:0 96px;box-sizing:border-box'>
<img src='file://$L/logo-a.svg' style='width:420px;height:92px;margin-bottom:54px'>
<div style='font-family:PJS;font-weight:800;font-size:72px;line-height:1.08;letter-spacing:-.03em;color:#0f172a;max-width:980px'>Dijital ihtiyaçlarınız için<br><span style='color:#e8590c;white-space:nowrap'>tek adres.</span></div>
<div style='font-family:system-ui,sans-serif;font-size:30px;color:#5b6474;margin-top:28px'>Web sitesi · Mobil uygulama · Sipariş · Randevu · Yapay zeka asistanı</div>
</div>" 1200 630 "$ROOT/assets/og-image.png" fbf8f3ff

rm -rf "$TMP"
ls -la "$L/png" "$ROOT"/assets/*.png
