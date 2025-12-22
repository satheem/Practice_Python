def analyze_logs(logs):
    """
    Docstring for analyze_logs

    :param logs: Description
    """

    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for log in logs:
        if ":" not in log:
            continue

        level = log.split(":",1)[0].strip()

        if level in counts:
            counts[level] += 1

    return counts


logs = [
    "INFO: Application started",
    "WARNING: Low disk space",
    "ERROR: Failed to connect to database",
    "INFO: User logged in",
    "ERROR: Timeout occurred",
]

result = analyze_logs(logs)
print(result)
