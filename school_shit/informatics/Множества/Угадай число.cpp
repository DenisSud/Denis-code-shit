#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> InputVector(string& line) {
vector<int> result;
string temp;
for (char x : line) {
if (x == ' ') {
result.push_back(stoi(temp));
temp.clear();
} else {
temp += x;
}
}
if (!temp.empty()) {
result.push_back(stoi(temp));
}
return result;
}

int main()
{
set<int> possible_nums;
int max_num;
cin >> max_num;
for (int i = 1; i <= max_num; ++i) {
possible_nums.insert(i);
}

string new_line;
getline(cin, new_line);
std::vector<int> numbers;
while (true) {
getline(cin, new_line);
if (new_line.front() == 'N' || new_line.front() == 'Y' || new_line.front() == 'H') {
if (new_line == "NO") {
for (int i : numbers) {
possible_nums.erase(i);
}
}
else if (new_line == "HELP") {
break;
}
else {
std::sort(numbers.begin(), numbers.end());
for (int i = 1; i < numbers.front(); ++i) {
possible_nums.erase(i);
}
auto it1 = numbers.begin();
auto it2 = numbers.begin() + 1;
for (; it2 != numbers.end(); ++it1, ++it2) {
for (int i = 1 + *it1; i < *it2; ++i) {
possible_nums.erase(i);
}
}
for (int i = 1 + numbers.back(); i <= max_num; ++i) {
possible_nums.erase(i);
}
}
}
else {
numbers = InputVector(new_line);
}
}

for (int i : possible_nums) {
cout << i << ' ';
}
cout << endl;
return 0;
}
