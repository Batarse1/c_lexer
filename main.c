int fibbonacci(int n) {
   if(n == 0 || n == 1){
      return 0;
   } else {
      int args1 = n - 1;
      int args2 = n - 2;
      int f1 = fibbonacci(args1);
      int f2 = fibbonacci(args2);
      int ans = f1 + f2;
      return (ans);
   }
}

int asd() {
   // Declaración de variables (VarDec)
   int result;
   int a = 5;
   int b = 3;
   // Asignación y llamada a función (StatementRest)
   result = add(a, b);
   // Bucle while (WhileStatement)
   while (result || 0) {
      result = result - 1;
   }
   return 0;
}

int main() {
   int n = 5;
   return fibbonacci(n);
}