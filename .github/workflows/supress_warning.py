# Dictionary of fields that should not appear in translation check warnings
# per each language
#
# each maintainer kindly PR's STR_nnnn he has checked and found being reported
# incorectly


SUPRESS_WARNING = dict()

# example
# SUPRESS_WARNING['qq-JJ'] = ['STR_0123', 'STR_5678', 'STR_8900']
# 2996 - 3009 are COLOR-ABC strings used in Banner window
# japanese and ukrainian use different scripts (hiragana and cyrillic)

SUPRESS_WARNING['ar-EG'] = []
SUPRESS_WARNING['ca-ES'] = []
SUPRESS_WARNING['cs-CZ'] = []
SUPRESS_WARNING['da-DK'] = []
SUPRESS_WARNING['de-DE'] = []
SUPRESS_WARNING['en-US'] = []
SUPRESS_WARNING['eo-ZZ'] = []
SUPRESS_WARNING['es-ES'] = []
SUPRESS_WARNING['fi-FI'] = []
SUPRESS_WARNING['fr-CA'] = []
SUPRESS_WARNING['fr-FR'] = []
SUPRESS_WARNING['gl-ES'] = []
SUPRESS_WARNING['hu-HU'] = []
SUPRESS_WARNING['it-IT'] = []
SUPRESS_WARNING['ja-JP'] = ['STR_2996', 'STR_2997', 'STR_2998', 'STR_2999',
                            'STR_3000', 'STR_3001', 'STR_3002', 'STR_3003',
                            'STR_3004', 'STR_3005', 'STR_3006', 'STR_3007',
                            'STR_3008', 'STR_3009']
SUPRESS_WARNING['ko-KR'] = []
SUPRESS_WARNING['nb-NO'] = []
SUPRESS_WARNING['nl-NL'] = []
SUPRESS_WARNING['pl-PL'] = []
SUPRESS_WARNING['pt-BR'] = []
SUPRESS_WARNING['ru-RU'] = []
SUPRESS_WARNING['sv-SE'] = []
SUPRESS_WARNING['tr-TR'] = []
SUPRESS_WARNING['uk-UA'] = ['STR_2996', 'STR_2997', 'STR_2998', 'STR_2999',
                            'STR_3000', 'STR_3001', 'STR_3002', 'STR_3003',
                            'STR_3004', 'STR_3005', 'STR_3006', 'STR_3007',
                            'STR_3008', 'STR_3009']
SUPRESS_WARNING['vi-VN'] = []
SUPRESS_WARNING['zh-CN'] = []
SUPRESS_WARNING['zh-TW'] = []
