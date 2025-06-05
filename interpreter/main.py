from interpreter.Interpreter import Interpreter
from interpreter.InputProcessor import InputProcessor

interpreter = Interpreter(candidate_folder="data")

#  Load JD
processor = InputProcessor("./tests/qanhtest.txt")
jd_command = processor.getParsedInput()
interpreter.run_command(jd_command)

# Filter top
print(interpreter.show_top(1))

# Run query
# processor = InputProcessor("./tests/ShowConditional.txt")
# query_command = processor.getParsedInput()
# interpreter.run_command(query_command)