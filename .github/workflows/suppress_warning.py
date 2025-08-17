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
"""

SUPPRESS_WARNING['ar-EG'] = []
SUPPRESS_WARNING['ca-ES'] = []
SUPPRESS_WARNING['cs-CZ'] = []
SUPPRESS_WARNING['da-DK'] = []
SUPPRESS_WARNING['de-DE'] = []
SUPPRESS_WARNING['en-US'] = []
SUPPRESS_WARNING['eo-ZZ'] = ['STR_0839', 'STR_0840']
SUPPRESS_WARNING['es-ES'] = []
SUPPRESS_WARNING['fi-FI'] = []
SUPPRESS_WARNING['fr-CA'] = []
# fr-FR uses em dashes (—) instead of en dashes (-) for separators and must have a non-breaking space before colons
SUPPRESS_WARNING['fr-FR'] = ['STR_1165', 'STR_1333', 'STR_1334', 'STR_2781', 'STR_6229', 'STR_6230', 'STR_6231']
SUPPRESS_WARNING['gl-ES'] = []
SUPPRESS_WARNING['hu-HU'] = []
SUPPRESS_WARNING['it-IT'] = []
SUPPRESS_WARNING['ja-JP'] = []
SUPPRESS_WARNING['ko-KR'] = []
SUPPRESS_WARNING['nb-NO'] = []
SUPPRESS_WARNING['nl-NL'] = []
SUPPRESS_WARNING['pl-PL'] = []
SUPPRESS_WARNING['pt-BR'] = []
SUPPRESS_WARNING['ru-RU'] = []
SUPPRESS_WARNING['sv-SE'] = []
SUPPRESS_WARNING['tr-TR'] = []
SUPPRESS_WARNING['uk-UA'] = []
SUPPRESS_WARNING['vi-VN'] = []
SUPPRESS_WARNING['zh-CN'] = []
SUPPRESS_WARNING['zh-TW'] = []
