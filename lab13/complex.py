def sum_comlex(com1, com2):
    sum_img = com1.imaginary + com2.imaginary
    if sum_img >= 0:
        return str(com1.real + com2.real) + '+' + str(sum_img) + 'i'
    else:
        return str(com1.real + com2.real) + str(sum_img) + 'i'
    

def minus_comlex(com1, com2):
    sum_img = com1.imaginary - com2.imaginary
    if sum_img >= 0:
        return str(com1.real - com2.real) + '+' + str(sum_img) + 'i'
    else:
        return str(com1.real - com2.real) + str(sum_img) + 'i'


class Complex():
    
    def __init__(self,a,b):
        self.real=int(a)
        self.imaginary=int(b)
        
    def set_real(self,dd):
        self.real=int(dd)
        
    def set_imaginary(self,mm):
        self.imaginary=int(mm)
        
    def show(self):
        if self.imaginary >= 0:
            print(str(self.real) + '+' + str(self.imaginary) + 'i')
        else:
            print(str(self.real) + str(self.imaginary) + 'i')
            
        
    def __del__(self):
        print('object has been destroyed')
        

