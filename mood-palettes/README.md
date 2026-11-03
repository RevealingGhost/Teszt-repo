# Mood Palettes

Design sablon adatvizualizációhoz: 3 hangulatpaletta, mindegyik világos és sötét módban.
Az alapelv: **az első két szín adja a hangulatot, az akcentus a személyiséget** (60% felület · 30% hangulatszín · 10% akcentus).

| Téma | Hangulatszín 1 | Hangulatszín 2 | Akcentus | Mire |
|---|---|---|---|---|
| Citrus | Mandarin Orange `#FD550A` | Forest Green `#015D47` | Crest Yellow `#E0F354` | kategória-review, friss áru, promó |
| Electric | Onyx Black `#01010D` | Electric Indigo `#6331FB` | Tropical Mint `#88F9C0` | e-commerce, app, digitális KPI-ok |
| Visionary | Seal Blue `#DBF2FC` | Navy Blue `#072D59` | Crimson Pink `#FD6E88` | vezetői, pénzügyi, stratégiai riport |

## Fájlok

| Fájl | Mire |
|---|---|
| `powerbi/*.json` | Power BI téma: Nézet → Témák → Téma keresése |
| `css/mood-palettes.css` | CSS tokenek: `<html data-palette="electric" data-theme="dark">` |
| `python/mood_palettes.py` | matplotlib + plotly: `from mood_palettes import use; use("visionary")` |
| `tokens.json` | Platformfüggetlen token-forrás (minden más ebből készült) |
| `kombinacios-labor.md` | Mind a 36 színpár és mind a 18 szereposztás mérési eredménye |

## Színhasználat röviden

- **1 sorozat:** `series[0]`. **Kiemelés:** `highlight` egy elemre, a többi `deemph`.
- **Több sorozat:** `series` fix sorrendben (max. 6, felette „Egyéb”). Szórásdiagramon max. 3.
- **Mennyiség:** `seq` (7 lépcső). **Előjel / YoY:** `div` (7 lépcső, a 4. a semleges).
- **Szöveg sosem series-színű.** Változás: ▲/▼ + előjel + `text-good` / `text-bad`.
- Az akcentus eredeti hexe csak a `band` sávon vagy sötét felületen áll meg. Világos felületen a `highlight` lépcsőt használd.

Minden kategorikus sorrend színtévesztés-szimulációval validált (protanópia/deuteranópia, szomszédos CVD ΔE ≥ 8, normál ΔE ≥ 15, ≥ 3:1 kontraszt), mind a 6 téma-módban.
