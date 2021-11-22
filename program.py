def get_median(nums):
    nums.sort()
    for index, g in enumerate(nums):
        if index == len(nums) // 2:
            median = g

    return median


def get_variance(nums):
    mean = get_mean(nums)
    variance = sum([((x - mean) ** 2) for x in nums]) / len(nums)
    return variance ** 0.5


def get_mean(nums):
    return sum(nums) / len(nums)


def get_stats(nums):
    max_capture_rate = 255

    mean = get_mean(nums)
    mean_pec = mean / max_capture_rate * 100

    median = get_median(nums)
    median_pec = median / max_capture_rate * 100

    variance = get_variance(nums)
    variance_pec = variance / max_capture_rate * 100

    print(f"Mean: {round_num(mean)} ({round_num(mean_pec)}%)")
    print(f"Median: {round_num(median)} ({round_num(median_pec)}%)")
    print(
        f"Variance: {round_num(variance)} ({round_num(variance_pec)}%)")


def round_num(num):
    if (num.is_integer()):
        return round(num)
    else:
        return round(num, 2)


def str_to_bool(str):
    if str == 'True':
        return True
    elif str == 'False':
        return False
    else:
        return bool(str)


with open('pokemon.csv') as f:
    lines = f.readlines()
    legendaries = []
    non_legendaries = []

    # skip CSV headers
    for line in lines[1:]:
        name, is_legendary, capture_rate = line.split(',')

        if (str_to_bool(is_legendary)):
            legendaries.append(float(capture_rate))
        else:
            non_legendaries.append(float(capture_rate))

    print("Chances of capturing a NON-legendary Pokemon")
    get_stats(non_legendaries)

    print("\nChances of capturing a legendary Pokemon")
    get_stats(legendaries)
