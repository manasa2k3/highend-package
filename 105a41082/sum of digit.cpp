#include <stdio.h>
int main() {
	int n,re,sum=0;
	printf("Enter the number");
	scanf("%d",&n);
	while(n>0)
	{
		re=n%10;
		sum=sum+re;
		n=n/10;
	}
	printf("sum of digits is %d",sum);
	return 0;
}
