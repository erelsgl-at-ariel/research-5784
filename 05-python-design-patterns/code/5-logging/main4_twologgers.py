import quadratic, factorial, logging

quadratic.logger.addHandler(logging.StreamHandler())
factorial.logger.addHandler(logging.StreamHandler())

print("\n\n### Running with all loggers at warning level\n")
print(quadratic.quadratic_formula(1, 0, -4))
print(factorial.factorial(5))

print("\n\n### Running with quadratic logger at info level\n")
quadratic.logger.setLevel(logging.INFO)
print(quadratic.quadratic_formula(1, 0, -4))
print(factorial.factorial(5))

print("\n\n### Running with factorial logger at info level\n")
quadratic.logger.setLevel(logging.WARNING)
factorial.logger.setLevel(logging.INFO)
print(quadratic.quadratic_formula(1, 0, -4))
print(factorial.factorial(5))

print("\n\n### Running with both loggers at info level\n")
quadratic.logger.setLevel(logging.INFO)
factorial.logger.setLevel(logging.INFO)
print(quadratic.quadratic_formula(1, 0, -4))
print(factorial.factorial(5))

