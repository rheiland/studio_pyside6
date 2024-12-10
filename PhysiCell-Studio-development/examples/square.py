# main.py

import wasmtime

# Load the Wasm module
wasm_module = wasmtime.Module.from_file("square.wasm",".")

# Create an instance of the module
instance = wasmtime.Instance(wasm_module)

# Get a reference to the exported function
square_func = instance.exports.square

# Call the function and print the result
result = square_func(5)
print("Square of 5:", result)
