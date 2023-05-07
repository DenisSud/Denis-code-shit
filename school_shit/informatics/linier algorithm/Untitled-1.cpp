#include <iostream>
#include <vector>
#include <string>
 
using namespace std;
 
class MyStack
{
    vector<int> mStack;
    int *back;
 
public:
    MyStack(void) : back(nullptr) {}
    int size() { return mStack.size(); }
 
    friend istream & operator>>(istream &in, MyStack &st)
    {
        cout << st.cmdProcess(in);
        return in;
    }
 
private:
    string cmdProcess(istream &);
    
    void push(istream &cmdstream)
    {
        int x;
        cmdstream >> x;
        mStack.push_back(x);
        back = &mStack[0];
    }
 
    bool pop(int &top)
    {
        if (!size())
            return false;
        
        top = mStack[size() - 1];
        mStack.erase(mStack.begin());
        back = &mStack[0];
        return true;
    }
};
 
string MyStack::cmdProcess(istream &cmdstream)
{
    string cmd, msg;
    int top;
    char bf[20];
    cmdstream >> cmd;
    if (cmd == "push")
    {
        push(cmdstream);
        msg = "ok";
    }
    else if (cmd == "pop")
        msg = pop(top) ? itoa(top, bf, 10) : "error! (pop: stack is empty)";
    else if (cmd == "size")
        msg = itoa(size(), bf, 10);
    else if (cmd == "back")
        msg = size() ? itoa(*back, bf, 10) : "error! (back: stck is empty)";
    else if (cmd == "clear")
    {
        mStack.clear();
        msg = "ok";
    }
    else if (cmd == "exit")
        msg = "bye";
    else
        msg = "error! unknown comand";
 
    msg.append("\n");
    
    if (cmd != "exit")
        msg += cmdProcess(cmdstream);
 
    return msg;
}
 
int main()
{
    MyStack s;
    cin >> s;
    return 0;
}