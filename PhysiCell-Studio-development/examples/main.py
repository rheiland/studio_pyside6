# main.py

import wasmtime

# Load the Wasm module
wasm_module = wasmtime.Module.from_file("simple.wasm")

# Create an instance of the module
instance = wasmtime.Instance(wasm_module)

# Get a reference to the exported function
add_func = instance.exports.add

# Call the function and print the result
result = add_func(2,40)
print("result of add:", result)
