<!--TO VIEW THE DOCUMENT CORRECTLY: USE LINE WRAP METHOD "NO WRAP"-->
<!--   Lines within these brackets are invisible and guides you   -->

# Localisation
This repository is for the translation of OpenRCT2 into other languages.<br/>
For the main development and codebase of OpenRCT2, visit [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2).

OpenRCT2's base language is English (UK), this is updated and maintained in the main repository.<br/>
Other languages are maintained in this repository.<br/>
Changes to the master branch are merged into the develop branch of OpenRCT2/OpenRCT2 every day at 4:00 AM UTC.

### Chat
| Language | Non Developer | Developer | Localisation |
|----------|---------------|-----------|--------------|
| English | [![Discord](https://img.shields.io/badge/discord-general-blue.svg)](https://discord.gg/ZXZd8D8) | [![Discord](https://img.shields.io/badge/discord-development-yellowgreen.svg)](https://discord.gg/fsEwSWs) | [![Discord](https://img.shields.io/badge/discord-localisation-green.svg)](https://discord.gg/sxnrvX9) |
| Nederlands | [![Discord](https://img.shields.io/badge/discord-general-blue.svg)](https://discord.gg/cQYSXzW) | | |


### Build Status
[![AppVeyor](https://ci.appveyor.com/api/projects/status/fkf22bp6tw8lxg6m?svg=true)](https://ci.appveyor.com/project/OpenRCT2/localisation)

To contribute to the translation of OpenRCT2, you will need to fork this repository.<br/>
This allows you to edit and push changes of files to your fork so that you can then open a pull request.<br/>
For more information, visit GitHub's official [forking guide](https://guides.github.com/activities/forking/).

### Creating a new language
If you want to begin translating OpenRCT2 for a new language, create a new file in the data directory with the correct two letter [language](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes#Partial_ISO_639_table) and [country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Decoding_table) (e.g. `cs-CZ`), then paste the contents of the [en-GB](https://github.com/OpenRCT2/OpenRCT2/blob/develop/data/language/en-GB.txt) file into it and start translating the strings.

### Maintainers & Maintaining languages
In each commit you create regarding a language file change, start the commit description (aka message) with the language and country code you're translating into, discussed in the previous paragraph (`cs-CZ`, `es-ES`, etc) (i.e. `git commit -m "es-ES: Description of the commit"` )

As this project always are moving forward, new strings get added from time to time which means they need to be added to the language files and be translated. All the new strings that are being added can be found in ['issues'](https://github.com/OpenRCT2/Localisation/issues) on the localisation webpage here on GitHub. To be a maintainer means that you have to add the new strings found on the issues page into the language you're translating in numerical order.

If you want to become a maintainer, tell us what language you will be maintaining on [Discord](https://discord.gg/sxnrvX9).

### Checking & testing strings in-game
You can always test the translated strings in-game before publishing a pull request. This can be especially handy to see if the strings fits the window.<br/>
To do this, go to the directory where OpenRCT2 resides (not to be confused with the directory where it saves your parks and config!), then go to `data/language` and replace the existing file with your updated version.

### Language Status
| Newest strings can be found in [issues](https://github.com/OpenRCT2/Localisation/issues) |
| -----------------------------------------------------------------------------------------|

| Language                                                                                                                                      | Maintainer |
|-----------------------------------------------------------------------------------------------------------------------------------------------| ---------- |
| [![](https://img.shields.io/badge/ar--EG-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ar-EG.txt) | [OmarAglan](https://github.com/OmarAglan)          |
| [![](https://img.shields.io/badge/ca--ES-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ca-ES.txt) | [J0anJosep](https://github.com/J0anJosep)          |
| [![](https://img.shields.io/badge/da--DK-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/da-DK.txt) | [LPSGizmo](https://github.com/LPSGizmo)          |
| [![](https://img.shields.io/badge/de--DE-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/de-DE.txt) | [Wuzzy2](https://github.com/Wuzzy2), [Gr33ndev](https://github.com/gr33ndev)        |
| [![](https://img.shields.io/badge/en--GB-maintained-green.svg)](https://github.com/OpenRCT2/OpenRCT2/blob/develop/data/language/en-GB.txt   ) | -Anyone-                                           |
| [![](https://img.shields.io/badge/eo--ZZ-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/eo-ZZ.txt)  | [tellovishous](https://github.com/tellovishous) |
| [![](https://img.shields.io/badge/es--ES-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/es-ES.txt) | [dimateos](https://github.com/dimateos) 		|
| [![](https://img.shields.io/badge/fi--FI-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/fi-FI.txt) | [groenroos](https://github.com/groenroos)          |
| [![](https://img.shields.io/badge/fr--FR-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/fr-FR.txt) | [rmnvgr](https://github.com/rmnvgr) |
| [![](https://img.shields.io/badge/it--IT-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/it-IT.txt) | [LucaRed](https://github.com/LucaRed)              |
| [![](https://img.shields.io/badge/ko--KR-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ko-KR.txt) | [telk5093](https://github.com/telk5093)            |
| [![](https://img.shields.io/badge/nb--NO-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/nb-NO.txt) | [Mmmmulder](https://github.com/Mmmmulder)            |
| [![](https://img.shields.io/badge/nl--NL-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/nl-NL.txt) | [Gymnasiast](https://github.com/Gymnasiast )      |
| [![](https://img.shields.io/badge/pl--PL-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/pl-PL.txt) | [marcinkunert](https://github.com/marcinkunert) |
| [![](https://img.shields.io/badge/pt--BR-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/pt-BR.txt) | [Tupaschoal](https://github.com/Tupaschoal)      |
| [![](https://img.shields.io/badge/uk--UA-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/uk-UA.txt) | [CsyeCokTheSolly](https://github.com/CsyeCokTheSolly) |
| [![](https://img.shields.io/badge/zh--CN-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/zh-CN.txt) | [LPR-Michael](https://github.com/LPR-Michael), [mrmagic2020](https://github.com/mrmagic2020) |
| [![](https://img.shields.io/badge/zh--TW-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/zh-TW.txt) | [daihakken](https://github.com/daihakken)         |
| Not maintained <!-- Languages that are outdated with strings missing from OpenRCT2/vanilla--> ||
| [![](https://img.shields.io/badge/hu--HU-outdated-yellow.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/hu-HU.txt) ||
| [![](https://img.shields.io/badge/sv--SE-outdated-yellow.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/sv-SE.txt) ||
| [![](https://img.shields.io/badge/cs--CZ-outdated-red.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/cs-CZ.txt) ||
| [![](https://img.shields.io/badge/ja--JP-outdated-red.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ja-JP.txt) ||
| [![](https://img.shields.io/badge/ru--RU-outdated-red.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ru-RU.txt) ||
| [![](https://img.shields.io/badge/tr--TR-outdated-red.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/tr-TR.txt) ||

Note:  The status bars can be inaccurate & some maintainers can be more inactive than others.<br/>
Anyone can still contribute to the languages.

#### Languages that inherit from others

These languages only need strings if they differ from the one they are inheriting from

| Language | Inherits from | Maintainer |          
| -------- | ------------- | ---------- |
| [![](https://img.shields.io/badge/en--US-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/en-US.txt) | en-GB |  |
| [![](https://img.shields.io/badge/fr--CA-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/fr-CA.txt) | fr-FR | [TheClaudeQC](https://github.com/TheClaudeQC) |

### Questions & Support

If you have any question or issues, you can always ask us on [Discord](https://discord.gg/sxnrvX9).

### Checking Translation Integrity

We have an action that automatically runs on every Pull Request and reports, for every supported language:

- If there are any strings left to translate
- If there are any strings that do not need translation
- If there are any strings that might not have been translated, as they are the same

The script is on the repository and can be run locally if one wants to anticipate the results, by doing:

```
python .github\workflows\translation_check.py -r <path to en-GB.txt> -m <path to data/language folder on master branch> -b <path to data/language folder on your branch>
```

Note that `-b` and `-m` can use the same argument if you don't want differential analysis.

You can use the `--help` switch to read more about what each switch does.
