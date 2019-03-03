#include <bits/stdc++.h>

using namespace std;

/*
The selection sort, finding the minimum
value and then swapping it.
*/

void sel_sort(int *a,int n)
{
    for(int i=0;i<n;i++)
    {
        int mini=a[i],mini_loc=0;
        for(int j=i+1;j<n;j++)
        {
            if(a[j]<mini)
            {
                mini=a[j];
                mini_loc=j;
            }
        }
        if(mini<a[i])
        {
            int dummy=a[i];
            a[i]=a[mini_loc];
            a[mini_loc]=dummy;
        }
    }
}

int main()
{
    ofstream out;
    out.open("worst.txt", ofstream::out);
    ///I am testing for 50 cases and I am writing the
    ///times in a text file called "worst.txt".
    int max_size=160000;
    int cases=50;
    int arr_sizes[51];
    for(int i=1;i<=cases;i++)
    {
        arr_sizes[i-1]=(i*(max_size/cases));
    }
    for(int i=0;i<cases;i++)
    {
        int curr_size=arr_sizes[i];
        int arr[curr_size];
        out<<curr_size<<endl;
        ///The worst case is if the array is sorted in decreasing
        ///order so that the selection sort has to swap every element.
        for(int i=0;i<curr_size;i++)
        {
            arr[i]=curr_size-i;
        }
        ///I am taking the time before and after the sort.
        clock_t start_t=clock();
        sel_sort(arr,curr_size);
        clock_t end_t=clock();
        out<<(double)(end_t-start_t)/CLOCKS_PER_SEC << endl;
    }
    out.close();

    return 0;
}
