class Solution {
public:
    /*
     * @param n: an integer
     * @return: an ineger f(n)
     */
    int fibonacci(int n) {
        if ( n > 4 )
        return fibonacci(n-2)*2+fibonacci(n-3);
        if ( n > 2 )
        return fibonacci(n-1)+fibonacci(n-2);
        else if ( n == 1 )
        return 0;
        else if ( n == 2 )
        return 1;
        // write your code here
    }
};
