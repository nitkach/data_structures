fn main() {
    let mut dll = data_structures::dll::DoubleLinkedList::<i32>::new();

    dll.push_back(1);
    dll.push_back(2);
    dll.push_back(3);
    dll.push_back(4);

    println!("{dll}");

    dll.pop_front();
    dll.pop_front();
    dll.pop_front();
    dll.pop_front();

    println!("{dll}");
}
