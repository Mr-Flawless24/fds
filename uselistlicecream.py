#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

list<int> intersection(list<int>& setA, list<int>& setB) {
    list<int> result;
    set_intersection(setA.begin(), setA.end(), setB.begin(), setB.end(), back_inserter(result));
    return result;
}

list<int> symmetricDifference(list<int>& setA, list<int>& setB) {
    list<int> result;
    set_symmetric_difference(setA.begin(), setA.end(), setB.begin(), setB.end(), back_inserter(result));
    return result;
}

void inputSet(list<int>& set) {
    int n, element;
    cout << "Enter the number of elements in the set: ";
    cin >> n;
    cout << "Enter the elements of the set:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> element;
        set.push_back(element);
    }
}

int main() {
    list<int> vanilla, butterscotch;

    // Input sets from user
    cout << "Vanilla set:" << endl;
    inputSet(vanilla);
    cout << "Butterscotch set:" << endl;
    inputSet(butterscotch);

    // Perform intersection and symmetric difference
    list<int> both = intersection(vanilla, butterscotch);
    list<int> eitherNotBoth = symmetricDifference(vanilla, butterscotch);

    int totalStudents;
    cout << "Enter total number of students: ";
    cin >> totalStudents;

    int neither = totalStudents - vanilla.size() - butterscotch.size() + both.size();

    // Output results
    cout << "Both: ";
    for (int x : both) cout << x << " ";
    cout << endl;

    cout << "Either but not both: ";
    for (int x : eitherNotBoth) cout << x << " ";
    cout << endl;

    cout << "Neither: " << neither << endl;

    return 0;
}
