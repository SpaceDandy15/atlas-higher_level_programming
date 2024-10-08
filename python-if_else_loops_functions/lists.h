#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description; singly linked list node structure
 */
typed def struct listint_s
{
	int n;
	stuct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);

#endif /* LISTS_H */
