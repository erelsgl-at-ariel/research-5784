import quadratic, logging
from quadratic import quadratic_formula

print("\n\n### Running with two handlers\n")
console = logging.StreamHandler()  # writes to stderr (= cerr)
logfile = logging.FileHandler("my_logger.log", mode="w")  # w = replace; r+ = append
quadratic.logger.handlers = [console, logfile]

logfile.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: Line %(lineno)d: %(message)s'))
console.setFormatter(logging.Formatter('Line %(lineno)d: %(message)s'))
logfile.setLevel(logging.DEBUG)
console.setLevel(logging.WARNING)  # log all messages to file, but only warnings and errors to the console
quadratic.logger.setLevel(logging.DEBUG)

print(quadratic_formula(1, 0, -4))
print(quadratic_formula(1, 0, 4))
