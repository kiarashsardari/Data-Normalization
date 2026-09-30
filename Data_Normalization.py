import math

#normed_x = (x - loc)/scale


def scale(nums_list):
    if nums_list:
        l = loc(nums_list)
        return math.sqrt(sum((x - l)**2 for x in nums_list)/len(nums_list))
    else:
        return None


def loc(nums_list):
    if nums_list:
        return sum(nums_list)/len(nums_list)
    else:
        return None


def norm(x_lst):
    if x_lst:
        l = loc(x_lst)
        s = scale(x_lst)        
        if s != 0 :
            return list(((x-l)/s) for x in x_lst)
        else:
            return x_lst 
    else: 
        return x_lst


if __name__ == '__main__':
    lst = [-10, 0, 25, 50, 75, 100, 110]
    print(lst)
    print(norm(lst))
