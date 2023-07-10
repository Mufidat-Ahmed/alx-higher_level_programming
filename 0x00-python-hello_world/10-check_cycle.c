#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: list to be checked
 * Return: 0 if no cycle found or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *front = list;
	listint_t *back = list;

	if (!list)
		return (0);
	while (front && back && back->next)
	{
		front = front->next;
		back = back->next->next;
		if (front == back)
			return (1);
	}
	return (0);
}
