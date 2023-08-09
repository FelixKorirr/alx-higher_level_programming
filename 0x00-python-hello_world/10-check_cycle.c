#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list
 * Return: 1 if list has a cycle, else, 0
 * korir codes
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list;
	listint_t *y = list;

	if (!list)
	{
		return (0);
	}
	while (x && y && y->next)
	{
		x = x->next;
		y = y->next->next;

		if (x == y)
		{
			return (1);
		}
	}

	return (0);
}
