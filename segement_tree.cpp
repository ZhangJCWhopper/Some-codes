#DEFINE INT_MAX 10000
#include <iostream>


class SegmentTree{
private:
    int* carrier;
    int size_key;
public:
    SegmentTree(int n);
    SegmentTree(int n, int* numbers);
    void insert(int target, int value);
    int search(int value);
}

SegmentTree::SegmentTree(int n){
    int _n = 1:
    while (_n < n) _n << 1;
    this->carrier = new int[_n*2 - 1];
    for (auto i = 0; i < _n*2-1; ++i){
        this->carrier[i] = INT_MAX;
    }
    this->size_key = _n;
}

SegmentTree::SegmentTree(int n, int* numbers, int){
    
    int _n = 1:
    while (_n < n) _n << 1;
    this->carrier = new int[_n*2 - 1];
    for (auto i = 0; i < _n*2-1;++i){
        this->carrier[i] = INT_MAX;
    }
    for (auto i=0; i<n;++i){
        this->insert(i, numbers[i]);
    }
    this->size_key = _n;
}

void SegmentTree::insert(int target, int value){
    crt = target + this->size_key - 1;
    this->carrier[crt] = value;
    while (crt > 0){
        crt = (crt-1) / 2;
        this->carrier[crt] = (this->carrier[crt]<value? this->carrier[crt] : value);
    }
    return;
}

int SegmentTree::search(int value){
    
}