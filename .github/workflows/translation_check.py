languages = ['ar-EG', 'ca-ES', 'cs-CZ', 'da-DK', 'de-DE', 'en-US', 'eo-OO', 'es-ES', 'fi-FI', 'fr-FR', 'hu-HU', 'it-IT',
             'ja-JP', 'ko-KR', 'nb-NO', 'nl-NL', 'pl-PL', 'pt-BR', 'ru-RU', 'sv-SE', 'tr-TR', 'zh-CN', 'zh-TW']


def file_to_dict(filename):
    with open(filename, encoding="utf8") as f:
        content = f.readlines()
    lines = [line.strip() for line in content]
    translations = {}
    for line in lines:
        if not line.startswith('#') and line.find(':') != -1:
            split = line.split(':')
            key = split[0].strip()
            value = ':'.join(split[1:]).strip()
            translations[key] = value

    return translations


def count_translations(dir_with_translations, print_info):
    en_gb = file_to_dict('OpenRCT2/data/language/en-GB.txt')

    missing_counters = dict.fromkeys(languages, 0)
    same_counters = dict.fromkeys(languages, 0)
    not_in_base_counters = dict.fromkeys(languages, 0)

    for lang in languages:
        translations = file_to_dict(dir_with_translations + '/' + lang + '.txt')
        for base_string in en_gb:
            if base_string not in translations:
                missing_counters[lang] += 1
                if print_info:
                    print('[{}] Missing translation: {}'.format(lang, base_string))
            elif en_gb[base_string] == translations[base_string]:
                same_counters[lang] += 1
                if print_info:
                    print('[{}] Same translation: {}'.format(lang, base_string))

        for translation in translations:
            if translation not in en_gb:
                not_in_base_counters[lang] += 1
                if print_info:
                    print('[{}] Unnecessary translation: {}'.format(lang, translation))

    result = {'missing': missing_counters, 'same': same_counters, 'not_needed': not_in_base_counters}
    return result


def format_result(count_on_master, count_on_pr):
    missing = str(count_on_pr)
    diff = count_on_pr - count_on_master
    if diff != 0:
        missing += ' ({0}{1})'.format('+' if diff > 0 else '', diff)
        missing = '**{0}**'.format(missing)
    return missing


def run():
    master_branch = count_translations('master/data/language', False)
    pr = count_translations('pr/data/language', True)
    result = '#### Check results\n\n'
    result += "For details go to `Translation Check` -> `Details`. Expand `Run checks` build stage and use the build-in search to find your language (e.g. `pl-PL`)\n"
    result += "| |Missing| Same as `en-GB` |Not in `en-GB`|\n"
    result += "|---|---|---|---|\n"

    for lang in languages:
        missing = format_result(master_branch['missing'][lang], pr['missing'][lang])
        same = format_result(master_branch['same'][lang], pr['same'][lang])
        not_needed = format_result(master_branch['not_needed'][lang], pr['not_needed'][lang])

        result += '|`{0}`|{1}|{2}|{3}|\n'.format(lang, missing, same, not_needed)

    text_file = open("result.md", "w")
    text_file.write(result)
    text_file.close()


run()
