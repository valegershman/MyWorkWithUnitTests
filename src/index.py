import random

def findMin(lst):
    min_number = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_number:
            min_number = lst[i]
    return min_number


def findMax(lst):
    max_number = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_number:
            max_number = lst[i]
    return max_number


def sumOfElements(lst):
    sm = 0
    for elem in lst:
        sm += elem        # sm = sm + elem
    return sm


def multOfElements(lst):
    mult = 1
    for elem in lst:
        mult *= elem    # mult = mult * elem
    return mult


def generateTestFiles():
    for i in range(5000, 100000, 5000):
        with open('temp/numbers' + str(i) + '.txt', 'w') as f:
            temp = ' '.join(random.choice('12345679') for _ in range(i))
            f.write(temp)


if __name__ == '__main__':
    with open('../temp/numbers.txt', 'r') as f:
        data = f.read()
        print(data)

    list_of_numbers = data.split()
    list_of_numbers = list(map(int, list_of_numbers))
    print(list_of_numbers)

    # print(findMin(list_of_numbers))
    # print(findMax(list_of_numbers))
    # print(sumOfElements(list_of_numbers))
    # print(multOfElements(list_of_numbers))