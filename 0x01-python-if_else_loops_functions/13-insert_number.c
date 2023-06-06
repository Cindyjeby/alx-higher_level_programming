#include "lists.h"
/**
 * insert_node - function that inserts a number into a sort singly list
 * @head: list head
 * @number: number to store the new node
 * Return: a ponter to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *mzee;
	listint_t *mpya;

	mzee = *head;

	mpya = malloc(sizeof(listint_t));
	if (!mpya)
		return (0);
	mya-> = number;

	if (*head == NULL || (*head)->n > number)
	{

