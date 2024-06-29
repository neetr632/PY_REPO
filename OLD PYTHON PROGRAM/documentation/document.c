#include <Python.h>

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Execute Python code
    PyRun_SimpleString("print('Hello from Python!')");

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}
