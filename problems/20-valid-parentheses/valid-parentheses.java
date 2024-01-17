class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        java.util.Map<Character, Character> d = new java.util.HashMap<>();
        d.put(')', '(');
        d.put('}', '{');
        d.put(']', '[');
        for (char i:s.toCharArray()) {
            if (i=='(' || i=='{' || i=='[')
                stk.push(i);
            else if (i==')' || i=='}' || i==']'){
                if (!stk.isEmpty() && stk.peek()==d.get(i))
                    stk.pop();
                else
                    return false;
            }
        }
        return stk.isEmpty();
    }
}