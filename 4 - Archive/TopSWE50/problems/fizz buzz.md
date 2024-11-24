```
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> resp = new ArrayList<String>();
        for(int i = 1; i <= n; i++){
            resp.add(parse(i));
        }

        return resp;

    }

    public String parse(int n){
        boolean fizz = n % 3 == 0;
        boolean buzz = n % 5 == 0;
        if(fizz && buzz) return "FizzBuzz";
        if(fizz) return "Fizz";
        if(buzz) return "Buzz";

        return String.valueOf(n);
    }
    
}
```

Very basic problem, there is not much elegance to it, you could avoid creating the booleans if you wanted but than would not do much.

Time complexity is O(n) since it grows proportionally with growth of n.
Space complexity is O(n) since the response grows proportionally with n.