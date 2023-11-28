use std::{
    collections::{btree_map::Entry, BTreeMap},
    fmt::Display,
    str::Chars,
};

#[derive(Debug)]
struct Trie {
    root: Node,
}

impl Display for Trie {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        fn recursive(
            main_node: &Node,
            f: &mut std::fmt::Formatter<'_>,
            indent: &mut Indent,
        ) -> std::fmt::Result {
            // more than 2 nodes: the first one will go to the firsts,
            // the second one will hit the lasts
            // dbg!(&indent);
            if main_node.child.len() > 1 {
                // remember level of nesting to print '│' in future nesting
                // levels

                // nodes without last node
                let firsts = main_node.child.iter().take(main_node.child.len() - 1);

                for (symbol, node) in firsts {
                    write!(f, "{}", indent.get())?;

                    write!(f, "├──{symbol}")?;

                    if node.is_word {
                        write!(f, " *")?;
                    }

                    writeln!(f)?;

                    // indent.add_spaces();
                    indent.add_bar();
                    // dbg!(&indent);

                    recursive(node, f, indent)?;
                    indent.truncate();
                }

                // remove nesting level, otherwise the last node will have
                // a trailing vertical bar
                // indent.remove_indent();
                // indent.add_bar();
            }

            let last = &main_node.child.iter().last();
            if let Some((symbol, node)) = last {
                write!(f, "{}", indent.get())?;

                write!(f, "└──{symbol}")?;

                if node.is_word {
                    write!(f, " *")?;
                }

                writeln!(f)?;

                indent.add_spaces();
                recursive(node, f, indent)?;
                indent.truncate();
            }

            Ok(())
        }
        let mut indent = Indent::new();

        if self.root.is_word {
            writeln!(f, "*")?;
        }

        recursive(&self.root, f, &mut indent)
    }
}

#[derive(Debug)]
struct Indent {
    indent: String,
}

impl Indent {
    fn new() -> Self {
        Self {
            indent: String::new(),
        }
    }

    fn get(&self) -> &str {
        &self.indent
    }

    fn add_spaces(&mut self) {
        let indent = "   ";
        self.indent.push_str(indent);
    }

    fn add_bar(&mut self) {
        self.indent.push_str("│  ");
    }

    fn truncate(&mut self) {
        for _ in 0..3 {
            self.indent.pop().expect("for each call add indent, 3 characters are added");
        }
    }
}

impl Trie {
    fn new() -> Self {
        Self {
            root: Node::new(false),
        }
    }

    fn insert(&mut self, word: &str) {
        // let mut node = self.root.get_or_insert_with(|| Node::new(false));
        let mut node = &mut self.root;

        for char in word.chars() {
            node = node.insert(char);
        }
        node.is_word = true;
    }

    fn contains(&self, word: &str) -> bool {
        if word.is_empty() {
            return true;
        }
        let mut node = &self.root;

        for char in word.chars() {
            node = match node.contains(char) {
                Some(node) => node,
                None => return false,
            };
        }

        true
    }

    fn words(&self) -> Vec<String> {
        let mut words = Vec::<String>::new();

        // if self.root.child.len() == 0
        let node = &self.root;
        let mut buf = String::new();
        Trie::search_words(node, &mut words, &mut buf);
        words
    }

    fn search_words(main_node: &Node, words: &mut Vec<String>, buf: &mut String) {
        if main_node.is_word {
            words.push(buf.clone());
        }

        for (char, child_node) in &main_node.child {
            buf.push(*char);

            Trie::search_words(child_node, words, buf);

            buf.pop();
        }
    }

    // -> bool
    fn remove(&mut self, word: &str) {
        let chars = word.chars();
        let node = &mut self.root;

        match Self::recursive_remove(node, chars) {
            RemoveState::NoSuchWord => println!("Word not found: \"{word}\" "),
            _ => println!("Word successfully deleted: \"{word}\" "),
        };
    }

    fn recursive_remove(main_node: &mut Node, mut word: Chars) -> RemoveState {
        let symbol = match word.next() {
            Some(symbol) => symbol,
            None => {
                if !main_node.is_word {
                    return RemoveState::NoSuchWord;
                }

                main_node.is_word = false;
                return if main_node.child.len() == 0 {
                    RemoveState::LeafNode
                } else {
                    RemoveState::Prefix
                };
            }
        };

        let Some(child_node) = main_node.child.get_mut(&symbol) else {
            return RemoveState::NoSuchWord;
        };

        let result = Trie::recursive_remove(child_node, word);

        if result != RemoveState::LeafNode {
            return result;
        }
        main_node
            .child
            .remove(&symbol)
            .expect("symbol was found earlier");
        if main_node.child.len() == 0 {
            return RemoveState::LeafNode;
        }
        RemoveState::Prefix
    }
}

#[derive(PartialEq)]
enum RemoveState {
    NoSuchWord,
    Prefix,
    LeafNode,
}

#[derive(Debug)]
struct Node {
    child: BTreeMap<char, Node>,
    is_word: bool,
}

impl Node {
    fn new(is_word: bool) -> Self {
        Self {
            child: BTreeMap::new(),
            is_word,
        }
    }

    fn insert(&mut self, char: char) -> &mut Node {
        match self.child.entry(char) {
            Entry::Vacant(vacant) => vacant.insert(Self::new(false)),
            Entry::Occupied(occupied) => occupied.into_mut(),
        }
    }

    fn contains(&self, char: char) -> Option<&Node> {
        self.child.get(&char)
    }
}

fn main() {
    let mut tries = Trie::new();

    // tries.insert("");
    // tries.insert("mare");
    // tries.insert("mara");
    // tries.insert("mars");
    // tries.insert("mares");
    // tries.insert("maer");
    // tries.insert("max");
    // tries.insert("maresex");
    // tries.insert("mareble");
    // tries.insert("maredorable");
    // tries.insert("marefoo");
    // tries.insert("maresssssssss");
    // tries.insert("maremare");
    // tries.insert("maer");
    // tries.insert("max");
    // tries.insert("masex");

    // tries.insert("snow");
    // tries.insert("snowpity");
    // tries.insert("snowmare");

    // tries.insert("flutter");
    // tries.insert("fluttershy");
    // tries.insert("flut");
    // tries.insert("fluxx");
    // tries.insert("fluxxxx");

    tries.insert("foo");
    tries.insert("foobar");
    tries.insert("bar");
    tries.insert("fooqox");
    tries.insert("foobaz");

    // tries.contains("snow").unwrap();
    // println!("{}", tries.contains("maredorbla"));
    println!("{tries}");

    // tries.remove("foo");
    // tries.remove("foobar");
    // tries.remove("foobaz");
    // tries.remove("fooq");

    // println!("{tries}");
    // dbg!(tries.words());

    // dbg!(&tries);
}

impl<'a> FromIterator<&'a str> for Trie {
    fn from_iter<T: IntoIterator<Item = &'a str>>(iter: T) -> Self {
        let mut trie = Trie::new();
        for item in iter {
            trie.insert(&item.to_string())
        }
        trie
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use expect_test::{expect, Expect};

    fn assert_from_iter<'a>(to_insert: impl IntoIterator<Item = &'a str>, expect: Expect) {
        // to_insert.into_iter().collect::<Trie>();
        let actual = Trie::from_iter(to_insert);
        expect.assert_eq(&actual.to_string());
    }

    #[test]
    fn smoke_test() {
        assert_from_iter(
            ["mare", "mara", "mars", "mares", "maer", "max", "maresex"],
            expect![[r#"
                └──m
                   └──a
                      ├──e
                      │  └──r *
                      ├──r
                      │  ├──a *
                      │  ├──e *
                      │  │  └──s *
                      │  │     └──e
                      │  │        └──x *
                      │  └──s *
                      └──x *
            "#]],
        )
    }

    #[test]
    fn empty() {
        assert_from_iter([], expect![[r#""#]]);
        assert_from_iter(
            [""],
            expect![[r#"
            *
        "#]],
        );
    }

    #[test]
    fn nesting_1() {
        assert_from_iter(
            [
                "xxx", "xxy", "xxz", "xyx", "xyy", "xyz", "xzx", "xzy", "xzz",
            ],
            expect![[r#"
                └──x
                   ├──x
                   │  ├──x *
                   │  ├──y *
                   │  └──z *
                   ├──y
                   │  ├──x *
                   │  ├──y *
                   │  └──z *
                   └──z
                      ├──x *
                      ├──y *
                      └──z *
            "#]],
        )
    }

    #[test]
    fn nesting_2() {
        assert_from_iter(
            ["xy", "xz", "xxy", "xxz", "xxxy", "xxxz", "xxxxx", "y"],
            expect![[r#"
            ├──x
            │  ├──x
            │  │  ├──x
            │  │  │  ├──x
            │  │  │  │  └──x *
            │  │  │  ├──y *
            │  │  │  └──z *
            │  │  ├──y *
            │  │  └──z *
            │  ├──y *
            │  └──z *
            └──y *
        "#]],
        );
    }
}
