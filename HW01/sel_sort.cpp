#include <bits/stdc++.h>

using namespace std;

int *sel_sort(int *a,int n)
{
    for(int i=0;i<n;i++)
    {
        int mini=a[i],mini_loc=0;
        ///checking every element after
        ///the current one in order to
        ///find the smallest member
        for(int j=i+1;j<n;j++)
        {
            if(a[j]<mini)
            {
                mini=a[j];
                mini_loc=j;
            }
        }
        ///swapping elements
        if(mini<a[i])
        {
            int dummy=a[i];
            a[i]=a[mini_loc];
            a[mini_loc]=dummy;
        }
    }
    return a;
}

int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int *ptr=a;
    ptr=sel_sort(ptr,n);
    for(int i=0;i<n;i++)
    {
        cout<<*(ptr+i)<<" ";
    }
    return 0;
}
