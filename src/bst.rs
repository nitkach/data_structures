#[derive(Debug)]
pub struct Tree {
    root: Option<Box<Node>>,
}

#[derive(Debug)]
struct Node {
    value: usize,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Tree {
    pub fn new() -> Self {
        Self { root: None }
    }

    pub fn insert(&mut self, to_insert: usize) {
        let mut node = match self.root {
            Some(ref mut node) => node,
            None => return self.root = Some(Box::new(Node::new(to_insert))),
        };

        loop {
            match node.value.cmp(&to_insert) {
                std::cmp::Ordering::Greater => {
                    let Some(ref mut left_node) = node.left else {
                        node.left = Some(Box::new(Node::new(to_insert)));
                        return
                    };
                    node = left_node;
                }
                std::cmp::Ordering::Equal => unreachable!(),
                std::cmp::Ordering::Less => {
                    let Some(ref mut right_node) = node.right else {
                        node.right = Some(Box::new(Node::new(to_insert)));
                        return
                    };
                    node = right_node;
                }
            }
        }
    }

    pub fn contains(&self, to_find: usize) -> bool {
        let mut node = match &self.root {
            Some(node) => node,
            None => return false,
        };
        loop {
            match node.value.cmp(&to_find) {
                std::cmp::Ordering::Greater => {
                    // go left
                    let Some(ref left_node) = &node.left else {
                        return false;
                    };
                    node = left_node;
                }
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Less => {
                    // go right
                    let Some(ref right_node) = &node.right else {
                        return false;
                    };
                    node = right_node;
                }
            }
        }
    }

    pub fn traverse(&self) -> String {
        let mut buf = String::new();
        let Some(ref node) = self.root else {
            return buf;
        };
        node.traverse(&mut buf);
        buf
    }

    pub fn remove(&mut self, to_remove: usize) -> Option<usize> {
        // reference to node
        let ref_remove_node = Self::find_node(&mut self.root, to_remove)?;

        let remove_node = ref_remove_node
            .as_mut()
            .expect("The node exist if it was found to have the value");

        let removed_value = match (&remove_node.left, &remove_node.right) {
            (None, None) => {
                // *ref_remove_node = None;
                ref_remove_node.take().unwrap().value
            }
            (None, Some(_)) => {
                // *ref_remove_node = std::mem::take(&mut remove_node.right);
                let right_subtree = remove_node
                    .right
                    .take()
                    .expect("At least one node in right subtree was found earlier");
                ref_remove_node
                    .replace(right_subtree)
                    .expect("Node with value to remove exist, since it was found earlier")
                    .value
            }
            (Some(_), None) => {
                // *ref_remove_node = std::mem::take(&mut remove_node.left);
                let left_subtree = remove_node
                    .left
                    .take()
                    .expect("At least one node in left subtree was found earlier");
                ref_remove_node
                    .replace(left_subtree)
                    .expect("Node with value to remove exist, since it was found earlier")
                    .value
            }
            (Some(_), Some(_)) => {
    /*
            5
           / \
          2   8
         / \   \
        1   3   23
               /  \
             20    30
                  /  \
                27    31
                  \
                   28
    */
                // search for smallest number in right subtree
                let ref_min = Self::find_min_node(&mut remove_node.right);

                let owned_min = ref_min
                    .take()
                    .expect("Node with minimum value exist, since it was found earlier");
                *ref_min = owned_min.right;

                std::mem::replace(&mut remove_node.value, owned_min.value)
            }
        };
        Some(removed_value)
    }

    fn find_node(node: &mut Option<Box<Node>>, needle: usize) -> Option<&mut Option<Box<Node>>> {
        let mut cur = node;
        loop {
            match cur.as_mut()?.value.cmp(&needle) {
                std::cmp::Ordering::Equal => return Some(cur),
                std::cmp::Ordering::Less => {
                    cur = &mut cur.as_mut().unwrap().right;
                }
                std::cmp::Ordering::Greater => {
                    cur = &mut cur.as_mut().unwrap().left;
                }
            }
        }
    }

    fn find_min_node(node: &mut Option<Box<Node>>) -> &mut Option<Box<Node>> {
        let mut cur = node;
        loop {
            match cur
                .as_mut()
                .expect("Node exist, since it was found earlier")
                .left
            {
                Some(_) => cur = &mut cur.as_mut().unwrap().left,
                None => return cur,
            }
        }
    }
}

impl Node {
    fn new(value: usize) -> Self {
        Self {
            value,
            left: None,
            right: None,
        }
    }

    fn traverse(&self, buf: &mut String) {
        if let Some(ref node) = self.left {
            Self::traverse(node, buf)
        }
        buf.push_str(&format!("{} ", self.value));
        if let Some(ref node) = self.right {
            Self::traverse(node, buf)
        }
    }
}

#[cfg(test)]
mod tests {
    use expect_test::expect;

    use super::*;

    fn create_tree() -> Tree {
        let mut tree = Tree::new();

        tree.insert(2);
        tree.insert(1);
        tree.insert(3);

        tree
    }

    #[test]
    fn smoke() {
        let mut tree = Tree::new();

        tree.insert(5);
        tree.insert(2);
        tree.insert(8);
        tree.insert(3);
        tree.insert(1);
        tree.insert(23);
        tree.insert(30);
        tree.insert(20);
        tree.insert(27);
        tree.insert(31);
        tree.insert(28);

    /*
            5
           / \
          2   8
         / \   \
        1   3   23
               /  \
             20    30
                  /  \
                27    31
                  \
                   28
    */

        let expected = expect!["1 2 3 5 8 20 23 27 28 30 31 "];
        expected.assert_eq(&tree.traverse());

        assert_eq!(tree.remove(23), Some(23));
        let expected = expect!["1 2 3 5 8 20 27 28 30 31 "];
        expected.assert_eq(&tree.traverse());
        /*
                5                   5
               / \                 / \
              2   8               2   8
             / \   \             / \   \
            1   3   23          1   3   27
                   /  \      ->        /  \
                 20    30            20    30
                      /  \                /  \
                    27    31            28    31
                      \
                       28
        */

        assert_eq!(tree.remove(5), Some(5));
        let expected = expect!["1 2 3 8 20 27 28 30 31 "];
        expected.assert_eq(&tree.traverse());
        /*
                5                   8
               / \                 / \
              2   8               2   \
             / \   \             / \   \
            1   3   27          1   3   27
                   /  \      ->        /  \
                 20    30            20    30
                      /  \                /  \
                    28    31            28    31
        */
    }

    #[test]
    fn test_insert() {
        let mut tree = Tree::new();

        tree.insert(10);
        tree.insert(5);
        tree.insert(6);
        tree.insert(3);
        tree.insert(12);
        tree.insert(11);

        let expected = expect!["3 5 6 10 11 12 "];
        expected.assert_eq(&tree.traverse());
    }

    #[test]
    fn test_remove_root() {
        let mut tree = create_tree();

        assert_eq!(tree.remove(2), Some(2));

        let expected = expect!["1 3 "];
        expected.assert_eq(&tree.traverse());
    }

    #[test]
    fn remove_no_child() {
        let mut tree = create_tree();

        assert_eq!(tree.remove(1), Some(1));

        let expected = expect!["2 3 "];
        expected.assert_eq(&tree.traverse());
    }

    #[test]
    fn remove_one_child() {
        let mut tree = create_tree();

        tree.insert(4);

        assert_eq!(tree.remove(3), Some(3));

        let expected = expect!["1 2 4 "];
        expected.assert_eq(&tree.traverse());
    }

    #[test]
    fn remove_two_child() {
        let mut tree = create_tree();

        tree.insert(5);
        tree.insert(4);
        tree.insert(6);

        assert_eq!(tree.remove(5), Some(5));

        let expected = expect!["1 2 3 4 6 "];
        expected.assert_eq(&tree.traverse());
    }
}
