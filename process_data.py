def process_data(data):
    """Process a list of numbers and return a summary.

    Args:
        data (list[int | float]): Input values.

    Returns:
        dict: A summary containing the count, total, average, minimum,
            maximum, and sorted values.
    """
    if not data:
        return {
            "count": 0,
            "total": 0,
            "average": 0,
            "minimum": None,
            "maximum": None,
            "sorted": [],
        }

    sorted_data = sorted(data)
    total = sum(data)
    count = len(data)

    return {
        "count": count,
        "total": total,
        "average": total / count,
        "minimum": sorted_data[0],
        "maximum": sorted_data[-1],
        "sorted": sorted_data,
    }


if __name__ == "__main__":
    sample = [3, 1, 4, 1, 5, 9, 2]
    result = process_data(sample)
    print(result)
