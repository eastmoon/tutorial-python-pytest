# content of myinvoke.py
import os
import sys
import pytest
import re

# Declare function
def parse_keys(keyword, line):
    if re.search(keyword, line):
        if not keyword in CMS_KV_PAIRS:
            CMS_KV_PAIRS[keyword]=[]
        line=line.replace(f"{keyword}:", "")
        line=line.replace("\n", "")
        line=line.strip()
        CMS_KV_PAIRS[keyword].append(line)

def gen_keys(keyword):
    if keyword in CMS_KV_PAIRS:
        for val in CMS_KV_PAIRS[keyword]:
            CMS_KEYS[keyword](val)

def gen_library(bddfile):
    bddfile.write("""# Import bdd library
from pytest_bdd import scenarios, given, when, then, parsers
from libs_arguments import *
\n""")

def gen_main(bddfile):
    bddfile.write(f"""# Execute script
scenarios('{feature_name}.feature')
\n""")

def gen_prescenario(args):
    print(f"Generate PreScenario: {args}")

def gen_aftscenario(args):
    print(f"Generate ArfScenario: {args}")

# Declare variable
CMS_KEYS = {
    "PreScenario": gen_prescenario,
    "AftScenario": gen_aftscenario
}
CMS_KV_PAIRS = {}

# Execute script
if __name__ == "__main__":
    # Find feature with argv
    feature_name = sys.argv[1] if len(sys.argv) > 1 else ""
    feature_dir=os.path.join(os.getcwd(), 'test/bdd')
    # Show information
    print("----------")
    print(f"Feature : {feature_name}.feature")
    print("----------")
    # Check file exist or not
    if os.path.exists(f"{feature_dir}/{feature_name}.feature"):
        # Parser custom keywords
        for line in open(f"{feature_dir}/{feature_name}.feature", 'r'):
            for key in CMS_KEYS:
                parse_keys(key, line)
        print(f"[+] Run BDD case {feature_name}.feature")
        # Generate case runner
        with open(f"{feature_dir}/bdd_case_runner.py", 'w') as bddcase:
            # Generate library information
            gen_library(bddcase)
            # Generate PreScenario
            gen_keys("PreScenario")
            # Generate main scenarios
            gen_main(bddcase)
            # Generate AftScenario
            gen_keys("AftScenario")
        # Execute case runner
        sys.exit(pytest.main([f"{feature_dir}/bdd_case_runner.py"]))
    else:
        print(f"[-] {feature_name}.feature not find")
    #sys.exit(pytest.main(["test/test_case0.py"]))
