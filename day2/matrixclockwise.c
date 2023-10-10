#include <stdio.h>

void main()

{
int n,i,j,temp; n=2;
scanf("%d",&n);
int a[20][20];
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
scanf("%d",&a[i][j]);
}
}

for(i=0;i<n;i++)
{
for(j=n-1;j>=0;j--)
{
printf("%d ",a[j][i]);
}
printf("\n");
}
/*for(i=0;i<n;i++)
{
	for(j=0;j<n;j++)
	{
		printf("%d ",a[i][j]);
	}
}
*/
}

