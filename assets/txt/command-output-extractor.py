import json

# Load JSON data from the input file
input_file = "Test-OilRig_event-logs.json"
output_file = "Test-OilRig_commands_output.txt"

with open(input_file, 'r') as file:
    data = json.load(file)

# Extract command and output fields for each JSON object
results = []
for obj in data:
    command = obj.get("command", "N/A")
    output = obj.get("output", {})
    stdout = output.get("stdout", "N/A")
    stderr = output.get("stderr", "N/A")
    exit_code = output.get("exit_code", "N/A")

    result = f"command: {command}\nstdout: {stdout}\nstderr: {stderr}\nexit code: {exit_code}\n"
    results.append(result)

# Write the results to the output file
with open(output_file, 'w') as file:
    for result in results:
        file.write(result + "\n")

print(f"Extracted information saved to {output_file}")
