import quadratic, logging
from quadratic import quadratic_formula

print("\n\n### Running with default formatter\n")
console = logging.StreamHandler()  # writes to stderr (= cerr)
quadratic.logger.addHandler(console)
quadratic.logger.setLevel(logging.DEBUG)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

print("\n\n### Running with a new formatter\n")
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: Line %(lineno)d: %(message)s')
console.setFormatter(formatter)
print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))

