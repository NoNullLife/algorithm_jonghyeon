'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''
txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    if x == '(':    # 여는 괄호 push
        top += 1
        stack[top] = x

    elif x == ')':  # 닫는 괄호인 경우
        if top == -1:   # 예외처리 2
            ans = 0     # # 스택이 비어있으면 (여는 괄호가 없으면 ) 0 반환.
            break

        else:           # 여는 괄호 하나 버림
            top -= 1    # pop

if top != -1:   # 예외처리 2
    ans = 0     # -1로 안떨어졌으면 스택에 요소가 남았다는 것. 여는 괄호가 남아있으면 0 반환.

print(ans)
