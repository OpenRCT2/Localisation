"""
This script is triggered after a new PR is created on OpenRCT2 Localisation repository.
It checks the difference in translation count between master and PR branch.
The results is put to result.md to be later published as a comment.
"""

import filecmp
import os
import re

MASTER_LANG_DIR = "master/data/language"
PR_LANG_DIR = "pr/data/language"
SPECIAL_KEYS = ['STR_SCNR', 'STR_PARK', 'STR_DTLS', 'STR_NAME']

languages = []


def read_languages_from_master_and_pr():
    """
    Reads languages from master and pr branches
    """
    read_languages_from_filenames(MASTER_LANG_DIR)
    read_languages_from_filenames(PR_LANG_DIR)


def read_languages_from_filenames(dir_to_search):
    """
    Searches given directory for language files and adds them to global languages variable
    """
    pattern = re.compile("([a-z]{2}-[A-Z]{2}).txt")
    for file in os.listdir(dir_to_search):
        find = pattern.findall(file)
        if len(find) == 1 and find[0] not in languages:
            languages.append(find[0])


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

    previous_group_name = ''

    for line in lines:
        if line.startswith('#') or len(line.strip()) == 0:
            continue

        if line.startswith('<') or line.startswith('['):
            previous_group_name = line
            continue

        if line.find(':') != -1:
            split = line.split(':')
            key = split[0].strip()
            if key in SPECIAL_KEYS:
                key = previous_group_name + key
            value = ':'.join(split[1:]).strip()
            translations[key] = value

    return translations


def count_translations(dir_with_translations, print_info):
    """
    Counts missing, same and not needed translations by comparing all files in given location to en-GB
    """
    en_gb = file_to_dict('OpenRCT2/data/language/en-GB.txt')

    missing_counters = dict.fromkeys(languages, 0)
    same_counters = dict.fromkeys(languages, 0)
    not_needed = dict.fromkeys(languages, 0)

    for lang in languages:
        translations = file_to_dict(dir_with_translations + '/' + lang + '.txt')

        for base_string in en_gb:
            if base_string not in translations:
                missing_counters[lang] += 1
                if print_info:
                    print(f'[{lang}] Missing translation: {base_string}')
            elif en_gb[base_string] == translations[base_string]:
                same_counters[lang] += 1
                if print_info:
                    print(f'[{lang}] Same translation: {base_string}')

        for translation in translations:
            if translation not in en_gb:
                not_needed[lang] += 1
                if print_info:
                    print(f'[{lang}] Unnecessary translation: {translation}')

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
    read_languages_from_master_and_pr()
    prepare_translation_report()


def prepare_translation_report():
    master_branch = count_translations(MASTER_LANG_DIR, False)
    pull_request = count_translations(PR_LANG_DIR, True)
    missing = prepare_spoiler('Missing', 'The translation is not added to translation file. '
                                         '(e.g. STR_9999 is in `en-GB` but is not available in given language)')
    not_needed = prepare_spoiler('Not needed', 'The translation file contains entries that are not in `en-GB` '
                                               'and should be removed '
                                               '(e.g. STR_9999 exits in given language but is not in `en-GB`)')
    same = prepare_spoiler('Same', 'The translation and source string is exactly the same.  '
                                   '(e.g. STR_9999 is `Umbrella` in both `en-GB` and given language). '
                                   'This may be desired in some cases (e.g. `April` is the same in English and German)')
    table_header = "| |" + missing + " | " + not_needed + " |" + same + "|\n"
    table_header += "|---|---|---|---|\n"
    languages_changed = []
    for lang in languages:
        filename = lang + '.txt'
        file_master = MASTER_LANG_DIR + '/' + filename
        file_pr = MASTER_LANG_DIR + '/' + filename
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
    text_file = open("result.md", "w")
    text_file.write(result)
    text_file.close()


if __name__ == "__main__":
    run()
