#include <stdio.h>
#include <stdlib.h>


double macierz1[3][3]={1,2,3,4,5,6,7,8,9};
double macierz2[3][3]={13,21,31,41,56,64,72,81,91};
double macierz3[3][3];

void dodawaniemacierzy();
void wyswietlmacierz();
void mnozeniemacierzy();


int main()
{
    printf("Hello world!\n");

    mnozeniemacierzy();
    //dodawaniemacierzy();
    wyswietlmacierz();



    return 0;
}

void wyswietlmacierz()
{
   int j=0;
while(j<3)
{

    for (int i=0;i<3;i++)
{printf("%g",macierz3[i][j]);
printf("%c",' ');
}
printf("%c",'\n');
j++;
};


};

void dodawaniemacierzy()
{   int j=0;
while(j<3)
{

    for (int i=0;i<3;i++)
{macierz3[i][j]=macierz1[i][j]+macierz2[i][j];
}

j++;

};


};



void mnozeniemacierzy()
{
    for(int i=0;i<3;i++)
{
for(int j=0;j<3;j++)
{
macierz3[i][j]=0;
for(int k=0;k<3;k++)
{
macierz3[i][j]+=macierz1[i][k]*macierz2[k][j];
}
}
}
};
