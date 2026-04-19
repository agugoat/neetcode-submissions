class DynamicArray {
     public int [] array;
     public int size;
    public DynamicArray(int capacity) {
    array = new int [capacity];
    }

    public int get(int i) {
    return array[i];
    }

    public void set(int i, int n) {
    array[i] = n;
    }

    public void pushback(int n) {
    if(size == array.length) {
    resize();
    }
    
    array[size] = n;
    size++;
    }

    public int popback() {
     int lastElement = array[size-1];
     size--;
     return lastElement;
    }

    private void resize() {
    int resize = array.length * 2;
    int [] resizeArray = new int [resize];
    
    System.arraycopy(array, 0, resizeArray, 0, array.length);

    array = resizeArray;
    }

    public int getSize() {
    return size;
    }


    public int getCapacity() {
    return array.length;
    }
}

