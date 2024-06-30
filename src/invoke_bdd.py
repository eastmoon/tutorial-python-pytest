# content of myinvoke.py
import os
import sys

import pytest

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
        print(f"[+] Run BDD case {feature_name}.feature")
        with open(f"{feature_dir}/bdd_case_runner.py", 'w') as bddcase:
            bddcase.write("""# Import bdd library
from pytest_bdd import scenarios, given, when, then, parsers
from libs_arguments import *
\n""")
            bddcase.write(f"""# Execute script
scenarios('{feature_name}.feature')
\n""")
        sys.exit(pytest.main([f"{feature_dir}/bdd_case_runner.py"]))
    else:
        print(f"[-] {feature_name}.feature not find")
    #sys.exit(pytest.main(["test/test_case0.py"]))
