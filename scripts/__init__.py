# Marks this repo's scripts/ as a regular package so `from scripts.X import ...`
# resolves here (sys.path[0] via conftest) rather than to any unrelated `scripts`
# package that may be installed in the environment's site-packages.
