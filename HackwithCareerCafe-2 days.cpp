#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void nodays(int month,int days)
{
    if(month>12 || month<1)
    {
          cout<<"Not Valid";
    }
    if(month==1)//jan
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            cout<<days;
        }
        
    }
else if(month==2)//feb
    {
        if(days>28)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31;
            cout<<days;
        }
}
    else if(month==3)//mar
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28;
            cout<<days;
        }
}
        else if(month==4)//apr
    {
        if(days>30)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31;
            cout<<days;
        }
}
        else if(month==5)//may
    {
        if(days>30)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30;
            cout<<days;
        }
}
     else if(month==6)//jun
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31;
            cout<<days;
        }
}
 else if(month==7)//july
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30;
            cout<<days;
        }
}
 else if(month==8)//aug
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30+31;
            cout<<days;
        }
}
    
     else if(month==9)//sep
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30+31+31;
            cout<<days;
        }
}
     else if(month==10)//oct
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30+31+31+30;
            cout<<days;
        }
}
    else if(month==10)//oct
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30+31+31+30;
            cout<<days;
        }
}
    else if(month==11)//nov
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30+31+31+30+31;
            cout<<days;
        }
        
}
else if(month==12)//nov
    {
        if(days>31)
        {
            cout<<"Not Valid";
        }
        else{
            days=days+31+28+31+30+31+30+31+31+30+31+30;
            cout<<days;
        }
        
}
 
    
}
int main() {
   
    int month,days;/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    cin>>month;
    cin>>days;
    nodays(month, days);
        return 0;
}
