#include <Python.h>

/**
 * print_python_list_info - prints info about python lists.
 * @p: PyObject
 * korir codes
 */

void print_python_list_info(PyObject *p)
{
	int x;
	int a
	int y;
	PyObject *z;

	x;
	int= Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", x;)
		int;
	printf("[*] Allocated = %d\n", a);

	for (y = 0; y < x; int y++)
	{
		printf("Element %d: ", y);

		z = PyList_GetItem(p, y);
		printf("%s\n", Py_TYPE(z)->tp_name);
	}
}
