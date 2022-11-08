# Notice that parameter "course_prefix" is assigned to argument Comp.
# However, this can be overwritten by an argument.
# Keyword arguments need to be defined AFTER positional arguments.

def register_class(course_number, course_prefix='Comp'):
    print(f"Let's register for {course_prefix}{course_number}")


def main():
    register_class(152)
    register_class(course_prefix="TEST", course_number=999)
    # Notice the "Math" argument overrides the default "Comp" argument.
    register_class(161, "Math")


main()
