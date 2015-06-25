class MyStack {
    // Push element x onto stack.
    
    Deque<Integer> q;
    public MyStack() {
        this.q = new LinkedList<Integer> ();
    }
    
    public void push(int x) {
        q.add(x);
    }

    // Removes the element on top of the stack.
    public void pop() {
        Deque<Integer> temp = new LinkedList<Integer> ();
        while(q.size() > 1) {
            temp.add(q.poll());
        }
        q.poll();
        while(!temp.isEmpty()) {
            q.add(temp.poll());
        }
    }

    // Get the top element.
    public int top() {
        Deque<Integer> temp = new LinkedList<Integer> ();
        while(q.size() > 1) {
            temp.add(q.poll());
        }
        int res;
        res = q.poll();
        temp.add(res);
        while(!temp.isEmpty()) {
            q.add(temp.poll());
        }
        return res;
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return q.isEmpty();
    }
}
