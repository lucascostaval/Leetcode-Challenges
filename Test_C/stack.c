#include <stdlib.h>
#include <stdio.h>

struct Node {
    int val;
    struct Node* next;
};

struct Stack {
    struct Node* head;
    int length;
};

struct Stack create_stack(void) {
    struct Stack stack;
    stack.length = 0;
    return stack;
}

void stack_add(struct Stack *stack, int x) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->val = x;
    new_node->next = stack->head;
    stack->head = new_node;
    stack->length += 1;
}

int stack_pop(struct Stack* stack) {
    if (stack->length == 0) exit(-1);
    int remove = stack->head->val;
    stack->head = stack->head->next;
    stack->length -= 1;
    return remove;
}

int main(void) {
    struct Stack stack = create_stack();
    stack_add(&stack, 5);
    stack_add(&stack, 6);
    printf("%d", stack_pop(&stack));
    return 0;
}