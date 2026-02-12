

def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def helper_function(current):
        if current > x:
            print("Harvest time!")
            return
        else:
            print("Day", current)
            helper_function(current + 1)
    helper_function(1)
