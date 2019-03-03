#include <bits/stdc++.h>

using namespace std;

void fmerge(vector <int> &arr,int a,int b,int c)
{
    vector <int> arr1;
    vector <int> arr2;
    for(int i=a; i<=b; i++)
    {
        arr1.push_back(arr[i]);
    }
    for(int i=b+1; i<=c; i++)
    {
        arr2.push_back(arr[i]);
    }
    int x=0,y=0,z=a;
    int size1=arr1.size();
    int size2=arr2.size();
    while(x<size1 && y<size2)
    {
        if(arr1[x]<=arr2[y])
        {
            arr[z]=arr1[x];
            x+=1;
        }
        else
        {
            arr[z]=arr2[y];
            y+=1;
        }
        z+=1;
    }
    while(x<size1)
    {
        arr[z]=arr1[x];
        x+=1;
        z+=1;
    }
    while(y<size2)
    {
        arr[z]=arr2[y];
        y+=1;
        z+=1;
    }
}

void insertionSort(vector <int> &arr,int x,int z)
{
    for(int i=x+1;i<=z;i++)
    {
        int key=arr[i];
        int j=i-1;
        while(j>=x && key<arr[j])
        {
            arr[j+1]=arr[j];
            j-=1;
        }
        arr[j+1]=key;
    }
}

void mergeSort(vector <int> &arr,int a,int b, int k)
{
    if((b-a+1)<=k)
    {
        insertionSort(arr,a,b);
    }
    else
    {
        int mid=(a+b)/2;
        mergeSort(arr,a,mid,k);
        mergeSort(arr,mid+1,b,k);
        fmerge(arr,a,mid,b);
    }
}

int main()
{
    srand(time(NULL));
    ofstream out;
    out.open("random.txt", ofstream::out);
    int curr_size=160000;
    int cases=100;
    for(int i=0; i<cases; i++)
    {
        int k = (i+1)*(curr_size/cases);
        vector <int> arr;
        out<<k<<endl;
        for(int j=0; j<curr_size; j++)
        {
            arr.push_back(rand()%INT_MAX);
        }
        clock_t start_t=clock();
        mergeSort(arr,0,curr_size-1,k);
        clock_t end_t=clock();
        out<<(double)(end_t-start_t)/CLOCKS_PER_SEC << endl;
    }
    out.close();

    out.open("best.txt", ofstream::out);
    for(int i=0; i<cases; i++)
    {
        int k=(i+1)*(curr_size/cases);
        vector <int> arr;
        out<<k<<endl;
        for(int j=0; j<curr_size; j++)
        {
            arr.push_back(j);
        }
        clock_t start_t=clock();
        mergeSort(arr,0,curr_size-1,k);
        clock_t end_t=clock();
        out<<(double)(end_t-start_t)/CLOCKS_PER_SEC << endl;
    }
    out.close();

    out.open("worst.txt", ofstream::out);
    for(int i=0; i<cases; i++)
    {
        int k = (i+1)*(curr_size/cases);
        vector <int> arr;
        out<<k<<endl;
        int l;
        if(curr_size%2==0)
        {
            l=curr_size-1;
        }
        else
        {
            l=curr_size;
        }
        for(int j=curr_size; j>=0; j--)
        {
            if(j<=(curr_size/2))
            {
                arr.push_back(j*2);
            }
            else
            {
                arr.push_back(l);
                l-=2;
            }
        }
        clock_t start_t=clock();
        mergeSort(arr,0,curr_size-1,k);
        clock_t end_t=clock();
        out<<(double)(end_t-start_t)/CLOCKS_PER_SEC << endl;
    }
    out.close();

    return 0;
}
