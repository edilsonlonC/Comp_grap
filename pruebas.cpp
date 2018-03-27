#include <iostream>
#include <vector>
#include <ctime>
using namespace std;
using vec=vector<int>;


void ordenShell(vec &v)
{
  int i, j, inc, temp;

  for(inc = 1 ; inc<v.size();inc=inc*3+1);

      while (inc > 0)
      {
          for (i=inc; i < v.size(); i++)
          {
                j = i;
                temp = v[i];
                while ((j >= inc) && (v[j-inc] > temp))
                {
                    v[j] = v[j - inc];
                    j = j - inc;
                }

                v[j] = temp;
          }

          inc/= 2;
      }

}
void quicksort(vec &v,int izq, int der )
{
int i, j, x , aux;
i = izq;
j = der;
x = v[ (izq + der) /2 ];
    do{
        while( (v[i] < x) && (j <= der) )
        {
            i++;
        }

        while( (x < v[j]) && (j > izq) )
        {
            j--;
        }

        if( i <= j )
        {
            aux = v[i]; v[i] = v[j]; v[j] = aux;
            i++;  j--;
        }

    }while( i <= j );

    if( izq < j )
        quicksort( v, izq, j );
    if( i < der )
        quicksort( v, i, der );
}

void insercionDirecta(vec &v)
{

      int i,j,x;

      for (i = 1; i < v.size(); i++)
        {
             x= v[i];
             j = i - 1;
             while (j >= 0 && v[j] > x)
             {
                  v[j + 1] = v[j];
                  j--;
             }

             v[j + 1] = x;
      }
}

double burbble (vec &v)
{
  int aux;
  double t0=clock();
  for (int i=0;i<v.size();i++)
  {
    for (int j=0;j<v.size();j++)
    {
      if (v[i]<v[j])
      {
      aux=v[i];
      v[i]=v[j];
      v[j]=aux;
      }
    }
  }
 double t1=clock();
 double tf=((t1-t0)/CLOCKS_PER_SEC);
 return tf;
}
void muestra (vec &v)
{
  for (int i=0;i<v.size();i++)
  cout<<v[i]<<endl;
}
void Create (vec &v)
{
  for (int i=0;i<10;i++)
  {
    v.push_back(rand()%100);
  }
}


int main()
{
  vec v;
  Create(v);
  muestra(v);
  cout<<burbble(v);
  //quicksort(v,0,v.size());
  //insercionDirecta(v);
//  ordenShell(v);
  cout<<endl<<endl;
  muestra(v);
  return 1;
}
