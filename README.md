# Localisation
This repository is for the translation of OpenRCT2 into other languages.
For the main development and codebase of OpenRCT2, visit [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2).

OpenRCT2's base language is English (UK), this is updated and maintained in the main repository.
Other languages are maintained in this repository.
Changes to the master branch are merged into the develop branch of OpenRCT2/OpenRCT2 every day at 4:00 AM UTC.

### Build Status
[![AppVeyor](https://ci.appveyor.com/api/projects/status/muc7co3bxvcayp5t?svg=true)](https://ci.appveyor.com/project/IntelOrca/localisation)

### Chat
[![Gitter](https://img.shields.io/badge/gitter-general-blue.svg)](https://gitter.im/OpenRCT2/OpenRCT2/non-dev)<br />
[![Gitter](https://img.shields.io/badge/gitter-localisation-green.svg)](https://gitter.im/OpenRCT2/Localisation)<br />
[![Gitter](https://img.shields.io/badge/gitter-development-yellowgreen.svg)](https://gitter.im/OpenRCT2/OpenRCT2)

### Language Status
| [![](https://img.shields.io/badge/en--GB-maintained-green.svg)](https://github.com/OpenRCT2/OpenRCT2/blob/develop/data/language/en-GB.txt   ) | [![](https://img.shields.io/badge/it--IT-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/it-IT.txt) | [![](https://img.shields.io/badge/zh--TW-maintained-green.svg      )](https://github.com/OpenRCT2/Localisation/blob/master/data/language/zh-TW.txt) |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [![](https://img.shields.io/badge/en--US-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/en-US.txt) | [![](https://img.shields.io/badge/pt--BR-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/pt-BR.txt) | [![](https://img.shields.io/badge/ja--JP-outdated-yellow.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ja-JP.txt) |
| [![](https://img.shields.io/badge/cs--CZ-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/cs-CZ.txt) | [![](https://img.shields.io/badge/es--ES-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/es-ES.txt) | [![](https://img.shields.io/badge/pl--PL-outdated-yellow.svg       )](https://github.com/OpenRCT2/Localisation/blob/master/data/language/pl-PL.txt) |
| [![](https://img.shields.io/badge/nl--NL-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/nl-NL.txt) | [![](https://img.shields.io/badge/sv--SE-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/sv-SE.txt) | [![](https://img.shields.io/badge/fi--FI-outdated-red.svg          )](https://github.com/OpenRCT2/Localisation/blob/master/data/language/fi-FI.txt) |
| [![](https://img.shields.io/badge/fr--FR-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/fr-FR.txt) | [![](https://img.shields.io/badge/ko--KR-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ko-KR.txt) | [![](https://img.shields.io/badge/hu--HU-outdated-red.svg          )](https://github.com/OpenRCT2/Localisation/blob/master/data/language/hu-HU.txt) |
| [![](https://img.shields.io/badge/de--DE-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/de-DE.txt) | [![](https://img.shields.io/badge/zh--CN-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/zh-CN.txt) | [![](https://img.shields.io/badge/ru--RU-outdated-red.svg          )](https://github.com/OpenRCT2/Localisation/blob/master/data/language/ru-RU.txt) |
| [![](https://img.shields.io/badge/nb--NO-maintained-green.svg)](https://github.com/OpenRCT2/Localisation/blob/master/data/language/nb-NO.txt) | | |

## Contributing
To contribute to the translation of OpenRCT2, you will need to fork this repository.
This allows you to edit and push changes of files to your fork so that you can then open a pull request.
For more information, visit GitHub's official [forking guide](https://guides.github.com/activities/forking/).

### Creating a new language
If you want to begin translating OpenRCT2 for a new language, create a new file in the data directory with the correct two letter [language](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes#Partial_ISO_639_table) and [country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Decoding_table) (e.g. `cs-CZ`), then paste the contents of the [en-GB](https://github.com/OpenRCT2/OpenRCT2/blob/develop/data/language/en-GB.txt) file into it and start translating the strings.
