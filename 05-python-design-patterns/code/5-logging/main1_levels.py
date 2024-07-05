import quadratic, logging
from quadratic import quadratic_formula

print("\n\n### Running with log level INFO\n")
console = logging.StreamHandler()  # writes to stderr (= cerr)
quadratic.logger.addHandler(console)
quadratic.logger.setLevel(logging.INFO)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

print("\n\n### Running with log level DEBUG\n")
quadratic.logger.setLevel(logging.DEBUG)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

print("\n\n### Running with log level WARNING\n")
quadratic.logger.setLevel(logging.WARNING)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

print("\n\n### Running with log level ERROR\n")
quadratic.logger.setLevel(logging.ERROR)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

print("\n\n### Running with log level CRITICAL\n")
quadratic.logger.setLevel(logging.CRITICAL)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

