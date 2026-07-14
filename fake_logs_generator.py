import random



def generate_log():

    return {

        "ip":
        f"192.168.1.{random.randint(1,255)}",

        "failed_login":
        random.randint(0,50),

        "requests":
        random.randint(50,700),

        "ports":
        random.randint(0,50)

    }



if __name__=="__main__":

    for i in range(5):

        print(
            generate_log()
        )