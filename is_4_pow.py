import math
class Sol:
    def is_4_pow(self,num):
        return 4**(math.log(num,4))==num


if __name__ == '__main__':
    p1=Sol()
    print(p1.is_4_pow(56))
