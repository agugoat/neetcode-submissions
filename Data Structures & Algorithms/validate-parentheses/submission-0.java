class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

     for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false; // Stack is empty, no matching opening bracket
                }

                char top = stack.pop(); // Pop the top element (most recent opening bracket)

                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false; // Mismatched brackets
                }
            }
        }

        return stack.isEmpty(); // Ensure all brackets are matched
    }
    }

