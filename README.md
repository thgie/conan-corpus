# Conan: The Corpus
This corpus was made to assist the visual analysis of Conan, a character created by Robert E. Howard. The focus is on the visuality of digital games from the 80ies. What unites them is their visual reference to Conan. This inquiry was initiated via another analysis of the digital game Ball Raider (1987), whose start screen features a reference to He-Man from Masters of the Universe, a franchise inspired by Conan.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8315806.svg)](https://doi.org/10.5281/zenodo.8315806)

Notes on the process, especially the close reading, can be found [on my PhD wiki](https://phd.thgie.ch/notes/Bare%20Chested%20Men.html).

## Methodology
- Design rhetoric on the [visual material](#visual-material)
- [Corpus analysis](#corpus-analysis) of original Conan stories

## Games
The following games were analysed through this corpus and inquiry:

- Barbarian: The Ultimate Warrior (1987)
- Barbarian II: The Dungeon of Drax (1988)
- Dragonslayer (1988, unreleased)
- Torvak the Warrior (1990)
- Conan the Cimmerian (1991)

## Visual material
An overview of the covers of all media can be browsed under [https://omeka.unibe.ch/s/procedural-visuality/item-set/9186](https://omeka.unibe.ch/s/procedural-visuality/item-set/9186?sort=dcterms%3Acreated+asc). Besides this collection, the visual material includes:

- Covers of the original publications of the stories such as magazines, books and comics
- Film posters of the Conan movies
- Covers, promos and screenshots of the digital games packaging

## Corpus analysis
### Textual analysis
In order to backtrace the visuality to the original narrative, 17 of the original stories by Robert E. Howard were analysed for visual descriptions of Conan. The python script `main.py` uses spaCy to walk through the text, search for `Conan` and then extracts the sentence's adjectives. Not all are related to visuality, or to Conan, and not all instances of Conan can be captured liked this. Sentences that refer to Conan through `he is/was` are left out, for example. The present approach still delivers enough material to get a rough idea of how Conan was visually imagined.

The cleaning of the text could be improved, `black-haired` is split into `black` and `haired` for example.

### Visual analysis
In a first attempt to distant read the covers, I analysed them through Google's Vision API and [Memespector-GUI](https://github.com/jason-chao/memespector-gui).

- [Tropy export of the covers](covers/)
- [Google Vision API output](covers_vision_api/)