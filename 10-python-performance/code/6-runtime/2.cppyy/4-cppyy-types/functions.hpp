#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
using namespace std;

int sum(const vector<int> &v)
{
    cout << "sum vector" << endl;
    return accumulate(begin(v), end(v), 0);
}

int sum(const vector<vector<int>> &mat)
{
    cout << "sum matrix" << endl;
    int result = 0;
    for (auto v : mat)
        result += accumulate(begin(v), end(v), 0);
    return result;
}

int sum(const set<int> &v)
{
    cout << "sum set" << endl;
    return accumulate(begin(v), end(v), 0);
}

int sumset(const set<int> &v)
{
    cout << "sumset" << endl;
    return accumulate(begin(v), end(v), 0);
}

int sum(const unordered_set<int> &v)
{
    cout << "sum unordered_set" << endl;
    return accumulate(begin(v), end(v), 0);
}

int summap(const map<int, int> &v)
{
    cout << "summap" << endl;
    int s = 0;
    for (const auto &[key, val] : v)
    {
        s += key + val;
    }
    return s;
}

int sum(const map<int, int> &v)
{
    return summap(v);
}
