import wasmtime

# Create a store
store = wasmtime.Store()

# Define a Python function to be imported by the WebAssembly module
def say_hello():
    print("Hello from Python!")

# Compile the WebAssembly module from the text format
module = wasmtime.Module(
    store.engine,
    """
    (module
        (import "python" "hello" (func $hello))
        (func (export "run") (call $hello))
    )
    """
)

# Create a function instance from the Python function
hello = wasmtime.Func(store, wasmtime.FuncType([], []), say_hello)

# Instantiate the module, passing the imported function
instance = wasmtime.Instance(store, module, [hello])

# Get the exported function from the instance
run = instance.exports(store)["run"]

# Call the exported function
run(store)
