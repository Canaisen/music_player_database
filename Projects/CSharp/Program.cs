using System.Reflection;

      static int factorial(int a){
    int result = 1 ;

    if (a>0)
    {
        for (int i = 1; i < a; i++)
        {
            result=result*i;
        }
        
    }
    return result;
}

       static void Main(string[] args){

        Console.WriteLine(factorial(10));


    }
     
    

    