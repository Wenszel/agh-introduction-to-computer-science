from t_06 import Node
from t_04 import reverse


def add_two_numbers(number1: Node, number2: Node) -> Node:
    output_list = None
    number1 = reverse(number1)
    number2 = reverse(number2)
    surplus = 0

    while number1 is not None and number2 is not None:
        addition_result, surplus = add_with_surplus(number1, number2, surplus)
        output_list = insert_at_front(addition_result, output_list)
        number1 = number1.next
        number2 = number2.next

    output_list = rewrite_rest(number1, number2, output_list, surplus)

    if surplus == 1:
        output_list = insert_at_front(1, output_list)

    return output_list


def add_with_surplus(number1, number2, surplus):
    addition_result = number1.val + number2.val + surplus
    if addition_result >= 10:
        addition_result = addition_result % 10
        surplus = 1
    else:
        surplus = 0
    return addition_result, surplus


def rewrite_rest(number1, number2, output_list, surplus):
    number = number1 if number1 is not None else number2
    while number is not None:
        output_list = insert_at_front(number.val + surplus, output_list)
        number = number.next
        surplus = 0
    return output_list


def insert_at_front(value, linked_list):
    node = Node(value)
    node.next = linked_list
    return node


first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
first_list = Node([int(i) for i in first_number])
second_list = Node([int(i) for i in second_number])
print(add_two_numbers(first_list, second_list))
