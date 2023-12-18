use std::{cell::RefCell, fmt::Display, rc::Rc};

#[derive(Debug)]
struct SingleLinkedList {
    head_tail: Option<(Rc<RefCell<Node>>, Rc<RefCell<Node>>)>,
    len: usize,
}

impl Display for SingleLinkedList {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str("[")?;
        let mut current = match &self.head_tail {
            Some((head, _)) => Rc::clone(&head),
            None => return f.write_str("]"),
        };
        write!(f, "{}", current.borrow())?;
        while let Some(next_node) = &Rc::clone(&current).borrow().next {
            write!(f, ", {}", next_node.borrow())?;
            current = Rc::clone(next_node);
        }

        f.write_str("]")
    }
}

impl Display for Node {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

#[derive(Debug)]
struct Node {
    next: Option<Rc<RefCell<Node>>>,
    value: usize,
}

impl Node {
    fn new(value: usize) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node { next: None, value }))
    }

    fn with_next(next: Rc<RefCell<Node>>, value: usize) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node {
            next: Some(next),
            value,
        }))
    }
}

enum IndexType {
    Head,
    Middle(Rc<RefCell<Node>>),
    Tail,
}

impl SingleLinkedList {
    fn new() -> Self {
        Self {
            head_tail: None,
            len: 0,
        }
    }

    // TODO make more type: Insert(index, Head/Middle/Tail/Push)
    // fn check_index(&self, index: usize, include: bool) -> IndexType {
    //     let include = if include { 1 } else { 0 };
    //     if index > self.len - 1 + include {
    //         let message = format!(
    //             "Index {index} is out of bound. List length: {}",
    //             self.len
    //         );

    //         panic!("{}", message);
    //     };

    //     if index == 0 {
    //         IndexType::Head
    //     } else if index == self.len
    // }

    fn insert(&mut self, index: usize, to_insert: usize) {
        // TODO use enum IndexType { Head, Middle, Tail }?
        if index > self.len {
            let message = format!(
                "Failed to insert at index {index}. Index must be less or equal list length {}",
                self.len
            );

            panic!("{}", message);
        };
        // valid index

        let Some((ref head, ref tail)) = self.head_tail else {
            let new_node = Node::new(to_insert);

                self.head_tail = Some((new_node.clone(), new_node.clone()));
                self.len += 1;

                return;
        };

        if index == 0 {
            // head insertion
            let head = head.clone();
            let new_node = Node::with_next(head, to_insert);

            self.head_tail = Some((new_node.clone(), tail.clone()));
            self.len += 1;

            return;
        } else if index == self.len {
            // tail insertion
            let new_node = Node::new(to_insert);

            (*tail).borrow_mut().next = Some(new_node.clone());

            self.head_tail = Some((head.clone(), new_node.clone()));
            self.len += 1;

            return;
        }

        let cur_node = self
            .find_node(index - 1)
            .expect("index must be less than len after previous check");

        let mut borrow_cur_node = cur_node.borrow_mut();

        let next_node = borrow_cur_node
            .next
            .as_ref()
            .expect("node exists after previous checks")
            .clone();
        let new_node = Node::with_next(next_node, to_insert);

        borrow_cur_node.next = Some(new_node.clone());
    }

    // TODO -> Rc<RefCell<Node>>>
    // and use enum type
    fn find_node(&self, index: usize) -> Option<Rc<RefCell<Node>>> {
        if index > self.len {
            return None;
        }

        let mut cur_node = match self.head_tail {
            Some((ref cur_node, _)) => cur_node.clone(),
            None => return None,
        };
        let mut cur_index = 0;

        while cur_index < index {
            cur_node = {
                let borrow_cur_node = cur_node.borrow();
                cur_index += 1;

                match borrow_cur_node.next {
                    Some(ref next_node) => next_node.clone(),
                    None => unreachable!(),
                }
            }
        }

        Some(cur_node)
    }

    fn push(&mut self, to_push: usize) {
        self.insert(self.len, to_push);
    }

    fn remove(&mut self, index: usize) -> usize {
        if index >= self.len {
            let message = format!(
                "Failed to remove at index {index}. Index must be less list length {}",
                self.len
            );

            panic!("{}", message);
        };

        let (head, tail) = match self.head_tail {
            Some((ref head, ref tail)) => (head.clone(), tail.clone()),
            None => unreachable!(),
        };

        if index == 0 {
            let head = head.borrow();

            self.len -= 1;

            match head.next {
                Some(ref next_node) => {
                    self.head_tail = Some((next_node.clone(), tail));
                    return head.value;
                }
                None => {
                    self.head_tail = None;
                    return head.value;
                }
            };
        } else if index == self.len - 1 {
            let prev_node = self.find_node(index - 1).expect("previous node must exist");

            let value = prev_node
                .borrow()
                .next
                .as_ref()
                .expect("node to remove must exist")
                .borrow()
                .value;

            prev_node.borrow_mut().next = None;
            self.head_tail = Some((head, prev_node));

            self.len -= 1;

            return value;
        };

        let prev_node = self
            .find_node(index - 1)
            .expect("index must be less than len after previous check");

        let value;

        let next_node = {
            let to_remove = match &prev_node.borrow().next {
                Some(to_remove) => to_remove.clone(),
                None => unreachable!(),
            };

            let to_remove = to_remove.borrow();

            value = to_remove.value;

            let x = match &to_remove.next {
                Some(next) => Some(next.clone()),
                None => None,
            };
            x
        };

        match next_node {
            Some(ref next_node) => {
                prev_node.borrow_mut().next = Some(next_node.clone());
            }
            None => {
                prev_node.borrow_mut().next = None;
            }
        }

        self.len -= 1;

        value
    }

    fn pop(&mut self) -> usize {
        self.remove(self.len - 1)
    }

    fn set(&mut self, index: usize, value: usize) {
        if index >= self.len {
            let message = format!(
                "Failed to set at index {index}. Index must be less list length {}",
                self.len
            );

            panic!("{}", message);
        };

        let node = self.find_node(index).expect("node must exist");

        node.borrow_mut().value = value;
    }

    fn get(&self, index: usize) -> usize {
        if index >= self.len {
            let message = format!(
                "Failed to get at index {index}. Index must be less list length {}",
                self.len
            );

            panic!("{}", message);
        };

        let node = self.find_node(index).expect("node must exist");

        let value = node.borrow().value;

        value
    }
}

impl FromIterator<usize> for SingleLinkedList {
    fn from_iter<I: IntoIterator<Item = usize>>(iter: I) -> Self {
        let mut sll = SingleLinkedList::new();
        for item in iter {
            sll.push(item);
        }
        sll
    }
}

fn main() {
    // CRUD
    // C - CREATE
    // R - READ
    // U - UPDATE
    // D - DELETE

    let mut std_sll = std::collections::LinkedList::new();

    let now = std::time::Instant::now();
    for elem in 0..1_000_000 {
        std_sll.push_back(elem);
    }
    println!("Time elapsed: {:?}", now.elapsed());

    let mut sll = SingleLinkedList::new();
    let now = std::time::Instant::now();
    for elem in 0..1_000_000 {
        sll.push(elem);
    }
    println!("Time elapsed: {:?}", now.elapsed());

    // println!("{}", sll);
}

#[cfg(test)]
mod tests {
    use expect_test::{expect, Expect};

    use super::*;

    fn create_list() -> SingleLinkedList {
        SingleLinkedList::from_iter([1, 2, 3, 4, 5])
    }

    fn assert_from_iter(iter: impl IntoIterator<Item = usize>, expect: Expect) {
        let actual = SingleLinkedList::from_iter(iter);
        expect.assert_eq(&actual.to_string());
    }

    fn assert_eq(actual: &str, expect: Expect) {
        expect.assert_eq(actual);
    }

    #[test]
    fn smoke_list() {
        assert_from_iter(vec![1, 2, 3], expect!["[1, 2, 3]"])
    }

    #[test]
    fn empty() {
        let actual = SingleLinkedList::new().to_string();
        let expected = expect![[r#"[]"#]];
        expected.assert_eq(&actual);
    }

    #[test]
    fn insert_zero_index() {
        let mut sll = SingleLinkedList::new();

        sll.insert(0, 5);
        assert_eq(&sll.to_string(), expect!["[5]"]);

        sll.insert(0, 4);
        assert_eq(&sll.to_string(), expect!["[4, 5]"]);

        sll.insert(0, 3);
        assert_eq(&sll.to_string(), expect!["[3, 4, 5]"]);

        sll.insert(0, 2);
        assert_eq(&sll.to_string(), expect!["[2, 3, 4, 5]"]);

        sll.insert(0, 1);
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4, 5]"]);
    }

    #[test]
    fn insert_middle_index() {
        let mut sll = SingleLinkedList::new();

        sll.insert(0, 1);
        assert_eq(&sll.to_string(), expect!["[1]"]);

        sll.insert(1, 3);
        assert_eq(&sll.to_string(), expect!["[1, 3]"]);

        sll.insert(2, 5);
        assert_eq(&sll.to_string(), expect!["[1, 3, 5]"]);

        sll.insert(2, 4);
        assert_eq(&sll.to_string(), expect!["[1, 3, 4, 5]"]);

        sll.insert(1, 2);
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4, 5]"]);
    }

    #[test]
    fn insert_last_index() {
        let mut sll = SingleLinkedList::new();

        sll.insert(0, 1);
        assert_eq(&sll.to_string(), expect!["[1]"]);

        sll.insert(1, 2);
        assert_eq(&sll.to_string(), expect!["[1, 2]"]);

        sll.insert(2, 3);
        assert_eq(&sll.to_string(), expect!["[1, 2, 3]"]);

        sll.insert(3, 4);
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4]"]);

        sll.insert(4, 5);
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4, 5]"]);
    }

    #[test]
    fn remove_head() {
        let mut sll = create_list();

        let mut value = sll.remove(0);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["1, [2, 3, 4, 5]"],
        );

        value = sll.remove(0);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["2, [3, 4, 5]"],
        );

        value = sll.remove(0);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["3, [4, 5]"],
        );

        value = sll.remove(0);
        assert_eq(&format!("{value}, {}", sll.to_string()), expect!["4, [5]"]);

        value = sll.remove(0);
        assert_eq(&format!("{value}, {}", sll.to_string()), expect!["5, []"]);
    }

    #[test]
    fn remove_tail() {
        let mut sll = create_list();

        let mut value = sll.remove(sll.len - 1);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["5, [1, 2, 3, 4]"],
        );

        value = sll.remove(sll.len - 1);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["4, [1, 2, 3]"],
        );

        value = sll.remove(sll.len - 1);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["3, [1, 2]"],
        );

        value = sll.remove(sll.len - 1);
        assert_eq(&format!("{value}, {}", sll.to_string()), expect!["2, [1]"]);

        value = sll.remove(sll.len - 1);
        assert_eq(&format!("{value}, {}", sll.to_string()), expect!["1, []"]);
    }

    #[test]
    fn remove_middle() {
        let mut sll = create_list();

        let mut value = sll.remove(3);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["4, [1, 2, 3, 5]"],
        );

        value = sll.remove(2);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["3, [1, 2, 5]"],
        );

        value = sll.remove(1);
        assert_eq(
            &format!("{value}, {}", sll.to_string()),
            expect!["2, [1, 5]"],
        );

        value = sll.remove(1);
        assert_eq(&format!("{value}, {}", sll.to_string()), expect!["5, [1]"]);

        value = sll.remove(0);
        assert_eq(&format!("{value}, {}", sll.to_string()), expect!["1, []"]);
    }

    #[test]
    fn get_head_from_non_empty() {
        let sll = create_list();

        assert_eq(&sll.get(0).to_string(), expect!["1"]);
    }

    #[test]
    fn get_middle_from_non_empty() {
        let sll = create_list();

        assert_eq(&sll.get(2).to_string(), expect!["3"]);
    }

    #[test]
    fn get_tail_from_non_empty() {
        let sll = create_list();

        assert_eq(&sll.get(sll.len - 1).to_string(), expect!["5"]);
    }

    #[test]
    fn set_head_non_empty() {
        let mut sll = create_list();

        sll.set(0, 0);
        assert_eq(&sll.to_string(), expect!["[0, 2, 3, 4, 5]"]);
    }

    #[test]
    fn set_middle_non_empty() {
        let mut sll = create_list();

        sll.set(1, 0);
        assert_eq(&sll.to_string(), expect!["[1, 0, 3, 4, 5]"]);

        sll.set(2, 0);
        assert_eq(&sll.to_string(), expect!["[1, 0, 0, 4, 5]"]);

        sll.set(3, 0);
        assert_eq(&sll.to_string(), expect!["[1, 0, 0, 0, 5]"]);
    }

    #[test]
    fn set_tail_non_empty() {
        let mut sll = create_list();

        sll.set(4, 0);
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4, 0]"]);
    }

    #[test]
    #[should_panic(expected = "Failed to set at index")]
    fn set_panic() {
        let mut sll = create_list();

        sll.set(100, 100);
    }
}
