use std::{rc::{Rc, Weak}, cell::RefCell, fmt::Display};

struct Node<T: Copy> {
    next: Option<Rc<RefCell<Node<T>>>>,
    prev: Option<Weak<RefCell<Node<T>>>>,
    value: T,
}

impl<T: Copy> Node<T> {
    fn new(value: T) -> Rc<RefCell<Self>> {
        Rc::new(RefCell::new(Self { value, next: None, prev: None }))
    }
}

impl<T: Copy + Display> Display for Node<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

pub struct DoubleLinkedList<T: Copy> {
    head_tail: Option<(Rc<RefCell<Node<T>>>, Weak<RefCell<Node<T>>>)>,
    len: usize
}

impl<T: Copy + Display> Display for DoubleLinkedList<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str("[")?;

        let mut current = match self.head_tail {
            Some((ref head, _)) => Rc::clone(head),
            None => return f.write_str("]"),
        };
        write!(f, "{}", RefCell::borrow(&current))?;
        while let Some(ref next_node) = Rc::clone(&current).borrow().next {
            write!(f, ", {}", RefCell::borrow(&next_node))?;
            current = Rc::clone(&next_node);
        }

        f.write_str("]")
    }
}

impl<T: Copy> DoubleLinkedList<T> {
    pub fn new() -> Self {
        Self { head_tail: None, len: 0 }
    }

    //               [ ]      | .push_back(1)
    //          H -> [1] <~ T | .push_back(2)
    // H -> [1] <~-> [2] <~ T |
    pub fn push_back(&mut self, value: T) {
        let new_node = Node::new(value);

        match self.head_tail {
            None => {
                self.head_tail = Some((Rc::clone(&new_node), Rc::downgrade(&new_node)));
            },
            Some((ref head, ref tail)) => {
                // create weak reference to tail in new node
                new_node.borrow_mut().prev = Some(Weak::clone(tail));

                // create reference in tail to new node (and new tail)
                tail.upgrade().unwrap().borrow_mut().next = Some(Rc::clone(&new_node));

                // update to new tail
                self.head_tail = Some((Rc::clone(&head), Rc::downgrade(&new_node)));
            },
        }
    }

    pub fn pop_back(&mut self) -> Option<T> {
        let value;
        match self.head_tail {
            None => return None,
            Some((ref head, ref tail)) => {
                let tail = tail.upgrade().unwrap();
                value = tail.borrow().value;

                match tail.borrow().prev {
                    None => {
                        // zero nodes left
                        self.head_tail = None;
                    },
                    Some(ref new_last_node) => {
                        let new_last_node = new_last_node.upgrade().unwrap();

                        new_last_node.borrow_mut().next = None;

                        self.head_tail = Some((Rc::clone(&head), Rc::downgrade(&new_last_node)));
                    },
                };
            }
        };
        Some(value)
    }

    pub fn push_front(&mut self, value: T) {
        let new_node = Node::new(value);

        match self.head_tail {
            None => {
                self.head_tail = Some((Rc::clone(&new_node), Rc::downgrade(&new_node)));
            },
            Some((ref head, ref tail)) => {
                new_node.borrow_mut().next = Some(Rc::clone(head));

                head.borrow_mut().prev = Some(Rc::downgrade(&new_node));

                self.head_tail = Some((Rc::clone(&new_node), Weak::clone(&tail)));
            },
        }
    }

    pub fn pop_front(&mut self) -> Option<T> {
        let value;
        match self.head_tail {
            None => return None,
            Some((ref head, ref tail)) => {
                let head = Rc::clone(head);
                value = head.borrow().value;

                match head.borrow().next {
                    None => {
                        self.head_tail = None
                    },
                    Some(ref new_head_node) => {
                        let new_head_node = Rc::clone(&new_head_node);

                        new_head_node.borrow_mut().prev = None;

                        self.head_tail = Some((Rc::clone(&new_head_node), Weak::clone(&tail)));
                    },
                };
            },
        }
        Some(value)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn smoke_front() {
        let mut list = DoubleLinkedList::<i32>::new();

        list.push_front(1);
        list.push_front(2);
        list.push_front(3);
        list.push_front(4);

        assert_eq!(list.pop_front(), Some(4));
        assert_eq!(list.pop_front(), Some(3));
        assert_eq!(list.pop_front(), Some(2));
        assert_eq!(list.pop_front(), Some(1));
        assert_eq!(list.pop_front(), None);
    }

    #[test]
    fn smoke_back() {
        let mut list = DoubleLinkedList::<i32>::new();

        list.push_back(1);
        list.push_back(2);
        list.push_back(3);
        list.push_back(4);

        assert_eq!(list.pop_back(), Some(4));
        assert_eq!(list.pop_back(), Some(3));
        assert_eq!(list.pop_back(), Some(2));
        assert_eq!(list.pop_back(), Some(1));
        assert_eq!(list.pop_back(), None);
    }
}
