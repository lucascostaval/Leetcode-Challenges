#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* result = malloc(sizeof(struct ListNode));
    while (list1 != 0) {
        list1 = list1->next;
    }
    return result;
}

int main() {
    int a = 0x3;
    float x = 34e-10;
    return 0;
}