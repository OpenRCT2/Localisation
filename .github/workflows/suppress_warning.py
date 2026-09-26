"""
Dictionary of fields that should not appear in translation check warnings
per each language.

Each maintainer kindly PRs STR_nnnn they have checked and found being reported
incorrectly.
"""

from collections import defaultdict

SUPPRESS_WARNING = defaultdict(list)
"""
This gets imported in translation_check.py, which checks it against all
languages present in the repo.

Note: Missing languages are automatically handled via defaultdict, so you 
only need to add entries here if a language has specific warnings to suppress.

Example of population:
SUPPRESS_WARNING['qq-JJ'] = ['STR_0123', 'STR_5678', 'STR_8900']
"""

SUPPRESS_WARNING['ca-ES'] = ['STR_3247', 'STR_6651', 'STR_6689', 'STR_6744']

SUPPRESS_WARNING['eo-ZZ'] = ['STR_0839', 'STR_0840']

# fr-FR uses em dashes (—) instead of en dashes (-) for separators and must have a non-breaking space before colons
SUPPRESS_WARNING['fr-FR'] = ['STR_1165', 'STR_1333', 'STR_1334', 'STR_2781', 'STR_6229', 'STR_6230', 'STR_6231']

# hu-HU needs to change order of {STRINGID}s for news and research to translate them properly.
SUPPRESS_WARNING['hu-HU'] = ['STR_2235', 'STR_2289']

# ko-KR needs to change order of {STRINGID}s for news and research to translate them properly. STR_1218, 1219 is changed by @AaronVanGeffen at 738e920.
SUPPRESS_WARNING['ko-KR'] = ['STR_1218', 'STR_1219', 'STR_2235', 'STR_2289']
