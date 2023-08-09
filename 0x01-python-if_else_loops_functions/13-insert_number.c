#include "lists.h"

/**
 * insert_node - Inserts a number to linked list.
 * @head: pointer the head of the linked list.
 * @number: number to insert.
 * Return: If function fails - NULL,
 * else - pointer to new node.
 * korir codes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x = *head, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (x == NULL || x->n >= number)
	{
		new_node->next = x;
		*head = new_node;
		return (new_node);
	}

	while (x && x->next && x->next->n < number)
		x = x->next;

	new_node->next = x->next;
	x->next = new_node;

	return (new_node);
}
