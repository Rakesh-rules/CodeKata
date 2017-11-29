#include<iostream.h>
#include<conio.h>
void main()
{
char i,j;
cin>>i;
j=tolower(i);
if(j == 'a' || j == 'e' || j=='i' || j=='o' || j =='u')
{
cout<<"Vowel";
}
else
{
cout<<"consonant";
}
}
