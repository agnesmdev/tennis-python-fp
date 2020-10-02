set -e

# --------------------------------------------------------------
# Print a short summary of each test to stdout.
# Can produde a lot of output on parameterized tests.
export PYTEST_ADDOPTS="-v"

# --------------------------------------------------------------
# By default pytest captures stdout/stderr.
# The --capture=tee-sys option ensures sys.stdout and
# sys.stderr are actually written to.

# --source=${CYBER_DOJO_SANDBOX} \
coverage3 run \
  --module pytest \
  --capture=tee-sys \
    *test*.py

# https://coverage.readthedocs.io/en/v4.5.x/index.html

coverage3 report \
  --show-missing \
    > reports/coverage.txt

# http://pycodestyle.pycqa.org/en/latest/intro.html#configuration

pycodestyle \
  ${CYBER_DOJO_SANDBOX} \
    --show-source `# show source code for each error` \
    --show-pep8   `# show relevent text from pep8` \
    --ignore E302,E305,W293 \
    --max-line-length=80 \
      > reports/style.txt
