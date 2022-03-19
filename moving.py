"""
assignment: Lab 6
file: moving.py
author: Ryan Nowak

Creates boxes and items based on data in file and uses three greedy
strategies to sort those items into the boxes. Then prints the contents
of each box and what items were left out.
"""

from dataclasses import dataclass


@dataclass
class Item:
    """
    Item represents the item that is being placed in a box.
    name: name of the item
    weight: weight of the item
    """
    name: str
    weight: int


@dataclass
class Box:
    """
    Box represents the container that items will be placed in.
    capacity: how much weight the box can hold
    items: list of items in box
    capacity_leftover: how much more weight the box can handle
    """
    capacity: int
    items: list
    capacity_leftover: int


def make_item(name, weight):
    """
    creates a item dataclass with given name and weight

    :param name: name of item
    :param weight: how much weight can be stored in box
    :return: Box dataclass
    """
    return Item(name, weight)


def make_box(capacity):
    """
    creates a box dataclass with given capacity

    :param capacity: how much weight can be stored in box
    :return: Box dataclass
    """
    return Box(capacity, [], capacity)


def read_file(name):
    """
    Makes Box dataclasses and Item dataclasses based on data from file

    :param name: name of file to open
    :return: list of Box dataclasses and list of Item dataclasses
    """
    with open(name) as fd:
        capacities = fd.readline().strip().split()
        boxes = []
        for capacity in capacities:
            boxes.append(make_box(int(capacity)))
        items = []
        for line in fd:
            line_list = line.strip().split()
            items.append(make_item(line_list[0], int(line_list[1])))
    return boxes, items


def sort_descending(items):
    """
    Sorts the given list of Item dataclasses in order of
    descending weight

    :param items: list of Item dataclasses
    :return: list of sorted Item dataclasses
    """
    items.sort(key=lambda x: x.weight, reverse=True)
    return items


def greedy_strat_1(boxes, items):
    """
    Sorts the list of item dataclasses in descending order and puts them
    into boxes using greedy strategy 1

    :param boxes: list of Box dataclasses
    :param items: list of Item dataclasses
    :return: None
    """
    items = sort_descending(items)
    items_leftover = []
    for item in items:
        idx = 0
        for i in range(1, len(boxes)):
            if boxes[i].capacity_leftover > boxes[idx].capacity_leftover:
                idx = i
        if item.weight <= boxes[idx].capacity_leftover:
            boxes[idx].items.append(item)
            boxes[idx].capacity_leftover -= item.weight
        else:
            items_leftover.append(item)

    print('\nResults from Greedy Strategy 1')
    print_data(boxes, items_leftover)


def greedy_strat_2(boxes, items):
    """
    Sorts the list of item dataclasses in descending order and puts them
    into boxes using greedy strategy 2

    :param boxes: list of Box dataclasses
    :param items: list of Item dataclasses
    :return: None
    """
    items = sort_descending(items)
    items_leftover = []
    for item in items:
        idx = 0
        for i in range(0, len(boxes)):
            if item.weight > boxes[idx].capacity_leftover:
                idx = i
            elif boxes[i].capacity_leftover < boxes[idx].capacity_leftover:
                if item.weight <= boxes[i].capacity_leftover:
                    idx = i
        if item.weight <= boxes[idx].capacity_leftover:
            boxes[idx].items.append(item)
            boxes[idx].capacity_leftover -= item.weight
        else:
            items_leftover.append(item)

    print('\nResults from Greedy Strategy 2')
    print_data(boxes, items_leftover)


def greedy_strat_3(boxes, items):
    """
    Sorts the list of item dataclasses in descending order and puts them
    into boxes using greedy strategy 3

    :param boxes: list of Box dataclasses
    :param items: list of Item dataclasses
    :return: None
    """
    items = sort_descending(items)
    items_leftover = []
    for item in items:
        is_room = False
        for box in boxes:
            if item.weight <= box.capacity_leftover:
                box.items.append(item)
                box.capacity_leftover -= item.weight
                is_room = True
                break
        if not is_room:
            items_leftover.append(item)

    print('\nResults from Greedy Strategy 3')
    print_data(boxes, items_leftover)


def print_data(boxes, items):
    """
    Prints if all items could fit into the boxes, the items and their
    weights in each box, and the items that could not fit

    :param boxes: list of Box dataclasses
    :param items: list of Item dataclasses
    :return: None
    """
    if not len(items) == 0:
        print('Unable to pack all items!')
    else:
        print('All items successfully packed into boxes!')
    for i in range(len(boxes)):
        print('Box',i+1,'of weight capacity',boxes[i].capacity,'contains:')
        for item in boxes[i].items:
            print(' ', item.name, 'of weight', item.weight)
    if not len(items) == 0:
        for item in items:
            print(item.name, 'of weight', item.weight, 'got left behind.')


def main():
    """
    Asks user for file name then calls the three different greedy
    strategies
    """
    file_name = input('Enter file name: ')
    boxes1, items1 = read_file(file_name)
    boxes2, items2 = read_file(file_name)
    boxes3, items3 = read_file(file_name)
    greedy_strat_1(boxes1, items1)
    greedy_strat_2(boxes2, items2)
    greedy_strat_3(boxes3, items3)


if __name__ == '__main__':
    main()
