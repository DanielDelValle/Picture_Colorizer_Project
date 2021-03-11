def avg(lista_numerica):
    """    Returns the average in a numerical list    """
    for x in lista_numerica:
        return "The average of the list is:", sum(lista_numerica) / len(lista_numerica)


def avg_inp():
    """    Returns the average of numbers by input, and asks for how many will be entered.    """
    choice = int(input('How many numbers will you want?: '))
    n_list = []

    for n in range(choice):
        numbers = int(input('Add your number: '))
        n_list.append(numbers)


def facto(n):
    """    It calculates the factorial of a number    """

    factorial = 1

    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
    
        return f"Factorial of {n} is : {factorial}"

    facto(5)