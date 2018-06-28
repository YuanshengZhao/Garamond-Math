# Garamond-Math

An open type math font matching the [EB Garamond](https://github.com/octaviopardo/EBGaramond12/).

## Notes

- *Blackboard* (`\mathbb`): glyphs based on [XITS Math](https://github.com/khaledhosny/xits) will be loaded by default. However, the crossings and endpoints of strokes are rounded to fit the style of EB Garamond. EB-Garamond based glyphs are also available (see below).

- *Script* (`\mathscr`): from XITS Math. The weight (especially for bold) and crossings and endpoints of strokes are modified.

- *Sans serif, typewriter*: from [Libertinus Math](https://github.com/khaledhosny/libertinus). This font has low x-height as Garamond do, though the bold italic greeks are unavailable.

- *Fraktur*: from [TeX Gyre Termes Math](http://www.gust.org.pl/projects/e-foundry/tg-math/). The design of some other glyphs are also inspired from this font.

- *Other glyphs available*: display `\int`, `\sum`, `\underbrace`, big delimiters, `\widehat`, more arrows and binary relations derived from the original EB Garamond.

- Stylistic sets: `StylisticSet={#1,#2,...}`

    - `1` -> Garamond based Blackboard `\mathbb`.
    - `2` -> Curved `\partial` (see the sample below), which is in style with many other fonts, like CM, XITS, TeX Gyre, etc.
    - `3` -> CM `\mathcal` (lowercase unavailble)
    - `4` -> Use semi-bold for `\symbf`
    - `5` -> Use extra-bold for `\symbf`
    - `6` -> horizontal "bar" for `\hbar`

---
- Part of TeX files are from [FiraMath](https://github.com/Stone-Zeng/FiraMath) repository.

- This font is still under development, any components might be updated at any time. Issues, bug reports and other suggestions are welcome.

## Sample

![sample](images/sample.svg)

## License

This Font Software is licensed under the [SIL Open Font License](http://scripts.sil.org/OFL), Version 1.1.
