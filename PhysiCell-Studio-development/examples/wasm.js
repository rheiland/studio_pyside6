const wasmModule = WebAssembly.instantiateStreaming(fetch('pyside0.wasm'), {});

const createWasm = async () => {
  const wasmInstance = await wasmModule;
  return wasmInstance.exports;
};

export { createWasm };
