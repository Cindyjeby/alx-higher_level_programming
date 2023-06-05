#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
/**
 * struct singly_l - singly linked list
 * @i: is integet
 * @flow: pointer to the next node
 * Description: singly linked list node structure
 */
typedef struct singly_l
{
	int i;
	struct singly_l *flow;
} singly_t;

#endif
