from matplotlib import pyplot as plt
from scipy.stats import pearsonr
def num_list():
    numbers = []
    while True:
        num = int(input('Enter number: '))
        if num == -1:
            break
        numbers.append(num)
    return numbers

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

def positive_numbers(numbers):
    return len([x for x in numbers if x>0])

def sort_list(numbers):
    return sorted(numbers)
def pearson_correlation_coefficient(numbers):
    x = range(1,len(numbers)+1)
    corr_coef, p_value = pearsonr(x, numbers)
    return corr_coef

def graph(numbers):
    x = range(1,len(numbers)+1)
    plt.scatter(x,numbers, label= "stars", color = "green",
            marker = "*", s=30)
    plt.xlabel('x - numbers order')
    plt.ylabel('y - numbers')
    plt.title('numbers graph')
    plt.legend()
    plt.show()

def print_nums():
    nums = num_list()
    print(f"average list is {average(nums)}")
    print(f"positive numbers in list is {positive_numbers(nums)}")
    print(f"sorted list {sort_list(nums)}")
    print(f"pearson correlation coefficient is {pearson_correlation_coefficient(nums)}")
    graph(nums)