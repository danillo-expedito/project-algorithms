def study_schedule(permanence_period, target_time):
    """
    :param permanence_period: list of tuples (start, end)
    :param target_time: int
    :return: int
    """
    counter = 0
    if target_time is None:
        return None
    for student_period in permanence_period:
        if not isinstance(student_period[0], int) or not isinstance(
            student_period[1], int
        ):
            return None
        elif (
            target_time >= student_period[0]
            and target_time <= student_period[1]
        ):
            counter += 1
    return counter
