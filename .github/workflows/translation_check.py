"""
This script is triggered after a new PR is created on OpenRCT2 Localisation repository.
It checks the difference in translation count between master and PR branch.
The results is put to result.md to be later published as a comment.
"""

import argparse
import filecmp
import os
import re

from suppress_warning import SUPPRESS_WARNING

MASTER_LANG_DIR = "master/data/language"
PR_LANG_DIR = "pr/data/language"
OPENRCT2_EN_GB_FILE = "OpenRCT2/data/language/en-GB.txt"

# Some strings have nothing to be translated and should not appear on the report
KEYS_TO_IGNORE = ['STR_0000', 'STR_0001', 'STR_0824', 'STR_0839', 'STR_0840', 'STR_0865', 'STR_0866', 'STR_0867',
                  'STR_0868', 'STR_0869', 'STR_0870', 'STR_0871', 'STR_0872', 'STR_0873', 'STR_0874', 'STR_0875',
                  'STR_0876', 'STR_0956', 'STR_0957', 'STR_0958', 'STR_0959', 'STR_0960', 'STR_0961', 'STR_0962',
                  'STR_0963', 'STR_0964', 'STR_0965', 'STR_0966', 'STR_0967', 'STR_0968', 'STR_0969', 'STR_0970',
                  'STR_0971', 'STR_0984', 'STR_0985', 'STR_0986', 'STR_0989', 'STR_1021', 'STR_1134', 'STR_1135',
                  'STR_1162', 'STR_1165', 'STR_1170', 'STR_1172', 'STR_1191', 'STR_1192', 'STR_1193', 'STR_1218',
                  'STR_1219', 'STR_1331', 'STR_1332', 'STR_1333', 'STR_1334', 'STR_1342', 'STR_1343', 'STR_1345',
                  'STR_1346', 'STR_1384', 'STR_1388', 'STR_1389', 'STR_1390', 'STR_1391', 'STR_1414', 'STR_1419',
                  'STR_1420', 'STR_1429', 'STR_1449', 'STR_1450', 'STR_1451', 'STR_1528', 'STR_1529', 'STR_1530',
                  'STR_1532', 'STR_1541', 'STR_1544', 'STR_1545', 'STR_1546', 'STR_1547', 'STR_1548', 'STR_1549',
                  'STR_1562', 'STR_1563', 'STR_1564', 'STR_1566', 'STR_1575', 'STR_1578', 'STR_1579', 'STR_1580',
                  'STR_1581', 'STR_1582', 'STR_1583', 'STR_1601', 'STR_1602', 'STR_1603', 'STR_1605', 'STR_1606',
                  'STR_1607', 'STR_1608', 'STR_1609', 'STR_1610', 'STR_1611', 'STR_1612', 'STR_1613', 'STR_1614',
                  'STR_1615', 'STR_1633', 'STR_1634', 'STR_1635', 'STR_1637', 'STR_1638', 'STR_1639', 'STR_1640',
                  'STR_1641', 'STR_1642', 'STR_1643', 'STR_1644', 'STR_1645', 'STR_1646', 'STR_1647', 'STR_1675',
                  'STR_1690', 'STR_1731', 'STR_1744', 'STR_1749', 'STR_1771', 'STR_1778', 'STR_1799', 'STR_1812',
                  'STR_1817', 'STR_1845', 'STR_1867', 'STR_1871', 'STR_1912', 'STR_1913', 'STR_1914', 'STR_1915',
                  'STR_1917', 'STR_1926', 'STR_1957', 'STR_1958', 'STR_1970', 'STR_1971', 'STR_1972', 'STR_1974',
                  'STR_1983', 'STR_1986', 'STR_1987', 'STR_2117', 'STR_2118', 'STR_2119', 'STR_2121', 'STR_2215',
                  'STR_2216', 'STR_2217', 'STR_2222', 'STR_2235', 'STR_2289', 'STR_2454', 'STR_2763', 'STR_2781',
                  'STR_2996', 'STR_2997', 'STR_2998', 'STR_2999', 'STR_3000', 'STR_3001', 'STR_3002', 'STR_3003',
                  'STR_3004', 'STR_3005', 'STR_3006', 'STR_3007', 'STR_3008', 'STR_3009', 'STR_3020', 'STR_3096',
                  'STR_3212', 'STR_3246', 'STR_3302', 'STR_3309', 'STR_3310', 'STR_3311', 'STR_5138', 'STR_5139',
                  'STR_5182', 'STR_5298', 'STR_5299', 'STR_5375', 'STR_5376', 'STR_5462', 'STR_5467', 'STR_5485',
                  'STR_5486', 'STR_5633', 'STR_5918', 'STR_5919', 'STR_6012', 'STR_6034', 'STR_6059', 'STR_6062',
                  'STR_6063', 'STR_6164', 'STR_6201', 'STR_6229', 'STR_6230', 'STR_6231', 'STR_6329', 'STR_6360']

languages = []
STR_NUMBER_RE = re.compile(r"STR_\d+")

def get_arg_parser():
    """ Command line arguments """
    parser = argparse.ArgumentParser(description='Check translation integrity',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--reference-lang-file', '-r', default=OPENRCT2_EN_GB_FILE,
                        help='a reference language file, typically en-GB.txt')
    parser.add_argument('--master-dir', '-m', default=MASTER_LANG_DIR,
                        help='the language directory on the master branch')
    parser.add_argument('--branch-dir', '-b', default=PR_LANG_DIR,
                        help='the language directory on the pull request branch')
    return parser


def read_languages_from_master_and_pr(master_dir, branch_dir):
    """
    Reads languages from master and pr branches
    """
    read_languages_from_filenames(master_dir)
    read_languages_from_filenames(branch_dir)


def read_languages_from_filenames(dir_to_search):
    """
    Searches given directory for language files and adds them to global languages variable
    """
    pattern = re.compile("([a-z]{2}-[A-Z]{2}).txt")
    for file in os.listdir(dir_to_search):
        find = pattern.findall(file)
        if len(find) == 1 and find[0] not in languages:
            languages.append(find[0])
        languages.sort()


def file_to_dict(filename):
    """
    Loads given file into a dictionary collection
    """
    if not os.path.exists(filename):
        return {}

    with open(filename, encoding="utf8") as file:
        content = file.readlines()
    lines = [line.strip() for line in content]
    translations = {}

    for line in lines:
        if line.startswith('#') or len(line.strip()) == 0:
            continue

        if line.find(':') != -1:
            split = line.split(':')
            key = split[0].strip()
            if not STR_NUMBER_RE.match(key):
                print(f'[{os.path.basename(filename)}]: {key} does not match STR_XXXX pattern')
            value = ':'.join(split[1:]).strip()
            if key in translations:
                print(f'[{os.path.basename(filename)}]: {key} is repeated')
            else:
                translations[key] = value

    return translations


def count_translations(dir_with_translations, print_info, reference_file):
    """
    Counts missing, same and not needed translations by comparing all files in given location to en-GB
    """
    en_gb = file_to_dict(reference_file)

    missing_counters = dict.fromkeys(languages, 0)
    same_counters = dict.fromkeys(languages, 0)
    not_needed = dict.fromkeys(languages, 0)

    for lang in languages:
        filename = lang + '.txt'
        translations = file_to_dict(os.path.join(dir_with_translations, filename))
        messages = {
            'missing': [],
            'same': [],
            'unexpected': [],
            'unnecessary': []
        }

        for base_string in en_gb:
            if base_string in KEYS_TO_IGNORE and base_string not in SUPPRESS_WARNING[lang]:
                if base_string in translations and en_gb[base_string] != translations[base_string]:
                    messages['unexpected'].append(base_string)
            elif base_string not in translations:
                messages['missing'].append(base_string)
            elif en_gb[base_string] == translations[base_string]:
                messages['same'].append(base_string)

        messages['unnecessary'].extend([key for key in translations if key not in en_gb])

        missing_counters[lang] = len(messages['missing'])
        same_counters[lang] = len(messages['same'])
        not_needed[lang] = len(messages['unnecessary'])

        if print_info:
            print(f'{"=" * 15} Language: {lang} {"=" * 15}')
            print(f'Missing ({missing_counters[lang]}):')
            print(f'\t{', '.join(messages["missing"])}')
            print(f'Unnecessary (not in en-GB) ({not_needed[lang]}):')
            print(f'\t{', '.join(messages["unnecessary"])}')
            print(f'Translation not expected ({len(messages["unexpected"])})\nPlease review and if OK, add to supress_warning.py:')
            print(f'\t{', '.join(messages["unexpected"])}')
            print(f'Same as en-GB ({same_counters[lang]}):')
            print(f'\t{', '.join(messages["same"])}')
            print(f'{"-" * 47}\n')

    result = {'missing': missing_counters, 'same': same_counters, 'not_needed': not_needed}
    return result


def format_result(count_on_master, count_on_pr):
    """
    Formats the result cell by formatting it bold if there is a difference between master and pr
    """
    missing = str(count_on_pr)
    diff = count_on_pr - count_on_master
    if diff != 0:
        missing += ' ({0}{1})'.format('+' if diff > 0 else '', diff)
        missing = f'**{missing}**'
    return missing


def prepare_spoiler(summary, details):
    """
    Prepares a foldable spoiler
    """
    return f'<p><details><summary>{summary}</summary>{details}</details></p>'


def run():
    """runs the script and outputs the result in result.md file"""
    parser = get_arg_parser()
    args = parser.parse_args()
    read_languages_from_master_and_pr(args.master_dir, args.branch_dir)
    prepare_translation_report(args.master_dir, args.branch_dir, args.reference_lang_file)


def prepare_translation_report(master_dir, branch_dir, reference_file):
    """ Generates the translation report """
    master_branch = count_translations(master_dir, False, reference_file)
    pull_request = count_translations(branch_dir, True, reference_file)
    missing = prepare_spoiler('Missing', 'The translation is not added to translation file. '
                                         '(e.g. STR_9999 is in `en-GB` but is not available in given language)')
    not_needed = prepare_spoiler('Not needed', 'The translation file contains entries that are not in `en-GB` '
                                               'and should be removed '
                                               '(e.g. STR_9999 exists in given language but is not in `en-GB`)')
    same = prepare_spoiler('Same', 'The translation and source string is exactly the same.  '
                                   '(e.g. STR_9999 is `Umbrella` in both `en-GB` and given language). '
                                   'This may be desired in some cases (e.g. `April` is the same in English and German)')
    table_header = "| |" + missing + " | " + not_needed + " |" + same + "|\n"
    table_header += "|---|---|---|---|\n"
    languages_changed = []
    for lang in languages:
        filename = lang + '.txt'
        file_master = os.path.join(master_dir, filename)
        file_pr = os.path.join(branch_dir, filename)
        if not os.path.exists(file_master) or not os.path.exists(file_pr):
            languages_changed.append(lang)
            continue
        if not filecmp.cmp(file_master, file_pr):
            languages_changed.append(lang)
    result = '#### Check results\n\n'
    result += "For details go to `Translation Check` -> `Details`. " \
              "Expand `Run checks` build stage and use the build-in search to find your language (e.g. `pl-PL`)\n\n"
    result += table_header
    other_table = "\n\n" + table_header
    for lang in languages:
        missing = format_result(master_branch['missing'][lang], pull_request['missing'][lang])
        not_needed = format_result(master_branch['not_needed'][lang], pull_request['not_needed'][lang])
        same = format_result(master_branch['same'][lang], pull_request['same'][lang])

        row = f'|`{lang}`|{missing}|{not_needed}|{same}|\n'

        if lang in languages_changed:
            result += row
        else:
            other_table += row
    result += prepare_spoiler('Other translations', other_table)
    result += '\n'
    text_file = open("result.md", "w")
    text_file.write(result)
    text_file.close()


if __name__ == "__main__":
    run()
