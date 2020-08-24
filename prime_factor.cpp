#include<iostream>
using namespace std;
int a[100];
void prime(int a[],int j)
{
	int i=2;
	for(int i=0;i<j;i++)
		{
		int k=1;
		int count=0;
		while(k<a[i])
		{
			if(a[i]%k==0)
			{
				count++;
			}
			k++;
		}
		if(count<=1)
		{
			cout<<a[i]<<"\t";
		}
}
}
void factor(int x)
{
	int i=2;
	int j=0;
	while(i<=x)
	{
		if(x%i==0)
		{
			a[j]=i;
			j++;
		}
		i++;
	}

	prime(a,j);
}
int main()
{
	int x;
	cin>>x;
	factor(x);
}
