use std::{cell::RefCell, fmt::Display, rc::Rc};

#[derive(Debug)]
struct SingleLinkedList {
    head: Option<Rc<RefCell<Node>>>,
    tail: Option<Rc<RefCell<Node>>>,
    len: usize,
}

impl Display for SingleLinkedList {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str("[")?;
        let mut current = match &self.head {
            Some(head) => Rc::clone(&head),
            None => return f.write_str("]"),
        };
        write!(f, "{}", current.borrow())?;
        while let Some(next_node) = &Rc::clone(&current).borrow().next {
            write!(f, ", {}", next_node.borrow())?;
            current = Rc::clone(next_node);
        }

        f.write_str("]")

        // fn recursive(current: &Rc<RefCell<Node>>, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        //     let borrow_current = current.borrow();
        //     write!(f, "{}", borrow_current)?;
        //     match borrow_current.next {
        //         Some(ref next_node) => {
        //             f.write_str(", ")?;
        //             recursive(next_node, f)
        //         },
        //         None => return Ok(()),
        //     }
        // }

        // f.write_str("[")?;

        // match self.head {
        //     Some(ref head) => recursive(head, f)?,
        //     None => return f.write_str("]"),
        // };

        // let mut cur_node = match self.head {
        //     Some(ref head) => head.clone(),
        //     None => return f.write_str("]"),
        // };

        // loop {
        //     write!(f, "{}", cur_node.borrow())?;
        //     if cur_node.borrow().next.is_none() {
        //         break;
        //     }
        //     cur_node = {
        //         f.write_str(", ")?;
        //         let ref_cur_node = cur_node.borrow();
        //         match ref_cur_node.next {
        //             Some(ref next_node) => next_node.clone(),
        //             None => unreachable!(),
        //         }
        //     }
        // }
        // f.write_str("]")

        // while cur_node.borrow().next.is_some() {
        //     cur_node = {
        //         write!(f, "{}", cur_node.borrow())?;
        //         let ref_next_node = cur_node.borrow();
        //         let next_node = match ref_next_node.next {
        //             Some(ref next_node) => next_node.clone(),
        //             None => unreachable!(),
        //         };
        //         next_node
        //     };
        // };
        // --------------------------------------
        //
        // --------------------------------------
        // let mut current = match &self.head {
        //     Some(current) => current.clone(),
        //     None => return f.write_str("]"),
        // };

        // loop {
        //     write!(f, "{}", current.borrow())?;

        //     if let Some(next_node) = &current.borrow().next {
        //         current = next_node.clone();
        //     } else {
        //         break;
        //     };
        // }
        // --------------------------------------
        // let mut current = &self.head;

        // loop {
        //     current = {
        //         if let Some(new_node) = current {
        //             write!(f, "{}", new_node.borrow())?;
        //             let borrow = (**new_node).borrow();
        //             let x = &borrow.next;
        //             x
        //         } else {
        //             break;
        //         }
        //     };
        // }
        // --------------------------------------
        // let mut current = match self.head {
        //     Some(ref current) => current.clone(),
        //     None => return f.write_str("]"),
        // };

        // while let Some(ref next_node) = current.borrow().next {
        //     write!(f, "{}", next_node.borrow())?;
        //     current = next_node.clone()
        // }
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

impl SingleLinkedList {
    fn new() -> Self {
        Self {
            head: None,
            tail: None,
            len: 0,
        }
    }

    fn insert(&mut self, index: usize, to_insert: usize) -> Result<(), String> {
        if index > self.len {
            // TODO panic
            return Err(format!(
                "Failed to insert at index {index}. Index must be less or equal list length {}",
                self.len
            ));
        }
        // valid index

        // Option<(self.head, self.tail)>
        // Option<HeadTail>
        // TODO
        // match (self.head, self.tail) {
        //     (None, None) => todo!(),
        //     (Some(_), Some(_)) => todo!(),
        //     _ => unreachable!()
        // }
        if let None = self.head {
            let new_node = Node::new(to_insert);

            self.head = Some(new_node.clone());
            self.tail = Some(new_node.clone());
            self.len += 1;

            return Ok(());
        } else if index == 0 {
            // head insertion
            let head = self
                .head
                .as_ref()
                .expect("at least one node (head and tail) exists")
                .clone();
            let new_node = Node::with_next(head, to_insert);

            self.head = Some(new_node.clone());
            self.len += 1;

            return Ok(());
        } else if index == self.len {
            // tail insertion
            let tail = self
                .tail
                .as_ref()
                .expect("at least one node (head and tail) exists");
            let new_node = Node::new(to_insert);

            (*tail).borrow_mut().next = Some(new_node.clone());

            self.tail = Some(new_node.clone());
            self.len += 1;

            return Ok(());
        }

        let cur_node = self.find_node(index - 1).unwrap();

        let mut borrow_cur_node = cur_node.borrow_mut();

        let next_node = borrow_cur_node
            .next
            .as_ref()
            .expect("node exists after previous checks")
            .clone();
        let new_node = Node::with_next(next_node, to_insert);

        borrow_cur_node.next = Some(new_node.clone());

        Ok(())
    }

    fn find_node(&self, index: usize) -> Option<Rc<RefCell<Node>>> {
        if index > self.len {
            return None;
        }

        let mut cur_node = match self.head {
            Some(ref cur_node) => cur_node.clone(),
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
        self.insert(self.len, to_push).expect("push cannot fail");
    }
}

impl FromIterator<usize> for SingleLinkedList {
    fn from_iter<T: IntoIterator<Item = usize>>(iter: T) -> Self {
        let mut sll = SingleLinkedList::new();
        for item in iter {
            sll.push(item);
        }
        sll
    }
}

fn main() {
    let mut sll = SingleLinkedList::new();

    // Rc::get_mut()
    // RefCell::borrow_mut()

    // sll.push(1);
    // sll.push(2);
    // sll.push(3);

    dbg!(sll.insert(1, 4).unwrap_err());

    println!("{sll}");
}

#[cfg(test)]
mod tests {
    use expect_test::{expect, Expect};

    use super::*;

    fn assert_from_iter(iter: impl IntoIterator<Item = usize>, expect: Expect) {
        let actual = SingleLinkedList::from_iter(iter);
        expect.assert_eq(&actual.to_string());
    }

    fn assert_eq(actual: &str, expect: Expect) {
        expect.assert_eq(actual);
    }

    #[test]
    fn smoke_test() {
        assert_from_iter(vec![1, 2, 3], expect!["[1, 2, 3]"])
    }

    #[test]
    fn test_empty() {
        let actual = SingleLinkedList::new().to_string();
        let expected = expect![[r#"[]"#]];
        expected.assert_eq(&actual);
    }

    #[test]
    fn test_insert_index_zero() {
        let mut sll = SingleLinkedList::new();

        sll.insert(0, 4).unwrap();
        assert_eq(&sll.to_string(), expect![["[4]"]]);

        sll.insert(0, 3).unwrap();
        assert_eq(&sll.to_string(), expect![["[3, 4]"]]);

        sll.insert(0, 2).unwrap();
        assert_eq(&sll.to_string(), expect!["[2, 3, 4]"]);

        sll.insert(0, 1).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4]"]);
    }

    #[test]
    fn test_insert_index_middle() {
        let mut sll = SingleLinkedList::new();

        sll.insert(0, 1).unwrap();
        assert_eq(&sll.to_string(), expect!["[1]"]);

        sll.insert(1, 4).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 4]"]);

        sll.insert(1, 3).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 3, 4]"]);

        sll.insert(1, 2).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4]"]);
    }

    #[test]
    fn test_insert_index_last() {
        let mut sll = SingleLinkedList::new();

        sll.insert(0, 1).unwrap();
        assert_eq(&sll.to_string(), expect!["[1]"]);

        sll.insert(1, 2).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 2]"]);

        sll.insert(2, 3).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 2, 3]"]);

        sll.insert(3, 4).unwrap();
        assert_eq(&sll.to_string(), expect!["[1, 2, 3, 4]"]);
    }
}
