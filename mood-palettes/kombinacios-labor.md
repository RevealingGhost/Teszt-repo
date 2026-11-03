# Kombinációs labor

Ez a szekció a videó mind a 9 színét kipróbálja minden lehetséges párosításban és szerepben. Kétféle mérés fut: a **WCAG 2 kontrasztarány** (szöveg legalább 4.5:1, nagy szöveg és diagramjelölő legalább 3:1) és a **színtévesztés-szimuláció** a kategorikus sorrendekre. A *ComboLab* komponens ugyanezt élőben mutatja.

## 1. Mind a 36 színpár

A 9 színből 36 különböző pár képezhető. Az arány szimmetrikus, tehát mindegy, melyik a szöveg és melyik a háttér. Jelmagyarázat: **AAA** ≥ 7:1, **AA** ≥ 4.5:1 (folyószöveg), **AA nagy** ≥ 3:1 (24px+ szöveg, ikon, diagramjelölő), **—** csak dekorációra.

| Pár | Arány | Szint |
|---|---|---|
| Onyx Black × Seal Blue | 17,91:1 | AAA |
| Crest Yellow × Onyx Black | 16,92:1 | AAA |
| Onyx Black × Tropical Mint | 16,17:1 | AAA |
| Seal Blue × Navy Blue | 11,85:1 | AAA |
| Crest Yellow × Navy Blue | 11,20:1 | AAA |
| Tropical Mint × Navy Blue | 10,70:1 | AAA |
| Onyx Black × Crimson Pink | 7,67:1 | AAA |
| Forest Green × Seal Blue | 6,82:1 | AA |
| Forest Green × Crest Yellow | 6,44:1 | AA |
| Mandarin Orange × Onyx Black | 6,41:1 | AA |
| Forest Green × Tropical Mint | 6,15:1 | AA |
| Electric Indigo × Seal Blue | 5,39:1 | AA |
| Crest Yellow × Electric Indigo | 5,09:1 | AA |
| Navy Blue × Crimson Pink | 5,08:1 | AA |
| Electric Indigo × Tropical Mint | 4,86:1 | AA |
| Mandarin Orange × Navy Blue | 4,24:1 | AA nagy |
| Onyx Black × Electric Indigo | 3,32:1 | AA nagy |
| Forest Green × Crimson Pink | 2,92:1 | — |
| Mandarin Orange × Seal Blue | 2,80:1 | — |
| Mandarin Orange × Crest Yellow | 2,64:1 | — |
| Forest Green × Onyx Black | 2,63:1 | — |
| Mandarin Orange × Tropical Mint | 2,52:1 | — |
| Mandarin Orange × Forest Green | 2,44:1 | — |
| Seal Blue × Crimson Pink | 2,33:1 | — |
| Electric Indigo × Crimson Pink | 2,31:1 | — |
| Crest Yellow × Crimson Pink | 2,21:1 | — |
| Electric Indigo × Navy Blue | 2,20:1 | — |
| Tropical Mint × Crimson Pink | 2,11:1 | — |
| Mandarin Orange × Electric Indigo | 1,93:1 | — |
| Forest Green × Navy Blue | 1,74:1 | — |
| Onyx Black × Navy Blue | 1,51:1 | — |
| Forest Green × Electric Indigo | 1,27:1 | — |
| Mandarin Orange × Crimson Pink | 1,20:1 | — |
| Tropical Mint × Seal Blue | 1,11:1 | — |
| Crest Yellow × Seal Blue | 1,06:1 | — |
| Crest Yellow × Tropical Mint | 1,05:1 | — |

Összesen 15 pár bírja a folyószöveget (≥ 4.5:1), további 2 csak nagy szöveget és jelölőt (3–4.5:1), 19 pár pedig csak dekorációra jó.

## 2. Szereposztás palettán belül: mind a 18 permutáció

Mindhárom paletta 3 színe 6-féleképpen osztható ki a 60 / 30 / 10 szerepre. A táblázat azt méri, hogy a 30%-os szín olvasható-e a 60%-os felületen, és az akcentus kiugrik-e a felületből és a 30%-os színből is. ★ jelöli a videó eredeti sorrendjét, ◆ a dashboard band-jének kiosztását (a dashboard 60%-a ettől függetlenül egy semleges, a hangulatszínből tört felület).

| Paletta | 60% felület | 30% hangulat | 10% akcentus | 30 a 60-on | 10 a 60-on | 10 a 30-on | Ítélet |
|---|---|---|---|---|---|---|---|
| Citrus | Mandarin Orange | Forest Green | Crest Yellow ★ | 2,44 | 2,64 | 6,44 | kerülendő |
| Citrus | Mandarin Orange | Crest Yellow | Forest Green | 2,64 | 2,44 | 6,44 | kerülendő |
| Citrus | Forest Green | Mandarin Orange | Crest Yellow ◆ | 2,44 | 6,44 | 2,64 | feltételesen |
| Citrus | Forest Green | Crest Yellow | Mandarin Orange | 6,44 | 2,44 | 2,64 | feltételesen |
| Citrus | Crest Yellow | Mandarin Orange | Forest Green | 2,64 | 6,44 | 2,44 | feltételesen |
| Citrus | Crest Yellow | Forest Green | Mandarin Orange | 6,44 | 2,64 | 2,44 | feltételesen |
| Electric | Onyx Black | Electric Indigo | Tropical Mint ★ ◆ | 3,32 | 16,17 | 4,86 | működik |
| Electric | Onyx Black | Tropical Mint | Electric Indigo | 16,17 | 3,32 | 4,86 | működik |
| Electric | Electric Indigo | Onyx Black | Tropical Mint | 3,32 | 4,86 | 16,17 | működik |
| Electric | Electric Indigo | Tropical Mint | Onyx Black | 4,86 | 3,32 | 16,17 | működik |
| Electric | Tropical Mint | Onyx Black | Electric Indigo | 16,17 | 4,86 | 3,32 | működik |
| Electric | Tropical Mint | Electric Indigo | Onyx Black | 4,86 | 16,17 | 3,32 | működik |
| Visionary | Seal Blue | Navy Blue | Crimson Pink ★ ◆ | 11,85 | 2,33 | 5,08 | feltételesen |
| Visionary | Seal Blue | Crimson Pink | Navy Blue | 2,33 | 11,85 | 5,08 | feltételesen |
| Visionary | Navy Blue | Seal Blue | Crimson Pink | 11,85 | 5,08 | 2,33 | működik |
| Visionary | Navy Blue | Crimson Pink | Seal Blue | 5,08 | 11,85 | 2,33 | működik |
| Visionary | Crimson Pink | Seal Blue | Navy Blue | 2,33 | 5,08 | 11,85 | feltételesen |
| Visionary | Crimson Pink | Navy Blue | Seal Blue | 5,08 | 2,33 | 11,85 | feltételesen |

„Működik”: a hangulatszín és az akcentus is legalább 3:1 a felületen. „Feltételesen”: csak az egyik; a gyenge párt ne tedd egymás mellé szövegként vagy kis jelölőként. „Kerülendő”: egyik sem olvasható a felületen. Az akcentus és a hangulatszín viszonya (10 a 30-on) tájékoztató, mert dashboardon ritkán érintkeznek közvetlenül.

## 3. Mit tanultunk

- **Citrus.** A videó sorrendjében (narancs felület, zöld szöveg) a zöld a narancson csak 2,44:1. Plakáton hangulatos, dashboardon olvashatatlan. A sárga a zöldön viszont 6,44:1, ezért dashboardon a Forest Green lesz a band és az 1. sorozat, a Mandarin a kiemelés, a Crest Yellow pedig a band-on élő akcentus. A 60%-os felület egy meleg, majdnem fehér semleges szín, nem a narancs.
- **Electric.** Az Electric Indigo az Onyxon 3,32:1, ez csak nagy szövegre és jelölőre elég. A Tropical Mint az Onyxon 16,17:1, az Indigón 4,86:1: a menta a legbiztosabb akcentus a háromból. Világos módban a menta helyett annak sötétebb lépcsője (`highlight`) jelöl.
- **Visionary.** A Navy a Seal Blue-n 11,85:1, ez a legolvashatóbb alap a háromból. A videó CTA-gombján fehér szöveg áll a Crimson Pinken, ez csak 2,71:1. A rendszerben ezért az `on-accent` Navy (5,08:1).
- **Palettákon átívelő párok.** A legerősebb „remixek”: Onyx × Seal Blue 17,91:1, Onyx × Crest Yellow 16,92:1, Navy × Crest Yellow 11,20:1, Navy × Tropical Mint 10,70:1, Forest Green × Seal Blue 6,82:1. Ezek szabadon keverhetők szövegként is.
- **Ami sosem megy szövegként:** Mandarin × Crimson (1,20:1), Forest Green × Electric Indigo (1,27:1), Crest Yellow × Tropical Mint (1,05:1), Crest Yellow × Seal Blue (1,06:1), Tropical Mint × Seal Blue (1,11:1).

## 4. Kategorikus sorrendek színtévesztésre

A diagramokhoz mindhárom palettát hat színre bővítettük a paletta saját árnyalataiból, és minden lehetséges sorrendet végigpróbáltunk. Az alábbiak teljesítik az összes kaput: a világosság a mód sávján belül van, a króma legalább 0,10, szomszédos pároknál CVD ΔE ≥ 8 és normál ΔE ≥ 15, a kontraszt pedig legalább 3:1 a felületen.

| Téma | Sorrend | Legrosszabb szomszéd CVD ΔE (vil. / söt.) | Első 3 minden párban |
|---|---|---|---|
| Citrus | zöld › mandarin › kék › szilva › arany › türkiz | 8,6 / 11,2 | igen |
| Electric | indigó › menta › borostyán › magenta › égkék › korall | 8,1 / 8,3 | igen |
| Visionary | navy-kék › crimson › türkiz › ibolya › borostyán › égkék | 8,5 / 8,4 | igen |

A szekvenciális skálák (`seq-*`) egyetlen árnyalatból készültek, monoton világossággal. Ordinális használatnál a `seq-4`-től indulnak, mert a Citrus világos módban a `seq-3` éppen 2:1 alatt marad a felületen.
