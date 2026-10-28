"""Convert a structured record (list of field/value pairs) to a dictionary."""

def structure_to_dictionary(fields: list[str], values: list[object]) -> dict[str, object]:
    if len(fields) != len(values):
        raise ValueError("The number of fields must match the number of values.")
    if len(set(fields)) != len(fields):
        raise ValueError("Field names must be unique.")
    return dict(zip(fields, values))


if __name__ == "__main__":
    student_fields = ["name", "course", "semester"]
    student_values = ["Divya", "Computer Science", 3]
    print(structure_to_dictionary(student_fields, student_values))
