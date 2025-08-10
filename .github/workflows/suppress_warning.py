"""
Dictionary of fields that should not appear in translation check warnings
per each language

each maintainer kindly PR's STR_nnnn he has checked and found being reported
incorectly
"""

SUPPRESS_WARNING = dict()
"""
This gets imported in translation_check.py, which checks it against all
languages present in repo.

Please note: Failing to add new language in this dictionary will cause
KeyError being raised in translation_check.py and therefore it
will break GitHub Action job

Example of population:
SUPPRESS_WARNING['qq-JJ'] = ['STR_0123', 'STR_5678', 'STR_8900']

2996 - 3009 are COLOR-ABC strings used in Banner window and were pre-added
for japanese and ukrainian which use different scripts (hiragana and cyrillic)
"""

SUPPRESS_WARNING['ar-EG'] = []
SUPPRESS_WARNING['ca-ES'] = []
SUPPRESS_WARNING['cs-CZ'] = []
SUPPRESS_WARNING['da-DK'] = []
SUPPRESS_WARNING['de-DE'] = []
SUPPRESS_WARNING['en-US'] = []
SUPPRESS_WARNING['eo-ZZ'] = []
SUPPRESS_WARNING['es-ES'] = []
SUPPRESS_WARNING['fi-FI'] = []
SUPPRESS_WARNING['fr-CA'] = []
SUPPRESS_WARNING['fr-FR'] = []
SUPPRESS_WARNING['gl-ES'] = []
SUPPRESS_WARNING['hu-HU'] = []
SUPPRESS_WARNING['it-IT'] = []
SUPPRESS_WARNING['ja-JP'] = ['STR_2996', 'STR_2997', 'STR_2998', 'STR_2999',
                             'STR_3000', 'STR_3001', 'STR_3002', 'STR_3003',
                             'STR_3004', 'STR_3005', 'STR_3006', 'STR_3007',
                             'STR_3008', 'STR_3009']
SUPPRESS_WARNING['ko-KR'] = []
SUPPRESS_WARNING['nb-NO'] = []
SUPPRESS_WARNING['nl-NL'] = []
SUPPRESS_WARNING['pl-PL'] = []
SUPPRESS_WARNING['pt-BR'] = []
SUPPRESS_WARNING['ru-RU'] = []
SUPPRESS_WARNING['sv-SE'] = []
SUPPRESS_WARNING['tr-TR'] = []
SUPPRESS_WARNING['uk-UA'] = ['STR_2996', 'STR_2997', 'STR_2998', 'STR_2999',
                             'STR_3000', 'STR_3001', 'STR_3002', 'STR_3003',
                             'STR_3004', 'STR_3005', 'STR_3006', 'STR_3007',
                             'STR_3008', 'STR_3009']
SUPPRESS_WARNING['vi-VN'] = []
SUPPRESS_WARNING['zh-CN'] = []
SUPPRESS_WARNING['zh-TW'] = []
