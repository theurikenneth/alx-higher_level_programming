#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly-linkedlist.
 * @head: pointer to the linked list head
 * @number: number to insert
 *
 * Return: NULL if it fails or pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *node = *head, *new;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);
  new->n = number;

  if (node == NULL || node->n >=number)
    {
      new->next = node;
      *head = new;
      return (new);
    }

}
