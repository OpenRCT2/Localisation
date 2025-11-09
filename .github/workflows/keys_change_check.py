import importlib.util

print("keys_change_check.py script text output")

"""
Load modules to compare and en-GB.txt file
"""
module_path = 'pr/.github/workflows/translation_check.py'
module_name = 'keys_pr'  
module_spec = importlib.util.spec_from_file_location(module_name, module_path)
keys_pr_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(keys_pr_module)

module_path = 'master/.github/workflows/translation_check.py'
module_name = 'keys_master'  
module_spec = importlib.util.spec_from_file_location(module_name, module_path)
keys_master_module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(keys_master_module)

keys_list_old = keys_master_module.KEYS_TO_IGNORE
keys_list_new = keys_pr_module.KEYS_TO_IGNORE

OPENRCT2_EN_GB_FILE = "OpenRCT2/data/language/en-GB.txt"

result_file = open("result.md", "w")

result = "**Comparing changes**\n\n"
result += "`KEYS_TO_IGNORE` in `translation_check.py` - list items expanded using `develop` version of `en-GB.txt`\n\n"

result += "```diff\n"
"""
use github codeblock diff style
"""

counter_add = 0
counter_rem = 0

for line in open(OPENRCT2_EN_GB_FILE):
    if line[0:8] in keys_list_old and line[0:8] in keys_list_new:
        result += ("  "+line) # =
    if line[0:8] in keys_list_old and line[0:8] not in keys_list_new:
        result += ("- "+line)
        counter_rem += 1
    if line[0:8] not in keys_list_old and line[0:8] in keys_list_new:
        result += ("+ "+line)
        counter_add += 1
    if line[0:8] in keys_list_new:
        keys_list_new.remove(line[0:8])
    if line[0:8] in keys_list_old:
        keys_list_old.remove(line[0:8])

result += "\n"

result += " "+30*"-"+"\n"

result += "+ "+str(counter_add)+" keys\n"
result += "- "+str(counter_rem)+" keys\n"

result += " "+30*"="+"\n"+"\n"

for compared_side_name, compared_side_keys in [('MASTER', keys_list_old), ('PR', keys_list_new)]:
    result += compared_side_name
    result += " KEYS NOT FOUND IN en-GB.txt"
    result += "\n"

    for key in compared_side_keys:
        result += "! "+key
        result += "\n"
        
    result += "\n "+30*"-"+"\n"
    result += "! "+str(len(compared_side_keys))+" keys\n"
    result += " "+30*"="+"\n\n"


result += "```"
result += "\n\n\n"

result_file.write(result)
result_file.close()
