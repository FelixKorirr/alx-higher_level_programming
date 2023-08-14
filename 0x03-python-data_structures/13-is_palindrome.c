#include "lists.h"

int is_palindrome(listint_t **head);
listint_t *_reverse_listint(listint_t **head);

/**
 * _reverse_listint - Reverses a linked list.
 * @head: pointer to the starting node
 * Return: pointer to head
 * korir codes
 */
listint_t *_reverse_listint(listint_t **head)
{
	listint_t *nod = *head, *next, *last = NULL;

	while (nod)
	{
		next = nod->next;
		nod->next = last;
		last = nod;
		nod = next;
	}

	*head = last;
	return (*head);
}

/**
 * is_palindrome - Checks if linked list is a palindrome.
 * @head: pointer to the head of the list.
 * Return: If palindrome - 0,else, 1.
 * korir codes
 */
int is_palindrome(listint_t **head)
{
	listint_t *x, *y, *z;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	x = *head;
	while (x)
	{
		size++;
		x = x->next;
	}

	x = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		x = x->next;

	if ((size % 2) == 0 && x->n != x->next->n)
		return (0);

	x = x->next->next;
	y = _reverse_listint(&x);
	z = y;

	x = *head;
	while (y)
	{
		if (x->n != y->n)
			return (0);
		x = x->next;
		y = y->next;
	}
	_reverse_listint(&z);

	return (1);
}
