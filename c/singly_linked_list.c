#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct LinkedList {
    size_t length;
    struct Node *head;
    struct Node *tail;
} LinkedList;

void prepend(LinkedList *list, int data) {
    Node *node = (Node *)malloc(sizeof(Node));

    if (node == NULL) {
        fprintf(stderr, "ERROR: malloc failed in prepend\n");
        exit(1);
    }

    node->data = data;
    node->next = NULL;

    if (list->length == 0) {
        list->head = node;
        list->tail = node;
    } else {
        node->next = list->head;
        list->head = node;
    }

    list->length++;
}

void append(LinkedList *list, int data) {
    Node *node = (Node *)malloc(sizeof(Node));

    if (node == NULL) {
        fprintf(stderr, "ERROR: malloc failed in append\n");
        exit(1);
    }

    node->data = data;
    node->next = NULL;

    if (list->length == 0) {
        list->head = node;
        list->tail = node;
    } else {
        list->tail->next = node;
        list->tail = node;
    }

    list->length++;
}

void insert_at(LinkedList *list, int data, size_t idx) {
    if (idx > list->length) {
        fprintf(stderr, "ERROR: index out of bounds");
        return;
    }

    if (idx == 0) {
        prepend(list, data);
        return;
    }

    if (idx == list->length) {
        append(list, data);
        return;
    }

    list->length++;

    Node *node = (Node *)malloc(sizeof(Node));

    if (node == NULL) {
        fprintf(stderr, "ERROR: malloc failed in insert_at\n");
        exit(1);
    }

    node->data = data;
    node->next = NULL;

    Node *previous_node = NULL;
    Node *current_node = list->head;

    for (size_t i = 0; i < idx && current_node != NULL; ++i) {
        previous_node = current_node;
        current_node = current_node->next;
    }

    previous_node->next = node;
    node->next = current_node;
}

int remove_node(LinkedList *list, int data) {
    if (list == NULL || list->length == 0) {
        return -1;
    }

    if (list->head->data == data) {
        list->length--;

        Node *rm_node = list->head;

        if (list->length == 0) {
            list->head = NULL;
            list->tail = NULL;
        } else {
            list->head = list->head->next;
        }

        int rm_data = rm_node->data;

        free(rm_node);

        return rm_data;
    }

    Node *previous_node = NULL;
    Node *current_node = list->head;

    while (current_node != NULL) {
        if (current_node->data == data) {
            list->length--;

            if (current_node->next == NULL) {
                Node *rm_node = list->tail;

                list->tail = previous_node;

                int rm_data = rm_node->data;

                free(rm_node);

                return rm_data;
            }

            Node *rm_node = current_node;

            previous_node->next = current_node->next;

            int rm_data = rm_node->data;

            free(rm_node);

            return rm_data;
        }

        previous_node = current_node;
        current_node = current_node->next;
    }

    return -1;
}

int remove_node_at(LinkedList *list, size_t idx) {
    if (list == NULL || list->length == 0) {
        return -1;
    }

    if (idx > list->length) {
        fprintf(stderr, "ERROR: index out of bounds");
        return -1;
    }

    list->length--;

    if (idx == 0) {
        Node *rm_node = list->head;

        if (list->length == 0) {
            list->head = NULL;
            list->tail = NULL;
        } else {
            list->head = list->head->next;
        }

        int rm_data = rm_node->data;

        free(rm_node);

        return rm_data;
    }

    Node *previous_node = NULL;
    Node *current_node = list->head;

    for (size_t i = 0; i < idx && current_node != NULL; ++i) {
        previous_node = current_node;
        current_node = current_node->next;
    }

    if (current_node->next == NULL) {
        Node *rm_node = list->tail;

        list->tail = previous_node;

        int rm_data = rm_node->data;

        free(rm_node);

        return rm_data;
    }

    Node *rm_node = current_node;

    previous_node->next = current_node->next;

    int rm_data = rm_node->data;

    free(rm_node);

    return rm_data;
}

int get(LinkedList *list, size_t idx) {
    if (list == NULL || list->length == 0) {
        return -1;
    }

    if (idx > list->length) {
        fprintf(stderr, "ERROR: index out of bounds");
        return -1;
    }

    if (idx == 0) {
        return list->head->data;
    }

    if (idx == list->length) {
        return list->tail->data;
    }

    Node *current_node = list->head;

    for (size_t i = 0; i < idx && current_node != NULL; ++i) {
        current_node = current_node->next;
    }

    return current_node->data;
}

void print_list(LinkedList *list) {
    char *msg = (char *)malloc(sizeof(char) * 1024);

    if (msg == NULL) {
        fprintf(stderr, "ERROR: malloc failed in print\n");
        exit(1);
    }

    char *ptr = msg;

    ptr += sprintf(ptr, "Length: %zu ", list->length);

    Node *current_head = list->head;

    while (current_head != NULL) {
        ptr += sprintf(ptr, "[%d] -> ", current_head->data);
        current_head = current_head->next;
    }

    sprintf(ptr, "END");

    printf("%s\n", msg);

    free(msg);
}

int main(void) {
    LinkedList linked_list = {0, NULL, NULL};

    print_list(&linked_list);

    insert_at(&linked_list, 5, 0);
    append(&linked_list, 7);
    append(&linked_list, 9);

    print_list(&linked_list);

    assert(get(&linked_list, 2) == 9);
    assert(remove_node_at(&linked_list, 1) == 7);
    print_list(&linked_list);
    assert(linked_list.length == 2);

    print_list(&linked_list);

    append(&linked_list, 11);

    assert(remove_node_at(&linked_list, 1) == 9);
    assert(remove_node(&linked_list, 9) == -1);
    assert(remove_node_at(&linked_list, 0) == 5);
    assert(remove_node_at(&linked_list, 0) == 11);
    assert(linked_list.length == 0);

    print_list(&linked_list);

    prepend(&linked_list, 5);
    prepend(&linked_list, 7);
    prepend(&linked_list, 9);

    print_list(&linked_list);

    assert(get(&linked_list, 2) == 5);
    assert(get(&linked_list, 0) == 9);
    assert(remove_node(&linked_list, 9) == 9);
    assert(linked_list.length == 2);
    assert(get(&linked_list, 0) == 7);

    printf("ALL TESTS PASSED\n");

    return 0;
}
