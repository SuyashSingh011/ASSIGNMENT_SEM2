#include <bits/stdc++.h>
using namespace std;

class DynamicArray {
private:
    vector<int> arr;

public:
    DynamicArray() {}

    void insert(int index, int value) {
        if (index < 0 || index > arr.size()) {
            cout << "Invalid index" << endl;
            return;
        }
        arr.insert(arr.begin() + index, value);
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= arr.size()) {
            cout << "Invalid index" << endl;
            return;
        }
        arr.erase(arr.begin() + index);
    }

    int getSize() {
        return arr.size();
    }

    // Return true if the dynamic array is empty, false otherwise
    bool isEmpty() {
        return arr.empty();
    }

    // Rotate the dynamic array by k positions to the right
    void rotateRight(int k) {
        if (arr.empty() || k <= 0) {
            return;
        }
        k = k % arr.size();
        if (k == 0) {
            return;
        }
        rotate(arr.begin(), arr.end() - k, arr.end());
    }

    // Reverse the dynamic array
    void reverse() {
        std::reverse(arr.begin(), arr.end());
    }

    // Append an element to the end of the dynamic array
    void append(int value) {
        arr.push_back(value);
    }

    // Prepend an element to the beginning of the dynamic array
    void prepend(int value) {
        arr.insert(arr.begin(), value);
    }

    // Merge two dynamic arrays into a single dynamic array
    DynamicArray* merge(DynamicArray* other) {
        DynamicArray* merged = new DynamicArray();
        merged->arr.reserve(arr.size() + other->arr.size());
        merged->arr.insert(merged->arr.end(), arr.begin(), arr.end());
        merged->arr.insert(merged->arr.end(), other->arr.begin(), other->arr.end());
        return merged;
    }

    // Interleave two dynamic arrays into a single dynamic array
    DynamicArray* interleave(DynamicArray* other) {
        DynamicArray* interleaved = new DynamicArray();
        int i = 0, j = 0;
        int size1 = arr.size(), size2 = other->arr.size();

        while (i < size1 && j < size2) {
            interleaved->arr.push_back(arr[i++]);
            interleaved->arr.push_back(other->arr[j++]);
        }

        while (i < size1) {
            interleaved->arr.push_back(arr[i++]);
        }

        while (j < size2) {
            interleaved->arr.push_back(other->arr[j++]);
        }

        return interleaved;
    }

    // Return the middle element of the dynamic array
    int getMiddleElement() {
        if (arr.empty()) {
            cout << "Dynamic array is empty" << endl;
            return -1;
        }
        return arr[arr.size() / 2];
    }

    // Return the index of the first occurrence of the specified element
    int indexOf(int value) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == value) {
                return i;
            }
        }
        return -1;
    }

    // Split the dynamic array into two dynamic arrays at the specified index
    DynamicArray* splitAtIndex(int index) {
        if (index < 0 || index > arr.size()) {
            cout << "Invalid index" << endl;
            return nullptr;
        }

        DynamicArray* secondArray = new DynamicArray();
        secondArray->arr.assign(arr.begin() + index, arr.end());
        arr.erase(arr.begin() + index, arr.end());

        return secondArray;
    }

    // Resizing the array with a custom factor
    void resize(int factor) {
        if (factor <= 0) {
            cout << "Invalid factor" << endl;
            return;
        }
        arr.resize(arr.size() * factor);
    }

    // Print the dynamic array
    void print() {
        for (int num : arr) {
            cout << num << " ";
        }
        cout << endl;
    }
};

int main() {
    DynamicArray arr;
    arr.append(1);
    arr.append(2);
    arr.append(3);
    arr.append(4);
    arr.print(); 

    arr.insert(2, 5);
    arr.print(); 

    arr.deleteAtIndex(2);
    arr.print();

    cout << "Size: " << arr.getSize() << endl; 
    cout << "Is empty? " << (arr.isEmpty() ? "Yes" : "No") << endl; 

    arr.rotateRight(2);
    arr.print(); 

    arr.reverse();
    arr.print(); 

    arr.prepend(0);
    arr.print(); 

    DynamicArray arr2;
    arr2.append(5);
    arr2.append(6);
    arr2.append(7);

    DynamicArray* merged = arr.merge(&arr2);
    merged->print(); 

    DynamicArray* interleaved = arr.interleave(&arr2);
    interleaved->print(); 

    cout << "Middle element: " << arr.getMiddleElement() << endl; 

    cout << "Index of 3: " << arr.indexOf(3) << endl;

    DynamicArray* secondArray = arr.splitAtIndex(2);
    arr.print(); 
    secondArray->print(); 

    arr.resize(3);
    arr.print(); 

    delete merged;
    delete interleaved;
    delete secondArray;

    return 0;
}
