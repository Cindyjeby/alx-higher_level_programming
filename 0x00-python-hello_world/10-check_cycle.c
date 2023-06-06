#include "list.h"
/**
 * check_cycle - function that check if there is a cycle
 * @list: to be checked
 * Return: 1 || 0
 */
int check_cycle(listint_t *list)
{
	listint_t *pole = list;
	listint_t *haraka = list;

	if (list == NULL)
		return (0);

	while (pole && haraka && haraka->next)
	{
		pole = pole->next;
		haraka = haraka->next->next;
		if (pole == haraka)
			return (1);
	}
	return (0);
}
