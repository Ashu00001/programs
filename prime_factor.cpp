#include<iostream>
using namespace std;
int main()
{
	int a,countfor=0,countwhile=0;
	cin>>a;
	for(int i=2;i<a;i++)
{
		if(a%i==0){
	while(a%i==0)
	{
		cout<<i<<"\n";
		a=a/i;
		countwhile++;
	}
					}
					countfor++;

}
cout<<"\n\n"<<countfor<<endl<<countwhile<<"\n\n"<<endl;
}
