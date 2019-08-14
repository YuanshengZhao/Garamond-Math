# Garamond-Math Ver. 2019-05-02

Garamond-Math is an open type math font matching the [EB Garamond (Octavio Pardo)](https://github.com/octaviopardo/EBGaramond12/) and [EB Garamond (Georg Mayr-Duffner)](https://github.com/georgd/EB-Garamond).
Many mathematical symbols are derived from other fonts, others are made from scratch.

## Notes

- Referred fonts:  [XITS Math](https://github.com/khaledhosny/xits), [Libertinus Math](https://github.com/khaledhosny/libertinus), Computer Modern, [Asana Math](https://www.ctan.org/pkg/asana-math).

- Stylistic sets: (`StylisticSet={#1,#2,...}` in [`unicode-math`](https://ctan.org/pkg/unicode-math?lang=en) package)
    - `1` → XITS Blackboard `\mathbb`.
    - `2` → Curved `\partial`.
    - `3` → CM `\mathcal` (no lowercase)
    - `4` → Use semi-bold for `\symbf`
    - `5` → Use extra-bold for `\symbf`
    - `6` → horizontal "bar" for `\hbar`
    - `7` → `\int` variant
    - `8` → A `\mathcal` variant (experimental, no boldface)
    - `9` → `\tilde` variant
    - `10` → out-bending italic h

- Part of TeX files are from [FiraMath](https://github.com/Stone-Zeng/FiraMath) repository.

- This font is still under development, there should be some bugs, use it with caution! Issues, bug reports, forks and other contributions are very welcome.

## Known Issue
- Various spacing problems. Though math fonts technically should not be kerned, some pairs looks very ugly (Ex. `VA`); sometimes sub/superscript may also have same problem.
- Fake optical size. EB Garamond does not contain a complete set of glyphs (normal + bold + optical size of both weights). The "optical size `ssty`" is made by interpolating different weights at the present (without this, the double script is too thin to be readable). 

## How to Build from Source
- The `sfdir` here is NOT ready to build! 
- To build the font from source, please install [FontForge](https://github.com/fontforge/fontforge) and Python 3.
- Open `./scripts/MetricGen.ipynb`, run all the codes before “codes for generating metrics”. For usage in MS Word, set `build4word=True` in the last cell to be run.
- On Windows, this should all work out, on other system, the `.bat` does not work, you should generate font from the generated `sfdir` with FontForge manually.
- Only when there is a major improvement will the `otf` file in the repository will be updated. And the file is built with `build4word=False`, so it may not be suitable to use in MS Word. 

## Sample

![sample](images/sample.svg)

## License

This Font Software is licensed under the [SIL Open Font License](http://scripts.sil.org/OFL), Version 1.1.
