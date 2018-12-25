# Garamond-Math

Garamond-Math is an open type math font matching the [EB Garamond (Octavio Pardo)](https://github.com/octaviopardo/EBGaramond12/) and [EB Garamond (Georg Mayr-Duffner)](https://github.com/georgd/EB-Garamond).
Many mathematical symbols are derived from other fonts (see below), others are made from scratch.

## Notes

- *Blackboard* (`\mathbb`):
    - glyphs based on [XITS Math](https://github.com/khaledhosny/xits) will be loaded by default. However, the crossings and endpoints of strokes are rounded to fit the style of EB Garamond.
    - EB-Garamond based glyphs are also available with `StylisticSet=1`.

- *Script* (`\mathscr`):
    - default glyphs are from XITS Math. The weight (especially for bold) and crossings and endpoints of strokes are modified.
    - CM glyphs with a little modification are also available with `StylisticSet=3`

- *Sans serif, typewriter*: from [Libertinus Math](https://github.com/khaledhosny/libertinus). This font has low x-height as Garamond do, though the bold italic greeks are unavailable.

- *Fraktur*: from [TeX Gyre Termes Math](http://www.gust.org.pl/projects/e-foundry/tg-math/). [There might be some license issues though, and should somehow be resolved (by using glyphs from other fonts, for example)]

- *Other glyphs available*: display `\int`, `\sum`, `\underbrace`, big delimiters, `\widehat`, arrows, binary relations derived, circled characters, etc, from the original EB Garamond.

- Stylistic sets: (`StylisticSet={#1,#2,...}` in [`unicode-math`](https://ctan.org/pkg/unicode-math?lang=en) package)

    - `1` → Garamond Blackboard `\mathbb`.
    - `2` → Curved `\partial` (see the sample below), which is in style with almost all other fonts.
    - `3` → CM `\mathcal` (lowercase unavailble)
    - `4` → Use semi-bold for `\symbf`
    - `5` → Use extra-bold for `\symbf`
    - `6` → horizontal "bar" for `\hbar`
    - `7` → `\int` variant
    - `8` → Garamond-compatible `\mathcal` (experimental)
    - `9` → `\tilde` variant

- Part of TeX files are from [FiraMath](https://github.com/Stone-Zeng/FiraMath) repository.

## Known Issue
- Currently only usable for `XeTeX` (with `unicode-math`). OTHER ENGINES (EX. `LuaTeX`, `MS Word`) WILL PRODUCE VERY BAD SPACINGS.
- Various spacing problems. Though math fonts technically should not be kerned, some pairs looks very ugly (Ex. `VA`); sometimes script also have same problem (Ex. `\partial_A`).
- Fake optical size. EG Garamond does not contain a complete set of glyphs (normal + bold + optical size of both weights). The "optical size `ssty`" is made by interpolating different weights at the present (without this, the double script is too thin to be readable). 

## Technical Staff
- To build the font from source, please install [FontForge](https://github.com/fontforge/fontforge). Installation on Linux system is strongly recommended.

- This font is still under development, any components might be updated at any time. Issues, bug reports, forks and other suggestions are welcome.

## Sample

![sample](images/sample.svg)

## License

This Font Software is licensed under the [SIL Open Font License](http://scripts.sil.org/OFL), Version 1.1.

