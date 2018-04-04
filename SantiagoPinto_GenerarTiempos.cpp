
#include<iostream>
#include <ctime>
using namespace std;

//devuelve el enesimo valor de la serie de fibonacci
int fibonacci(int N) {
    if(N < 2){
        return N;}
    else {
	return fibonacci(N-1) + fibonacci(N-2);}
  	}

//corre la serie de fibonacci
float get_time(int N) {	 
  clock_t t;
  t = clock();

// SOME CODE THAT TAKES TIME
  fibonacci(N);

  t = clock() - t;
  float time = ((float)t)/CLOCKS_PER_SEC;
  return time;}



//corre todo
int main() {
  int N;
   N=35;
  fibonacci(N); 
  get_time(N);
  
  for(int i =0; i <= N; i++)
  {cout << i <<" "<< get_time(i) << " "<< endl;}


  return 0;
}














