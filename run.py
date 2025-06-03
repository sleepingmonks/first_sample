import argparse


if __name__ == "__main__":

    obj = argparse.ArgumentParser()

    obj.add_argument("-input1",type=int,required=True)
    obj.add_argument("-input2",type=int,required=True)

    args = obj.parse_args()

    var1 = args.input1
    var2 = args.input2

    print(var1+var2)