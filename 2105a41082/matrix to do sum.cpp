#include<stdio.h>
#def ke=0
int fun(int n)
{
	int even[n],odd[n];
	int i,ke=0,ko=0;
	for(i=1;i<n*n;i++)
	{
		if(i%2==0)
		{
			even[ke]=i;
			ke++;
			}elseq{
				odd[ko]=i;
				ko++;
			}
		}
		return 	
}
void main() 
{
	int i,j,ke=0,ko=4;
	int even[],odd[],arr[3][3];
	int n=3;
	even[],odd[]=fun(n);
	for(i=1;i<=3;i++)
	{
		for(j=0;j<=3;j++)
		{
			if(i==2 && j==2)
			{
				arr[i-1][j-1]=5;
			}else if((i+j)%2==0)
			}else{
				arr[i-1][j-1]=even[ke];
				ke++;
			}else{
				arr[i-1][j-1]=odd[ko];
				ko--;
			}
		}
	}
	for(i=1;i<=3;i++)
	{
		for(j=1;j<=3;j++)
		{
			
		}
		}	
