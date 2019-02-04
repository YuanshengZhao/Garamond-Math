<!-- README for CTAN -->
# Garamond-Math Ver. 2019-02-05

Garamond-Math is an open type math font matching the [EB Garamond (Octavio Pardo)](https://github.com/octaviopardo/EBGaramond12/) and [EB Garamond (Georg Mayr-Duffner)](https://github.com/georgd/EB-Garamond).
Many mathematical symbols are derived from other fonts (see below), others are made from scratch. The metric is generated with a python script.

## Notes

- *Important notes for this version* 
    - Fixed various wrong mappings, add italic h.var.
    - Fraktur is (temporarily) not supported, Because (1) Originally they come from  [TeX Gyre Termes Math](http://www.gust.org.pl/projects/e-foundry/tg-math/) and GUST and OFL are not completely compatible; (2) The glyphs are not modified at all, so there is in principle no need to include it (one can use `range` option in `unicode-math`) 
    - Default `\mathbb` is swapped with original `StylisticSet=1`.

- *Blackboard* (`\mathbb`):
    - Glyphs based on [XITS Math](https://github.com/khaledhosny/xits) are also available. However, the crossings and endpoints of strokes are rounded to fit the style of EB Garamond. They can be accessed via `StylisticSet=1`.

- *Script* (`\mathscr`):
    - Default glyphs are from XITS Math. The weight (especially for bold) and crossings and endpoints of strokes are modified.
    - CM glyphs with a little modification are also available with `StylisticSet=3`

- *Sans serif, typewriter*: from [Libertinus Math](https://github.com/khaledhosny/libertinus). This font has low x-height as Garamond do, though the bold italic Greeks are unavailable.

- *Other glyphs available*: display `\int`, `\sum`, `\underbrace`, big delimiters, `\widehat`, arrows, binary relations derived, circled characters, etc, from the original EB Garamond.

- Stylistic sets: (`StylisticSet={#1,#2,...}` in [`unicode-math`](https://ctan.org/pkg/unicode-math?lang=en) package)

    - `1` → XITS Blackboard `\mathbb`.
    - `2` → Curved `\partial`, which is in style with almost all other fonts.
    - `3` → CM `\mathcal` (lowercase unavailble)
    - `4` → Use semi-bold for `\symbf`
    - `5` → Use extra-bold for `\symbf`
    - `6` → horizontal "bar" for `\hbar`
    - `7` → `\int` variant
    - `8` → Garamond-compatible `\mathcal` (experimental)
    - `9` → `\tilde` variant
    - `10` → out-bending italic h

## Known Issue
- Currently only usable for `XeTeX` (with `unicode-math`). OTHER ENGINES (EX. `LuaTeX`, `MS Word`) WILL PRODUCE VERY BAD SPACINGS.
- Various spacing problems. Though math fonts technically should not be kerned, some pairs looks very ugly (Ex. `VA`); sometimes sub/superscript may also have same problem.
- Fake optical size. EB Garamond does not contain a complete set of glyphs (normal + bold + optical size of both weights). The "optical size `ssty`" is made by interpolating different weights at the present (without this, the double script is too thin to be readable). 

## Technical Staff
- This font is still under development, any components might be updated at any time. Issues, bug reports, forks and other contributions are welcome.

## License

This Font Software is licensed under the [SIL Open Font License](http://scripts.sil.org/OFL), Version 1.1.


