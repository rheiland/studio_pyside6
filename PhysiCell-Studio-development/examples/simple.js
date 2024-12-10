// Load the WebAssembly module
WebAssembly.instantiateStreaming(fetch('./simple.wasm'))
  .then(results => {
    // Access exported functions from the module
    const add = results.instance.exports.add; 

    // Call the exported function
    const result = add(2, 3);

    // Use the result
    console.log('The result is:', result); // Output: 5
  });
