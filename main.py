from api import utils

def main_wrapper():
    print(f"This is the start of our Python Project. This function's name is {main_wrapper.__name__}")

    # code here
    utils.solid_example_1(example_param_2='r', example_param_2=5)
    print("This is the end of our Python Project.")


if __name__ == "__main__":
    main_wrapper()
