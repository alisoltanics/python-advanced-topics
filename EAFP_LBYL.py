# LBYL
if os.path.exists(filename):
    with open(filename) as f:
        pass


# EAFP
try:
    with open(filename) as f:
        pass
except FileNotFoundError as e:
    logger.error(e)


# Prefer EAFP over LBYL
