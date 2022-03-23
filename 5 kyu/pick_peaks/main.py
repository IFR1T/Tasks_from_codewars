def pick_peaks(arr):
    d = {'pos': [], 'peaks': []}

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1] or arr[i] > arr[i - 1] and arr[i] == arr[i + 1] and is_platoe(
                arr[i + 1:]):
            d['pos'].append(i)
            d['peaks'].append(arr[i])
    return d


def is_platoe(arr):
    print(arr)
    if len(arr) == 1:
        return False
    else:
        if arr[1] < arr[0]:
            return True
        elif arr[1] > arr[0]:
            return False
        else:
            return (is_platoe(arr[1:]))