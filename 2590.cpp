#include <stdio.h>
 
int main() {
  
  int t, n;
  
  scanf("%d", &t);
  
  int i; 
  for(i = 0; i < t; i++) {
    
    scanf("%d", &n);
    
    if((n % 4) == 0) printf("%d\n", 1); 
    else if((n % 4) == 1) printf("%d\n", 7); 
    else if((n % 4) == 2) printf("%d\n", 9); 
    else if((n % 4) == 3) printf("%d\n", 3); 
    
  }
  
  return 0; 
  
}
