# Garamond-Math

An OTF math font matching the [EB Garamond](https://github.com/octaviopardo/EBGaramond12/).

## Notes

- *Blackboard* (`\mathbb`): glyphs based on [XITS Math](https://github.com/khaledhosny/xits) will be loaded by default. However, the crossings and endpoints of strokes are rounded to fit the style of EB Garamond. `StylisticSet=1` will load the EB-Garamond-based glyphs (as in the sample below).

- *Script* (`\mathscr`): from XITS Math. The weight (especially for bold) and crossings and endpoints of strokes are modified.

- *Sans serif, typewriter*: from [Libertinus Math](https://github.com/khaledhosny/libertinus). This font has low x-height as Garamond do, though the bold italic greeks are unavailable.

- *Fraktur, binary relations*: from [TeX Gyre Termes Math](http://www.gust.org.pl/projects/e-foundry/tg-math/).  Binary relations are modified on the crossings and endpoints of strokes.

- *Arrows*: combination of TeX Gyre Termes math (tail) and EB Garamond (head).

- *Other glyphs available*: display `\int`, `\sum`, `\underbrace`, big delimiters, `\widehat`, etc.

- Part of TeX files are from [FiraMath](https://github.com/Stone-Zeng/FiraMath) repository.

- This font is still under development, any components might be updated at any time.

## Sample

![sample](sample.svg)

## License

This Font Software is licensed under the [SIL Open Font License](http://scripts.sil.org/OFL), Version 1.1.
