#[derive(Debug)]
struct Tree {
    root: Option<Box<Node>>,
}

#[derive(Debug)]
struct Node {
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Tree {
    fn new() -> Self {
        Self { root: None }
    }

    fn insert(&mut self, to_insert: i32) {
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

    fn contains(&self, to_find: i32) -> bool {
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

    fn traverse(&self) {
        let Some(ref node) = self.root else {
            return;
        };
        node.traverse();
    }

    fn remove(&mut self, to_remove: i32) -> Option<i32> {
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

    fn find_node(node: &mut Option<Box<Node>>, needle: i32) -> Option<&mut Option<Box<Node>>> {
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
    fn new(value: i32) -> Self {
        Self {
            value,
            left: None,
            right: None,
        }
    }

    fn traverse(&self) {
        if let Some(ref node) = self.left {
            Self::traverse(node)
        }
        println!("{}", self.value);

        if let Some(ref node) = self.right {
            Self::traverse(node)
        }
    }
}

fn main() {
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
    tree.traverse();

    println!("{}", tree.contains(10));

    // println!("\nremoved: {}", tree.remove(8).unwrap());
    // tree.traverse();

    println!("\nremoved: {}", tree.remove(23).unwrap());
    tree.traverse();
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
    dbg!(&tree);

    println!("\nremoved: {}", tree.remove(5).unwrap());
    tree.traverse();
    /*
            5                   8
           / \                 / \
          2   8               2   27
         / \   \             / \   \
        1   3   27          1   3   |\
               /  \      ->        /  \
             20    30            20    30
                  /  \                /  \
                28    31            28    31
    */
    dbg!(tree);
}
