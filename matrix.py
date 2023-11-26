                ####### 3rd Order #######
def third_order():
    print(" Put elements: ")
    try:
        a = int(input("  ", ))
        b = int(input("  ", ))
        c = int(input("  ", ))
        print('----')
        d = int(input("  ", ))
        e = int(input("  ", ))
        f = int(input("  ", ))
        print('----')
        g = int(input("  ", ))
        h = int(input("  ", ))
        i = int(input("  ", ))

        A = [[a, b, c],
             [d, e, f],
             [g, h, i]]
        a= A[0][0]
        b= A[0][1]
        c= A[0][2]

        d = A[1][0]
        e = A[1][1]
        f = A[1][2]

        g = A[2][0]
        h = A[2][1]
        i = A[2][2]

        A11= e*i - f*h
        A12= -(d*i - f*g)
        A13= d*h - e*g
        A21= -(b*i - c*h)
        A22= a*i - c*g
        A23= -(a*h - b*g)
        A31= b*f - c*e
        A32= -(a*f - c*d)
        A33= a*e - b*d
    except Exception:
        print("Put valid number! Restart the program")
        
                ####### Determinant display #######
    try:
        print()
        print("  Determinant of 3rd order: ")
        for matrix in A:
            for elements in matrix:
                 print(elements, end=" ")
            print()
        method = input("""  By which method you want to solve the determinant?
                Triange(t), Laplass(l), Sarrius(s): """).lower()
    except Exception:
        print()
        
                ####### Functions (methods and steps) #######
    det=0
    def tr_m(det: int) -> int:
        det = (a*e*i + b*f*g + c*d*h) -\
              (c*e*g + a*f*h + b*d*i)
        return det
    def tr_steps():
        print()
        print("Steps:")
        print(f""" Miltiply elements by diagonals adding other elements miltiplied by triangle:
        1) {a}*{e}*{i} + {c}*{d}*{h} + {g}*{b}*{f}
        2) {g}*{e}*{c} + {a}*{h}*{f} + {d}*{i}*{b}

        Substract them:
        ({a}*{e}*{i} + {c}*{d}*{h} + {g}*{b}*{f}) -\
 ({g}*{e}*{c} + {a}*{h}*{f} + {d}*{i}*{b}) = {tr_m(det)}""")
    
    def laplass(det: int) -> int:
        if A[0][0]==0:
            det = A12*b + A13*c
        elif A[0][1] == 0:
            det = A11*a + A13*c
        elif A[0][2] == 0:
            det = A11*a + A12*b
        
        elif A[1][0] == 0:
            det = A22*e + A23*f
        elif A[1][1] == 0:
            det = A21*d + A23*f
        elif A[1][2] == 0:
            det = A21*d + A22*e

        elif A[2][0] == 0:
            det = A32*h + A33*i
        elif A[2][1] == 0:
            det = A31*g + A33*i
        elif A[2][2] == 0:
            det = A31*g + A32*h
        elif a !=0 and b !=0 and c !=0 and d and e !=0\
             and f !=0 and g !=0 and h !=0 and i != 0 :
            det = A11*a + A12*b + A13*c
        else:
            pass
        return det

    def sarrius(det: int) -> int:
        det = (a*e*i + b*f*g + c*d*h) -\
              (c*e*g + a*f*h + b*d*i)
        return det
    def sarrius_steps():
        print(""" Steps:
        Add first two columns next to the last:""")
        A= [[a, b, c, a, b],
            [d, e, f, d, e],
            [g, h, i, g, h]]
        for matrix in A:
            for elements in matrix:
                print(elements, end=" ")
            print()
        print(f"""   Miltiply elements like diagonals.
    Summarize each.
    1) {a}*{e}*{i} + {b}*{f}*{g} + {c}*{d}*{h}
    2) {c}*{e}*{g} + {a}*{f}*{h} + {b}*{d}*{i}
    Then, substract the sums:
        ({a}*{e}*{i} + {b}*{f}*{g} + {c}*{d}*{h}) -\
 ({c}*{e}*{g} + {a}*{f}*{h} + {b}*{d}*{i}) = {sarrius(det)}""")
        
                ####### Output #######
    try:
        if method == "t":
            print()
            print(" Determinant by triangle method: ", tr_m(det))
            print()
            ask = input("Do you want to see steps? (y/n):  ").lower()
            if ask == "y":
                tr_steps()
            else:
                pass
        elif method == "l":
            print("Determinant by Laplass method:", laplass(det))
        
        elif method == "s":
            print()
            print("Determinant by Sarrius method: ", sarrius(det))
            print()
            ask = input("Do you want to see steps? (y/n):  ").lower()
            if ask == "y":
                sarrius_steps()
            else:
                pass
        else:
               pass
    except Exception:
        print("Put 't', 'l' or 's'. Restart the program!")
        

                ####### 4th Order #######

def fourth_order():
    print(" Put elements: ")
    try:
        a = int(input("  ", ))
        b = int(input("  ", ))
        c = int(input("  ", ))
        d = int(input("  ", ))
        print('------')
        e = int(input("  ", ))
        f = int(input("  ", ))
        g = int(input("  ", ))
        h = int(input("  ", ))
        print('------')
        i = int(input("  ", ))
        j = int(input("  ", ))
        k = int(input("  ", ))
        l = int(input("  ", ))
        print('------')
        m = int(input("  ", ))
        n = int(input("  ", ))
        o = int(input("  ", ))
        p = int(input("  ", ))
        
        A = [[a, b, c, d],
             [e, f, g, h],
             [i, j, k, l],
             [m, n, o, p]]
        a = A[0][0]
        b = A[0][1]
        c = A[0][2]
        d = A[0][3]
        e = A[1][0]
        f = A[1][1]
        g = A[1][2]
        h = A[1][3]
        i = A[2][0]
        j = A[2][1]
        k = A[2][2]
        l = A[2][3]
        m = A[3][0]
        n = A[3][1]
        o = A[3][2]
        p = A[3][3]
        
        A11= (f*k*p + h*j*o + n*g*l) - (n*k*h + f*o*l + p*g*j)
        A12= -((e*k*p + h*i*o + m*g*l) - (m*k*h + e*o*l + p*i*g))
        A13= (e*j*p + h*i*n + m*f*l) - (m*j*h + e*n*l + p*i*f)
        A14= -((e*j*o + g*i*n + m*f*k) - (m*j*g + e*k*n + o*f*i))
        A21= -((b*k*p + d*j*o + n*c*l) - (n*k*d + b*o*l + p*c*j))
        A22= (a*k*p + m*c*l + d*i*o) - (m*k*d + p*i*c + a*o*l)
        A23= -((a*j*p + d*i*n + m*b*l) - (m*j*d + a*l*n + p*i*b))
        A24= (a*j*o + c*i*n + m*b*k) - (m*j*c + a*k*n + o*b*i)
        A31= (b*g*p + d*f*o + n*c*h) - (n*g*d + b*o*h + p*c*f)
        A32= (a*g*p + m*c*h + d*e*o) - (m*g*d + p*e*c + a*o*h)
        A33= -((a*f*p + d*e*n + m*b*h) - (m*f*d + a*h*n + p*e*b))
        A34= -((a*f*o + c*e*n + m*b*g) - (m*f*c + a*g*n + o*b*e))
        A41= -((b*g*l + d*f*k + j*c*h) - (j*g*d + b*k*h + l*c*f))
        A42= (a*g*l + i*c*h + d*e*k) - (i*g*d + l*e*c + a*k*h)
        A43= -((a*f*l + d*e*j + i*b*h) - (i*f*d + a*h*j + l*e*b))
        A44= (a*f*k + c*e*j + i*b*g) - (i*f*c + a*g*j + k*b*e)
    except Exception:
         print("Put valid number!")
         
                ####### Determinant display #######
    try:
        print()
        print("  Determinant of 4th order: ")
        for matrix in A:
            for elements in matrix:
                 print(elements, end=" ")
            print()
        method = input("""  Press <Enter> to solve determinant """)
    except Exception:
        print()
    
                ####### Functions (methods and steps) #######
    det = 0
    def decomposition(det: int) -> int:
        det = e*A21 + f*A22 + g*A23 + h*A24
        return det
    def decopm_steps():
        print(f"""    At first, let's choose a row. For example 2nd row!
        Now, multiply each element of 4th row to its algebraic complement:
        
        1) {e} * {A21} = {e*A21}
        2) {f} * {A22} = {f*A22}
        3) {g} * {A23} = {g*A23}
        4) {h} * {A24} = {h*A24}3

        Then, summarize them:
        5) {e*A21} + {f*A22} + {g*A23} + {h*A24} = {decomposition(det)}""")

                ####### Output #######
    try:
        if method == "":
            print("    Determinant:", decomposition(det))
            print()
            ask = input("Press 'y' to see steps or just skip:  ").lower()
            if ask == "y":
                print()
                decopm_steps()
            else:
                pass
        else:
            pass
    except Exception:
        print("Press just <Enter> please")
        
                ####### Order #######
try:
    det_order = int(input(" Put determinant order (put only 3 or 4 please): "))
    if det_order == 3:
        third_order()
    elif det_order == 4:
        fourth_order()
    else:
        print("Able to solve only 3rd and 4th determinant order!")
except Exception:
    print("Put only numbers!")
