
def calc_postf_expr(s):
    lis = s.split()
    st  = []
    op = ''
    while lis:
        st.append( lis.pop(0) )
        if not st[-1].isdigit():
            if len(st) < 3:
                return False
            op = st.pop()
            R = int( st.pop() )
            L = int( st.pop() )
            match op:
                case '+':
                    st.append( L + R )
                case '-':
                    st.append( L - R )
                case '*':
                    st.append( L * R )
                case '/':
                    st.append( L / R )
                case _:
                    return False
    if len(st) != 1:
        return False
    return int( st.pop() )
s = input()
res = calc_postf_expr(s)
print(res)