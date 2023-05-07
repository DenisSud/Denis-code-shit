#include <iostream>
#include <string>
#include <cctype>
#include <stack>

int main() {
    std::string s;
    std::getline(std::cin, s);
    std::stack<int> stack;
    for (char c : s)
        if (isdigit(c))
            stack.push(c - '0');
        else if (c != ' ') {
            const int a = stack.top();
            stack.pop();
            const int b = stack.top();
            stack.pop();
            if (c == '+')
                stack.push(a + b);
            else if (c == '-')
                stack.push(b - a);
            else
                stack.push(a * b);
        }
    return 0;
}